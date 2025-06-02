from datetime import datetime

class Workout:
    def __init__(self, user_id, exercise_name, sets, reps, weight, date=None, notes=""):
        self.user_id = user_id
        self.exercise_name = exercise_name
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.date = date or datetime.now()
        self.notes = notes
        self.category = "strength"  # default

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'exercise_name': self.exercise_name,
            'sets': self.sets,
            'reps': self.reps,
            'weight': self.weight,
            'date': self.date,
            'notes': self.notes,
            'category': self.category
        }

class FitnessGoal:
    def __init__(self, user_id, goal_name, target_value, target_date, current_value=0):
        self.user_id = user_id
        self.goal_name = goal_name
        self.target_value = target_value
        self.target_date = target_date
        self.current_value = current_value

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'goal_name': self.goal_name,
            'target_value': self.target_value,
            'target_date': self.target_date,
            'current_value': self.current_value
        }