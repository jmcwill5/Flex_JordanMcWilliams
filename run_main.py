'''run_main.py

This script sets up a Flask web application that allows users to search for exercises based on muscle groups and difficulty levels.
It also enables the creation of a personalized exercise plan by adding and removing exercises.'''


# Necessary imports
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Set working directory
os.chdir(os.path.dirname(os.path.abspath(__file__))) # change working directory to the directory of this script
print("Current working directory:", os.getcwd())

# Load dataframe once globally
dfg = pd.read_csv('data/exercises.csv', encoding='latin1')
dfg['primaryMuscles'] = dfg['primaryMuscles'].str.lower()
dfg['level'] = dfg['level'].str.lower()

@app.route('/')
def home():
    '''Route to home page'''
    return render_template('home.html')

@app.route('/search')
def search():
    '''Search function to handle requests for specific muscle types and difficulty levels.
    Returns a results page with a filtered list of exercises based on user input.'''
    muscle = request.args.get('muscle', '').lower()
    level = request.args.get('level', '').lower()

    # use a copy to avoid modifying the global dataframe
    df = dfg.copy()

    df['primaryMuscles'] = df['primaryMuscles'].str.lower()
    df['level'] = df['level'].str.lower()

    # filter by muscle
    if muscle:
        df = df[df['primaryMuscles'].str.contains(muscle, na=False)] # Allows for matches that are not exact
        
    # filter by level
    if level != 'all':
        df = df[df['level'] == level]

    # return the results page with filtered exercises
    results = df.to_dict(orient='records')
    return render_template('results.html', results=results, muscle=muscle, level=level) 

plan = [] # will store temporary exercise plan

@app.route('/add_to_plan', methods=['POST'])
def add_to_plan():
    '''Adds exercises to the user's exercise plan if not already present'''
    exercise = {
        'name': request.form['name'],
        'muscle': request.form['muscle'],
        'level': request.form['level'],
        'instructions': request.form['instructions']
    }

    if exercise not in plan:
        plan.append(exercise)
    return redirect(request.referrer)

@app.route('/my_exercise_plan')
def view_plan():
    '''Routes to the user's exercise plan page, displaying all exercises added by the user.'''
    return render_template('my_exercise_plan.html', plan=plan)

@app.route('/delete_from_plan', methods=['POST'])
def delete_from_plan():
    '''Deletes an exercise from the user's exercise plan based on user input.'''
    exercise_delete = {
        'name': request.form['name'],
        'muscle': request.form['muscle'],
        'level': request.form['level'],
        'instructions': request.form['instructions']
    }

    global plan
    plan = [ex for ex in plan if ex != exercise_delete]

    return redirect(url_for('view_plan'))

if __name__ == '__main__':
    app.run(debug=False)