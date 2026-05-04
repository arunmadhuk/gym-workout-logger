#python manage.py shell

from gym_app.models import Exercise, WorkoutSession, ExerciseLog
from datetime import date, time
from gym_app.models import User

user = User.objects.get(id=1)

workout_sessions_data = [
    {
        "user": user,
        "session_date": date(2026, 5, 1),
        "start_time": time(6, 30),  # 6:30 AM
        "end_time": time(7, 15),    # 7:15 AM
        "duration_minutes": 45,
        "calories_burned": 350,
        "notes": "Morning cycling session - leisure pace",
    },
    {
        "user": user,
        "session_date": date(2026, 5, 2),
        "start_time": time(17, 0),  # 5:00 PM
        "end_time": time(17, 45),   # 5:45 PM
        "duration_minutes": 45,
        "calories_burned": 420,
        "notes": "HIIT cycling - intervals",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 25),
        "start_time": time(7, 0),   # 7:00 AM
        "end_time": time(9, 0),     # 9:00 AM
        "duration_minutes": 120,
        "calories_burned": 780,
        "notes": "Weekend long ride - mountain trails",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 26),
        "start_time": time(18, 30), # 6:30 PM
        "end_time": time(19, 30),   # 7:30 PM
        "duration_minutes": 60,
        "calories_burned": 500,
        "notes": "Indoor spin class",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 28),
        "start_time": time(6, 0),   # 6:00 AM
        "end_time": time(9, 0),     # 9:00 AM
        "duration_minutes": 180,
        "calories_burned": 1100,
        "notes": "Endurance road cycling - 50km",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 30),
        "start_time": time(16, 0),  # 4:00 PM
        "end_time": time(16, 40),   # 4:40 PM
        "duration_minutes": 40,
        "calories_burned": 280,
        "notes": "Recumbent bike - recovery ride",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 22),
        "start_time": time(7, 30),  # 7:30 AM
        "end_time": time(8, 30),    # 8:30 AM
        "duration_minutes": 60,
        "calories_burned": 550,
        "notes": "Hill repeats training",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 23),
        "start_time": time(8, 0),   # 8:00 AM
        "end_time": time(8, 35),    # 8:35 AM
        "duration_minutes": 35,
        "calories_burned": 200,
        "notes": "Commute to work",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 25),
        "start_time": time(17, 30), # 5:30 PM
        "end_time": time(17, 45),   # 5:45 PM
        "duration_minutes": 15,
        "calories_burned": 180,
        "notes": "Time trial - maximum effort",
    },
    {
        "user": user,
        "session_date": date(2026, 4, 27),
        "start_time": time(19, 0),  # 7:00 PM
        "end_time": time(19, 55),   # 7:55 PM
        "duration_minutes": 55,
        "calories_burned": 480,
        "notes": "Virtual cycling on Zwift",
    },
]

created_sessions = []
for data in workout_sessions_data:
    # Remove user_id and get the actual User object

    session, created = WorkoutSession.objects.get_or_create(
        user=data['user'],
        session_date=data['session_date'],
        start_time=data['start_time'],
        defaults=data
    )
    created_sessions.append(session)
    print(f"{'Created' if created else 'Found'}: {session}")

cycling_exercises_data = [
    {
        "name": "Outdoor Cycling - Leisure",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "beginner",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 45,
    },
    {
        "name": "Stationary Bike - HIIT",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "intermediate",
        "sets": 5,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 25,
    },
    {
        "name": "Mountain Biking",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "advanced",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 90,
    },
    {
        "name": "Indoor Cycling Class",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "intermediate",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 60,
    },
    {
        "name": "Road Cycling - Long Distance",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "advanced",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 180,
    },
    {
        "name": "Recumbent Bike",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "beginner",
        "sets": 2,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 20,
    },
    {
        "name": "Cycling - Hill Repeats",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "advanced",
        "sets": 8,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 40,
    },
    {
        "name": "Commuter Cycling",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "beginner",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 35,
    },
    {
        "name": "Cycling - Time Trial",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "intermediate",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 15,
    },
    {
        "name": "Virtual Cycling (Zwift)",
        "exercise_type": "cardio",
        "equipment": "machine",
        "difficulty": "intermediate",
        "sets": 1,
        "reps": 1,
        "weight_kg": None,
        "duration_minutes": 55,
    }
]
created_exercises = []
for data in cycling_exercises_data:
    exercise, created = Exercise.objects.get_or_create(
        name=data['name'],
        defaults={
            'exercise_type': data['exercise_type'],
            'equipment': data['equipment'],
            'difficulty': data['difficulty'],
            'sets': data['sets'],
            'reps': data['reps'],
            'weight_kg': data.get('weight_kg'),
            'duration_minutes': data.get('duration_minutes'),
        }
    )
    created_exercises.append(exercise)
    print(f"{'Created' if created else 'Found'}: {exercise.name} (ID: {exercise.exercise_id})")

