from django.shortcuts import render, redirect
from .utils import get_db_connection
from bson import ObjectId
from datetime import datetime

def home(request):
    db = get_db_connection()
    last_workout = db.workouts.find_one(sort=[("date", -1)])
    goals = list(db.goals.find())
    
    for goal in goals:
        goal['progress'] = int((goal['current_value'] / goal['target_value']) * 100) if goal['target_value'] else 0
    
    return render(request, 'fitness_app/home.html', {
        'last_workout': last_workout,
        'goals': goals[:3]
    })

def log_workout(request):
    if request.method == 'POST':
        db = get_db_connection()
        workout = {
            'exercise_name': request.POST.get('exercise_name'),
            'sets': int(request.POST.get('sets')),
            'reps': int(request.POST.get('reps')),
            'weight': float(request.POST.get('weight')),
            'notes': request.POST.get('notes', ''),
            'date': datetime.now(),
            'category': 'strength'
        }
        db.workouts.insert_one(workout)
        return redirect('workout_history')
    return render(request, 'fitness_app/log_workout.html')

def workout_history(request):
    db = get_db_connection()
    workouts = list(db.workouts.find().sort("date", -1))
    return render(request, 'fitness_app/workout_history.html', {'workouts': workouts})

def set_goal(request, goal_id=None):
    db = get_db_connection()
    goal = None
    
    if goal_id:
        goal = db.goals.find_one({'_id': ObjectId(goal_id)})
    
    if request.method == 'POST':
        target_date = request.POST.get('target_date')
        # Ensure date is saved in consistent format
        goal_data = {
            'goal_name': request.POST.get('goal_name'),
            'current_value': float(request.POST.get('current_value', 0)),
            'target_value': float(request.POST.get('target_value')),
            'target_date': target_date  # Store as string in YYYY-MM-DD format
        }
        
        if goal_id:
            db.goals.update_one({'_id': ObjectId(goal_id)}, {'$set': goal_data})
        else:
            db.goals.insert_one(goal_data)
        
        return redirect('view_goals')
    
    return render(request, 'fitness_app/set_goal.html', {'goal': goal})

def view_goals(request):
    db = get_db_connection()
    goals = list(db.goals.find())
    
    for goal in goals:
        goal['progress'] = int((goal['current_value'] / goal['target_value']) * 100) if goal['target_value'] else 0
        goal['goal_id'] = str(goal['_id'])  # Convert ObjectId to string
    
    return render(request, 'fitness_app/view_goals.html', {'goals': goals})