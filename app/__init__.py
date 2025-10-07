#===========================================================
# YOUR PROJECT TITLE HERE
# YOUR NAME HERE
#-----------------------------------------------------------
# BRIEF DESCRIPTION OF YOUR PROJECT HERE
#===========================================================

from flask import Flask, render_template, request, flash, redirect, session
import html

from app.helpers.session import init_session
from app.helpers.db      import connect_db
from app.helpers.errors  import init_error, not_found_error
from app.helpers.logging import init_logging
from app.helpers.dates   import init_datetime, utc_datetime_str, utc_date_str, utc_time_str
from datetime            import date


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
        # Get all the teams from the DB
        sql = "SELECT id, name FROM teams ORDER BY name ASC"
        params = []
        result = client.execute(sql, params)
        teams = result.rows

        # And show them on the page
        return render_template("pages/football.jinja", teams=teams)
    
#------------------------------------------------------------
# makes the form for the admin to sing in with 
#-------------------------------------------------------------
@app.get("/sign-in")
def sign_in_form():
    return render_template("pages/admin-sign-in.jinja",)

    
#------------------------------------------------------------
# Lets the admin sign in and lets them go to the admin page
#-------------------------------------------------------------
@app.post("/sign-in")
def sign_in():
    password = request.form.get("password")

    if password == "hello":
        session['admin'] = True
        return redirect("/admin")
    else:
        session['admin'] = False
        flash("Incorrect password")
        return redirect("/sign-in")

    
#------------------------------------------------------------
# a button the sign out the admin
#-------------------------------------------------------------
@app.get("/sign-out")
def sign_out():
    session['admin'] = False
    return redirect("/")

    
#-----------------------------------------------------------
#if admin = false the user can't enter this page other wise they go back to home page
#-----------------------------------------------------------
@app.get("/admin")
def show_admin():
    if session['admin']:
        with connect_db() as client:
            # Get all the teams from the DB
            sql = "SELECT id, name FROM teams ORDER BY name ASC"
            params = []
            result = client.execute(sql, params)
            teams = result.rows

            # And show them on the page

            return render_template("pages/admin.jinja", teams=teams)

    return redirect("/")

#-----------------------------------------------------------
# team page route - Show details of a single team
#-----------------------------------------------------------
@app.get("/team/<int:id>")
def show_one_team(id):
    with connect_db() as client:
        # Get the team details from the DB
        sql = "SELECT id, name, details, players FROM teams WHERE id=?"
        params = [id]
        result = client.execute(sql, params)

        # Did we get a result?
        if result.rows:
            # yes, so show it on the page
            team = result.rows[0]

          # Get the current local date in ISO format
            today = date.today().strftime('%Y-%m-%d')

            # Get the game details from the DB
            sql = """
                SELECT 
                    games.id,
                    games.location,
                    games.date,
                    games.time,
                    CASE
                        WHEN games.team1 = ? 
                        THEN t2.name
                        ELSE t1.name
                    END AS opponent
                
                FROM games 
                JOIN teams AS t1 ON games.team1 = t1.id
                JOIN teams AS t2 ON games.team2 = t2.id
                
                WHERE (games.team1 = ? OR games.team2 = ?)
                AND games.date >= ?
                
            """
            params = [id, id, id, today]
            result = client.execute(sql, params)
            games = result.rows


            

            return render_template("pages/team.jinja", team=team, games=games)

        else:
            # No, so show error
            return not_found_error()
        
#-----------------------------------------------------------
# team-admin page route - Show details of a single team and lets the user edit it's infomation
#-----------------------------------------------------------
@app.get("/team-admin/<int:id>")
def show_team_form(id):
    with connect_db() as client:
        # Get the team details from the DB
        sql = "SELECT id, name, details, players FROM teams WHERE id=?"
        params = [id]
        result = client.execute(sql, params)

        # Did we get a result?
        if result.rows:
            # yes, so show it on the page
            team = result.rows[0]

            
            # Get the current local date in ISO format
            today = date.today().strftime('%Y-%m-%d')

            # Get the game details from the DB
            sql = """
                SELECT 
                    games.id,
                    games.location,
                    games.date,
                    games.time,
                    CASE
                        WHEN games.team1 = ? 
                        THEN t2.name
                        ELSE t1.name
                    END AS opponent
                
                FROM games 
                JOIN teams AS t1 ON games.team1 = t1.id
                JOIN teams AS t2 ON games.team2 = t2.id
                
                WHERE (games.team1 = ? OR games.team2 = ?)
                AND games.date >= ?
                
            """
            params = [id, id, id, today]
            result = client.execute(sql, params)
            games = result.rows


            # Get the team details from the DB
            sql = "SELECT id, name, details FROM teams WHERE id != ?"
            params = [id]
            result = client.execute(sql, params)
            other_teams = result.rows

            return render_template("pages/team-admin.jinja", 
                                   team=team, 
                                   games=games,
                                   other_teams=other_teams 
            )
                                
        else:
            # No, so show error
            return not_found_error()
        
#-----------------------------------------------------------
# Route for adding a game, using data posted from a form
#-----------------------------------------------------------
@app.post("/game")
def add_a_game():
    # Get the data from the form
    location  = request.form.get("location")
    date = request.form.get("date")
    time = request.form.get("time")
    team1 = request.form.get("team1")
    team2 = request.form.get("team2")
    # Sanitise the text inputs
    location = html.escape(location)
    date = html.escape(date)
    time = html.escape(time)
    team1 = html.escape(team1)
    team2 = html.escape(team2)

    with connect_db() as client:
        # Add the row to the DB
        sql = "INSERT INTO games ( location,date,time,team1,team2) VALUES (?, ?, ?, ? ,?)"
        params = [location,date,time,team1,team2]
        client.execute(sql, params)

        # Go back to the home page
        flash(f" game '{location,date,time,team2}'added", "success")
        return redirect("/admin")
    #-----------------------------------------------------------
# Route for adding a team, using data posted from a form
#-----------------------------------------------------------
@app.post("/team")
def add_a_team():
    # Get the data from the form
    name  = request.form.get("name")
    details = request.form.get("details")
    players = request.form.get("players")

    # Sanitise the text inputs
    name = html.escape(name)
    details = html.escape(details)
    players = html.escape(players)

    with connect_db() as client:
        # Add the row to the DB
        sql = "INSERT INTO teams (name,details,players) VALUES (?, ?, ?)"
        params = [name,details,players]
        client.execute(sql, params)

        # Go back to the home page
        flash(f" game '{name,details,players}'added", "success")
        return redirect("/admin")
    

