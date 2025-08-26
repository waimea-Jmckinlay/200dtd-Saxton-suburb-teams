#===========================================================
# YOUR PROJECT TITLE HERE
# YOUR NAME HERE
#-----------------------------------------------------------
# BRIEF DESCRIPTION OF YOUR PROJECT HERE
#===========================================================

from flask import Flask, render_template, request, flash, redirect
import html

from app.helpers.session import init_session
from app.helpers.db      import connect_db
from app.helpers.errors  import init_error, not_found_error
from app.helpers.logging import init_logging
from app.helpers.time    import init_datetime, utc_timestamp, utc_timestamp_now


# Create the app
app = Flask(__name__)

# Configure app
init_session(app)   # Setup a session for messages, etc.
init_logging(app)   # Log requests
init_error(app)     # Handle errors and exceptions
init_datetime(app)  # Handle UTC dates in timestamps


#-----------------------------------------------------------
# Home page route
#-----------------------------------------------------------
@app.get("/")
def index():
    with connect_db() as client:
        # Get all the things from the DB
        sql = "SELECT id, name FROM teams ORDER BY name ASC"
        params = []
        result = client.execute(sql, params)
        teams = result.rows

        # And show them on the page
        return render_template("pages/home.jinja", teams=teams)
    
#-----------------------------------------------------------
#admin page route
#-----------------------------------------------------------
@app.get("/admin")
def show_admin():
    with connect_db() as client:
        # Get all the things from the DB
        sql = "SELECT id, name FROM teams ORDER BY name ASC"
        params = []
        result = client.execute(sql, params)
        teams = result.rows

        # And show them on the page

        return render_template("pages/admin.jinja", teams=teams)


#-----------------------------------------------------------
# Thing page route - Show details of a single thing
#-----------------------------------------------------------
@app.get("/team/<int:id>")
def show_one_thing(id):
    with connect_db() as client:
        # Get the thing details from the DB
        sql = "SELECT name, details, players FROM teams WHERE id=?"
        params = [id]
        result = client.execute(sql, params)

        # Did we get a result?
        if result.rows:
            # yes, so show it on the page
            team = result.rows[0]

            # Get the thing details from the DB
            sql = "SELECT location, date, time FROM games WHERE team1=? OR team2=?"
            params = [id, id]
            result = client.execute(sql, params)
            games = result.rows

            return render_template("pages/team.jinja", team=team, games=games)

        else:
            # No, so show error
            return not_found_error()
        

#-----------------------------------------------------------
# Route for adding a thing, using data posted from a form
#-----------------------------------------------------------
@app.post("/add")
def add_a_thing():
    # Get the data from the form
    location  = request.form.get("location")
    date = request.form.get("date")
    time = request.form.get("time")
    team1= request.form.get("team1")
    team2 = request.form.get("team2")
    # Sanitise the text inputs
    location = html.escape(location)
    date = html.escape(date)
    time = html.escape(time)
    team1 = html.escape(team1)
    team2 = html.escape(team2)

    with connect_db() as client:
        # Add the thing to the DB
        sql = "INSERT INTO games ( location,date,time,team1,team2) VALUES (?, ?, ?, ? ,?)"
        params = [location,date,time,team1,team2]
        client.execute(sql, params)

        # Go back to the home page
        flash(f" game '{location,date,time,team2}'added", "success")
        return redirect("/edit")
#-----------------------------------------------------------
# Route for deleting a thing, Id given in the route
#-----------------------------------------------------------
@app.get("/delete/<int:id>")
def delete_a_thing(id):
    with connect_db() as client:
        # Delete the thing from the DB
        sql = "DELETE FROM games WHERE id=?"
        params = [id]
        client.execute(sql, params)

        # Go back to the home page
        flash("Thing deleted", "success")
        return redirect("/edit")
