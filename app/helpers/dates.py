#===========================================================
# Session Related Functions
# - Note that these require tzdata to be imported
#===========================================================

from datetime import datetime
from zoneinfo import ZoneInfo

DEFAULT_LOCAL_TZ = "Pacific/Auckland"
ISO_DATE_FORMAT  = "%Y-%m-%d"
ISO_TIME_FORMAT  = "%H:%M:%S"
DATE_TIME_FORMAT = f"{ISO_DATE_FORMAT} {ISO_TIME_FORMAT}"



#===========================================================
# Note: The following functions are used as Jinja template
#       filters, rather than being called directly


#-----------------------------------------------------------
# Convert a given datetime to local timezone
# - The datetime format is YYYY-MM-DD HH:MM:SS
# - The optional local_timezone defaults to NZ (inc. DST)
#-----------------------------------------------------------
def _utc_datetime_to_local_timezone(
    utc_datetime_str,
    datetime_format = DATE_TIME_FORMAT,
    output_format   = DATE_TIME_FORMAT,
    local_timezone  = DEFAULT_LOCAL_TZ
):
    utc_dt = datetime.strptime(utc_datetime_str, datetime_format)
    utc_dt = utc_dt.replace(tzinfo=ZoneInfo("UTC"))

    # Convert to local timezone
    local_dt = utc_dt.astimezone(ZoneInfo(local_timezone))

    # Format back into datetime string
    return local_dt.strftime(output_format)


#-----------------------------------------------------------
# Convert a given UTC date to local timezone
#-----------------------------------------------------------
def _utc_date_to_local_timezone(utc_date_str, local_timezone = DEFAULT_LOCAL_TZ):
    return _utc_datetime_to_local_timezone(
        utc_date_str,
        ISO_DATE_FORMAT,
        ISO_DATE_FORMAT,
        local_timezone
    )


#-----------------------------------------------------------
# Convert a given UTC time to local timezone
#-----------------------------------------------------------
def _utc_time_to_local_timezone(utc_time_str, local_timezone = DEFAULT_LOCAL_TZ):
    # Need to add in a date for time-only converions
    utc_date_str = datetime.now(ZoneInfo("UTC")).date()
    utc_datetime_str = f"{utc_date_str} {utc_time_str}"
    return _utc_datetime_to_local_timezone(
        utc_datetime_str,
        DATE_TIME_FORMAT,
        ISO_TIME_FORMAT,
        local_timezone
    )


#-----------------------------------------------------------
# Convert a given datetime to a more friendly format
# - The datetime format is YYYY-MM-DD HH:MM:SS
# - The optional format string as per https://strftime.org/
#-----------------------------------------------------------
def _timestamp_friendly(
    timestamp_str,
    datetime_format = DATE_TIME_FORMAT,
    friendly_format = "%a, %d/%m/%Y at %I:%M%p"
):
    dt = datetime.strptime(timestamp_str, datetime_format)

    # Format to a user-friendly string
    return dt.strftime(friendly_format)


#-----------------------------------------------------------
# Convert a given date to a more friendly DD/MM/YYY format
#-----------------------------------------------------------
def _date_friendly(date_str):
    return _timestamp_friendly(date_str, ISO_DATE_FORMAT, "%d/%m/%Y")


#-----------------------------------------------------------
# Convert a given date to a more friendly day of the week format
#-----------------------------------------------------------
def _day_friendly(date_str):
    return _timestamp_friendly(date_str, ISO_DATE_FORMAT, "%a")


#-----------------------------------------------------------
# Convert a given time to a more friendly HH:MM a/pm format
#-----------------------------------------------------------
def _time_friendly(time_str):
    return _timestamp_friendly(time_str, ISO_TIME_FORMAT, "%I:%M%p")


#-----------------------------------------------------------
# Register the above functions as Jinja filters
#-----------------------------------------------------------
def init_datetime(app):
    # Register Jinja filters for timezone adjusting
    app.jinja_env.filters['localtimestamp'] = _utc_datetime_to_local_timezone
    app.jinja_env.filters['localdate']      = _utc_date_to_local_timezone
    app.jinja_env.filters['localtime']      = _utc_time_to_local_timezone
    # Register Jinja filters for friendly versions
    app.jinja_env.filters['nicetimestamp']  = _timestamp_friendly
    app.jinja_env.filters['nicedate']       = _date_friendly
    app.jinja_env.filters['nicetime']       = _time_friendly
    app.jinja_env.filters['niceday']        = _day_friendly



#===========================================================
# Note: The following functions are used directly when
#       processing dates/times from HTML form inputs


#-----------------------------------------------------------
# Create a UTC timestamp, optionally providing a local date
# and local time string (e.g. from a HTML form)
# - local_date_str is in format "YYYY-MM-DD"
# - local_time_str is in format "HH:MM" or "HH:MM:SS"
# - Returns UTC timestamp in format "YYYY-MM-DD HH:MM:SS"
#-----------------------------------------------------------
def utc_datetime_str(
    local_date_str = None,
    local_time_str = None,
    format         = DATE_TIME_FORMAT,
    local_timezone = DEFAULT_LOCAL_TZ
):
    # Deal with optional date/time
    if not local_date_str:
        local_date_str = datetime.now().strftime(ISO_DATE_FORMAT)
    if not local_time_str:
        local_time_str = datetime.now().strftime(ISO_TIME_FORMAT)

    local_tz = ZoneInfo(local_timezone)

    # If no seconds provided, add some
    if len(local_time_str) == 5:
        local_time_str += ":00"

    # Parse the combined date and time string
    local_dt_str = f"{local_date_str} {local_time_str}"
    local_dt = datetime.strptime(local_dt_str, DATE_TIME_FORMAT)
    local_dt = local_dt.replace(tzinfo=local_tz)

    # Convert to UTC
    utc_dt = local_dt.astimezone(ZoneInfo("UTC"))

    # Format as UTC timestamp string
    return utc_dt.strftime(format)


#-----------------------------------------------------------
# Create a UTC datestamp from a given local date
# - local_date_str is in format "YYYY-MM-DD"
# - Returns UTC datestamp in format "YYYY-MM-DD"
#-----------------------------------------------------------
def utc_date_str(
    local_date_str = None,
    local_timezone = DEFAULT_LOCAL_TZ
):
    return utc_datetime_str(
        local_date_str = local_date_str if local_date_str else datetime.now().strftime(ISO_DATE_FORMAT),
        format         = ISO_DATE_FORMAT,
        local_timezone = local_timezone
    )


#-----------------------------------------------------------
# Create a UTC timestamp from a given local time
# - local_time_str is in format "HH:MM:SS" or "HH:MM"
# - Returns UTC timestamp in format "HH:MM:SS"
#-----------------------------------------------------------
def utc_time_str(
    local_time_str = None,
    local_timezone = DEFAULT_LOCAL_TZ
):
    return utc_datetime_str(
        local_time_str = local_time_str if local_time_str else datetime.now().strftime(ISO_TIME_FORMAT),
        format         = ISO_TIME_FORMAT,
        local_timezone = local_timezone
    )
