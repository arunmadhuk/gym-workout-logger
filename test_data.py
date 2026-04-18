test_exercises_data = [
    {
        "name": "Running",
        "exercise_type": "cardio",
        "equipment": "none",
        "difficulty": "beginner",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 30  # 30 minutes
    },
    {
        "name": "Bench Press",
        "exercise_type": "strength",
        "equipment": "barbell",
        "difficulty": "intermediate",
        "sets": 4,
        "reps": 8,
        "weight_kg": 60.0,
        "duration_minutes": None
    },
    {
        "name": "Yoga Stretch",
        "exercise_type": "flexibility",
        "equipment": "none",
        "difficulty": "beginner",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 15  # 15 minutes
    },
    {
        "name": "Single-Leg Stand",
        "exercise_type": "balance",
        "equipment": "none",
        "difficulty": "intermediate",
        "sets": 3,
        "reps": 5,
        "weight_kg": None,
        "duration_minutes": 1
    },
    {
        "name": "Deadlift",
        "exercise_type": "strength",
        "equipment": "barbell",
        "difficulty": "advanced",
        "sets": 5,
        "reps": 5,
        "weight_kg": 100.0,
        "duration_minutes": None
    },
    {
        "name": "Kettlebell Swing",
        "exercise_type": "cardio",
        "equipment": "kettlebell",
        "difficulty": "intermediate",
        "sets": 3,
        "reps": 15,
        "weight_kg": 16.0,
        "duration_minutes": None
    },
    {
        "name": "Pull-ups",
        "exercise_type": "strength",
        "equipment": "machine",
        "difficulty": "advanced",
        "sets": 3,
        "reps": 10,
        "weight_kg": None,
        "duration_minutes": None
    },
    {
        "name": "Resistance Band Stretch",
        "exercise_type": "flexibility",
        "equipment": "resistance_bands",
        "difficulty": "beginner",
        "sets": 2,
        "reps": 10,
        "weight_kg": None,
        "duration_minutes": 2
    },
    {
        "name": "Dumbbell Rows",
        "exercise_type": "strength",
        "equipment": "dumbbells",
        "difficulty": "intermediate",
        "sets": 4,
        "reps": 12,
        "weight_kg": 15.0,
        "duration_minutes": None
    },
    {
        "name": "Stationary Bike",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "beginner",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 40  # 40 minutes
    }
]

from datetime import date, time, timedelta

test_workout_sessions_data = [
    {
        "user_id": 1,
        "session_date": date(2026, 3, 15),
        "start_time": time(7, 0, 0),  # 7:00 AM
        "end_time": time(8, 0, 0),    # 8:00 AM
        "duration_minutes": 60,
        "calories_burned": 450,
        "notes": "Morning cardio session - felt energetic",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 3, 17),
        "start_time": time(18, 30, 0),  # 6:30 PM
        "end_time": time(19, 15, 0),    # 7:15 PM
        "duration_minutes": 45,
        "calories_burned": 380,
        "notes": "Strength training - upper body focus",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 3, 20),
        "start_time": time(6, 45, 0),   # 6:45 AM
        "end_time": time(7, 30, 0),     # 7:30 AM
        "duration_minutes": 45,
        "calories_burned": 320,
        "notes": "Yoga and stretching",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 3, 22),
        "start_time": time(17, 0, 0),    # 5:00 PM
        "end_time": time(18, 30, 0),     # 6:30 PM
        "duration_minutes": 90,
        "calories_burned": 650,
        "notes": "Leg day - heavy squats and deadlifts",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 3, 25),
        "start_time": time(7, 15, 0),    # 7:15 AM
        "end_time": time(7, 45, 0),      # 7:45 AM
        "duration_minutes": 30,
        "calories_burned": 250,
        "notes": "Quick HIIT session",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 3, 28),
        "start_time": time(19, 0, 0),    # 7:00 PM
        "end_time": time(20, 0, 0),      # 8:00 PM
        "duration_minutes": 60,
        "calories_burned": 500,
        "notes": "Full body workout",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 3, 30),
        "start_time": time(6, 30, 0),    # 6:30 AM
        "end_time": time(7, 15, 0),      # 7:15 AM
        "duration_minutes": 45,
        "calories_burned": 350,
        "notes": "Core workout and light cardio",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 4, 2),
        "start_time": time(16, 0, 0),    # 4:00 PM
        "end_time": time(17, 30, 0),     # 5:30 PM
        "duration_minutes": 90,
        "calories_burned": 580,
        "notes": "Long run day",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 4, 5),
        "start_time": time(7, 0, 0),     # 7:00 AM
        "end_time": time(7, 30, 0),      # 7:30 AM
        "duration_minutes": 30,
        "calories_burned": 200,
        "notes": "Recovery session - light stretching",
        
       
    },
    {
        "user_id": 1,
        "session_date": date(2026, 4, 8),
        "start_time": time(18, 0, 0),    # 6:00 PM
        "end_time": time(19, 15, 0),     # 7:15 PM
        "duration_minutes": 75,
        "calories_burned": None,  # Not tracked
        "notes": "Swimming session",
        
       
    }
]