test_cycling_exercise_logs_data = [
    {
        "workout_session_id": 18,
        "exercise_id": 11,  # Outdoor Cycling - Leisure
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 45,
        "notes": "Morning ride around the park, moderate pace",
    },
    {
        "workout_session_id": 19,
        "exercise_id": 12,  # Stationary Bike - HIIT
        "sets_completed": 5,
        "reps_completed": 1,  # 5 intervals of high intensity
        "weight_kg": None,
        "duration_minutes": 25,
        "notes": "30 sec sprint / 90 sec recovery pattern",
    },
    {
        "workout_session_id": 20,
        "exercise_id": 13,  # Mountain Biking
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 90,
        "notes": "Trail riding with steep climbs",
    },
    {
        "workout_session_id": 21,
        "exercise_id": 14,  # Indoor Cycling Class
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 60,
        "notes": "Spin class with resistance changes",
    },
    {
        "workout_session_id": 22,
        "exercise_id": 15,  # Road Cycling - Long Distance
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 180,  # 3 hours
        "notes": "Endurance training, 50km ride",
    },
    {
        "workout_session_id": 23,
        "exercise_id": 16,  # Recumbent Bike
        "sets_completed": 2,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 20,
        "notes": "Low-impact cardio, focused on steady pace",
    },
    {
        "workout_session_id": 24,
        "exercise_id": 17,  # Cycling - Hill Repeats
        "sets_completed": 8,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 40,
        "notes": "2-minute climb repeats on 8% grade",
    },
    {
        "workout_session_id": 25,
        "exercise_id": 18,  # Commuter Cycling
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 35,
        "notes": "Work commute, stop-and-go traffic",
    },
    {
        "workout_session_id": 26,
        "exercise_id": 19,  # Cycling - Time Trial
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 15,
        "notes": "Maximum effort on flat course",
    },
    {
        "workout_session_id": 27,
        "exercise_id": 20,  # Virtual Cycling (Zwift)
        "sets_completed": 1,
        "reps_completed": 1,
        "weight_kg": None,
        "duration_minutes": 55,
        "notes": "Virtual group ride, simulated hills",
    }
]

created_logs = []
for data in test_cycling_exercise_logs_data:
    workout_session = WorkoutSession.objects.get(session_id=data['workout_session_id'])
    exercise = Exercise.objects.get(exercise_id=data['exercise_id'])
    
    log = ExerciseLog.objects.create(
        workout_session=workout_session,
        exercise=exercise,
        sets_completed=data['sets_completed'],
        reps_completed=data['reps_completed'],
        weight_kg=data.get('weight_kg'),
        duration_minutes=data['duration_minutes'],
        notes=data['notes']
    )
    created_logs.append(log)
    print(f"Created log: {log} - {log.duration_minutes} minutes")

print(f"\n✅ Created {len(created_exercises)} cycling exercises")
print(f"✅ Created {len(created_logs)} cycling exercise logs")

# Display summary
print("\n📊 Cycling Workout Summary:")
print("-" * 50)
total_minutes = 0
for log in created_logs:
    total_minutes += log.duration_minutes
    print(f"• {log.exercise.name}: {log.duration_minutes} min - {log.notes}")
print("-" * 50)
print(f"🏆 Total cycling time: {total_minutes} minutes ({total_minutes/60:.1f} hours)")