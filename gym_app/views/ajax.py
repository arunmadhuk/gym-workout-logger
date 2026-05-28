from django.http import HttpResponse, JsonResponse
from gym_app.models import Exercise, ExerciseLog

def load_selected_exercise_ajax(request):
    exercise_name = request.GET['exercise_name']
    print("exercise_name : '{}'".format(exercise_name))
    data = {}
    if exercise_name:
        qs=Exercise.objects.get(name=exercise_name)
        print("Queryset : '{}'".format(qs))
        data = {
            "exercise_type": qs.exercise_type,
            "equipment": qs.equipment,
            "difficulty": qs.difficulty,
            "sets": qs.sets,
            "reps": qs.reps,
            "weight_kg": qs.weight_kg,
            "duration_minutes": qs.duration_minutes,
            "distance_km": qs.distance_km,
            "description": qs.description
        }
        print("Data : '{}'".format(data))
    else:
        print("No exercise name provided in the request.")

    return JsonResponse(data, safe=False)


def load_selected_workout_ajax(request):
    log_id = request.GET['log_id']
    print("log_id : '{}'".format(log_id))
    data = {}
    if log_id:
        exercise_logs = ExerciseLog.objects.filter(log_id=log_id).select_related('workout_session', 'exercise').order_by('-created_at')

        if exercise_logs:
            log = exercise_logs.first()
            data = {
                "session_date": log.workout_session.session_date,
                "start_time": log.workout_session.start_time,
                "end_time": log.workout_session.end_time,
                "session_duration": log.workout_session.duration_minutes,   
                "calories_burned": log.workout_session.calories_burned,
                "session_notes": log.workout_session.notes,
                "exercise_name": log.exercise.name,
                "exercise_type": log.exercise.exercise_type,
                "equipment": log.exercise.equipment,
                "difficulty": log.exercise.difficulty,
                "sets_completed": log.sets_completed,
                "reps_completed": log.reps_completed,
                "weight_kg": log.weight_kg,
                "sets": log.exercise.sets,
                "reps": log.exercise.reps,
                "distance_km": log.exercise.distance_km,
                "exercise_duration": log.duration_minutes,   
                "exercise_description": log.exercise.description,
                "exercise_notes": log.notes,
            }
        else:
            print(f"No exercise logs found for log_id: {log_id}")
            data = {"error": "No exercise logs found for the provided log ID."}

    else:
        print("No log ID provided in the request.")

    return JsonResponse(data, safe=False)