from gym_app.models import WorkoutSession
from datetime import date, time

from django.contrib.auth.models import User
user = User.objects.get(id=1)

for data in test_workout_sessions_data:
    # Remove created_at and updated_at as they're auto-managed
    session = WorkoutSession.objects.create(**data)
    print(f"Created: {session}")


from datetime import datetime, timezone
from decimal import Decimal

test_exercise_logs_data = [
    # Cardio logs
    {
        "workout_session_id": 1,  # Morning cardio session
        "exercise_id": 1,          # Running
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 30,    # 30 minutes (changed from seconds)
        "notes": "Maintained steady pace",
    },
    {
        "workout_session_id": 2,  # Strength training session
        "exercise_id": 2,          # Bench Press
        "sets_completed": 4,
        "reps_completed": 8,
        "weight_kg": 60.0,
        "duration_minutes": None,
        "notes": "Felt strong, could increase weight next time",
    },
    {
        "workout_session_id": 2,  # Same session - multiple exercises
        "exercise_id": 9,          # Dumbbell Rows
        "sets_completed": 4,
        "reps_completed": 12,
        "weight_kg": 15.0,
        "duration_minutes": None,
        "notes": "Good form maintained",
    },
    {
        "workout_session_id": 3,  # Yoga session
        "exercise_id": 3,          # Yoga Stretch
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 15,    # 15 minutes
        "notes": "Focused on deep breathing",
    },
    {
        "workout_session_id": 4,  # Leg day
        "exercise_id": 5,          # Deadlift
        "sets_completed": 5,
        "reps_completed": 5,
        "weight_kg": 100.0,
        "duration_minutes": None,
        "notes": "Personal best!",
    },
    {
        "workout_session_id": 4,  # Same leg day session
        "exercise_id": 7,          # Pull-ups
        "sets_completed": 3,
        "reps_completed": 10,
        "weight_kg": None,
        "duration_minutes": None,
        "notes": "Used assisted machine for last set",
    },
    {
        "workout_session_id": 5,  # HIIT session
        "exercise_id": 6,          # Kettlebell Swing
        "sets_completed": 3,
        "reps_completed": 15,
        "weight_kg": 16.0,
        "duration_minutes": None,
        "notes": "High intensity",
    },
    {
        "workout_session_id": 6,  # Full body workout
        "exercise_id": 4,          # Single-Leg Stand (balance)
        "sets_completed": 3,
        "reps_completed": 5,
        "weight_kg": None,
        "duration_minutes": 0.5,   # 30 seconds = 0.5 minutes
        "notes": "Improved stability",
    },
    {
        "workout_session_id": 7,  # Core workout
        "exercise_id": 8,          # Resistance Band Stretch
        "sets_completed": 2,
        "reps_completed": 10,
        "weight_kg": None,
        "duration_minutes": 2,     # 2 minutes
        "notes": "Good warmup",
    },
    {
        "workout_session_id": 10, # Swimming session
        "exercise_id": 10,         # Stationary Bike
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 40,    # 40 minutes
        "notes": "Used pool bike",
    }
]



from gym_app.models import ExerciseLog, WorkoutSession, Exercise

# Verify sessions and exercises exist
sessions = WorkoutSession.objects.filter(user_id=1)
exercises = Exercise.objects.all()
print(f"Sessions available: {sessions.count()}")
print(f"Exercises available: {exercises.count()}")

# Create exercise logs
created_count = 0
for data in test_exercise_logs_data:
    # Remove auto-generated fields if present
    data.pop('created_at', None)
    data.pop('updated_at', None)
    
    # Get the actual objects
    workout_session = WorkoutSession.objects.get(session_id=data.pop('workout_session_id'))
    exercise = Exercise.objects.get(exercise_id=data.pop('exercise_id'))
    
    # Create the log
    log = ExerciseLog.objects.create(
        workout_session=workout_session,
        exercise=exercise,
        **data
    )
    created_count += 1
    print(f"Created: {log} - Duration: {log.duration_minutes} minutes")

print(f"\nSuccessfully created {created_count} exercise logs")



from gym_app.models import User, ExerciseLog, WorkoutSession, Exercise

# Assuming you have a user instance
user = User.objects.get(user_id=3)

workout_sessions = [
    WorkoutSession.objects.create(user=user,session_date=date(2026, 4, 15),start_time=time(7, 0),end_time=time(7, 30),duration_minutes=30,calories_burned=120, notes="Morning yoga session"),
    WorkoutSession.objects.create(
        user=user,
        session_date=date(2026, 4, 16),
        start_time=time(18, 0),
        end_time=time(18, 45),
        duration_minutes=45,
        calories_burned=180,
        notes="Evening stretch"
    ),
    WorkoutSession.objects.create(
        user=user,
        session_date=date(2026, 4, 17),
        start_time=time(8, 30),
        end_time=time(9, 0),
        duration_minutes=30,
        calories_burned=110,
        notes="Quick morning stretch"
    ),
]

exercise_logs = []
for i, session in enumerate(workout_sessions):
    log = ExerciseLog.objects.create(
        workout_session=session,
        exercise=exercise,
        sets_completed=3,  # 3 sets
        reps_completed=1,  # Each set is 1 hold/stretch
        weight_kg=None,    # No weight for yoga
        duration_minutes=session.duration_minutes,
        notes=f"Yoga stretch session {i+1} - focused on full body flexibility"
    )
    exercise_logs.append(log)

print(exercise_logs)


yoga_variations = [
    {
        'session_date': date(2026, 4, 18),
        'start_time': time(7, 0),
        'end_time': time(8, 0),
        'duration': 60,
        'calories': 250,
        'sets': 4,
        'reps': 1,
        'notes': 'Power yoga - more intense'
    },
    {
        'session_date': date(2026, 4, 19),
        'start_time': time(20, 0),
        'end_time': time(20, 30),
        'duration': 30,
        'calories': 100,
        'sets': 2,
        'reps': 1,
        'notes': 'Gentle evening stretch'
    },
    {
        'session_date': date(2026, 4, 20),
        'start_time': time(6, 30),
        'end_time': time(7, 15),
        'duration': 45,
        'calories': 190,
        'sets': 3,
        'reps': 2,
        'notes': 'Morning flow with extra reps'
    },
]

for var in yoga_variations:
    session = WorkoutSession.objects.create(
        user=user,
        session_date=var['session_date'],
        start_time=var['start_time'],
        end_time=var['end_time'],
        duration_minutes=var['duration'],
        calories_burned=var['calories'],
        notes=var['notes']
    )
    
    ExerciseLog.objects.create(
        workout_session=session,
        exercise=exercise,
        sets_completed=var['sets'],
        reps_completed=var['reps'],
        weight_kg=None,
        duration_minutes=var['duration'],
        notes=f"Yoga stretch: {var['notes']}"
    )



#for user 3

from gym_app.models import User, ExerciseLog, WorkoutSession, Exercise
from datetime import datetime, timezone
from decimal import Decimal

test_exercise_logs_data = [
    {
        "workout_session_id": 12,  # Yoga session
        "exercise_id": 3,          # Yoga Stretch
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 15,    # 15 minutes
        "notes": "Focused on deep breathing",
    },
       {
        "workout_session_id": 13,  # Yoga session
        "exercise_id": 3,          # Yoga Stretch
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 15,    # 15 minutes
        "notes": "Focused on deep breathing",
    },
        {
        "workout_session_id": 14,  # Yoga session
        "exercise_id": 3,          # Yoga Stretch
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 15,    # 15 minutes
        "notes": "Focused on deep breathing",
    },
        {
        "workout_session_id": 15,  # Yoga session
        "exercise_id": 3,          # Yoga Stretch
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 15,    # 15 minutes
        "notes": "Focused on deep breathing",
    },
        {
        "workout_session_id": 16,  # Yoga session
        "exercise_id": 3,          # Yoga Stretch
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 15,    # 15 minutes
        "notes": "Focused on deep breathing",
    },
]

# Verify sessions and exercises exist
sessions = WorkoutSession.objects.filter(user_id=3)
exercises = Exercise.objects.all()
print(f"Sessions available: {sessions.count()}")
print(f"Exercises available: {exercises.count()}")

# Create exercise logs
created_count = 0
for data in test_exercise_logs_data:
    # Remove auto-generated fields if present
    data.pop('created_at', None)
    data.pop('updated_at', None)
    
    # Get the actual objects
    workout_session = WorkoutSession.objects.get(session_id=data.pop('workout_session_id'))
    exercise = Exercise.objects.get(exercise_id=data.pop('exercise_id'))
    
    # Create the log
    log = ExerciseLog.objects.create(
        workout_session=workout_session,
        exercise=exercise,
        **data
    )
    created_count += 1
    print(f"Created: {log} - Duration: {log.duration_minutes} minutes")

print(f"\nSuccessfully created {created_count} exercise logs")