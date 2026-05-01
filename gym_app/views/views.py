from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from gym_app.models import ExerciseLog, WorkoutSession

@login_required
def dashboard(request):
    # Get current user's exercise logs
    user_logs = ExerciseLog.objects.filter(
        workout_session__user=request.user
    ).select_related('exercise', 'workout_session').order_by('-workout_session__session_date')
    
    # Total stats
    total_workouts = WorkoutSession.objects.filter(user=request.user).count()
    total_exercises = user_logs.count()
    
    # Calculate totals using loops
    total_sets = 0
    total_reps = 0
    total_volume = 0
    total_duration = 0
    weekday_counts = {}
    exercise_type_counts = {}
    exercise_counts = {}
    exercise_sets = {}
    
    for log in user_logs:
        # Sum totals
        total_sets += log.sets_completed
        total_reps += log.reps_completed
        
        if log.weight_kg:
            total_volume += log.sets_completed * log.reps_completed * log.weight_kg
        
        if log.duration_minutes:
            total_duration += log.duration_minutes
        
        # Most active day
        weekday_name = log.created_at.strftime('%A')
        weekday_counts[weekday_name] = weekday_counts.get(weekday_name, 0) + 1
        
        # Exercise type distribution
        if hasattr(log.exercise, 'exercise_type'):
            ex_type = log.exercise.exercise_type
            exercise_type_counts[ex_type] = exercise_type_counts.get(ex_type, 0) + 1
        
        # Top exercises
        exercise_name = log.exercise.name
        exercise_counts[exercise_name] = exercise_counts.get(exercise_name, 0) + 1
        exercise_sets[exercise_name] = exercise_sets.get(exercise_name, 0) + log.sets_completed
    
    # Averages
    average_sets_per_workout = total_sets / total_workouts if total_workouts > 0 else 0
    average_reps_per_set = total_reps / total_sets if total_sets > 0 else 0
    
    # Most active day
    most_active_day = max(weekday_counts, key=weekday_counts.get) if weekday_counts else 'No data'
    
    # Last 7 days data for chart
    today = timezone.now().date()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    
    chart_labels = []
    chart_data = []
    volume_data = []
    weekly_data = {
        'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 
        'Thursday': 0, 'Friday': 0, 'Weekend': 0
    }
    
    for day in last_7_days:
        day_logs = [log for log in user_logs if log.created_at.date() == day]
        day_count = len(day_logs)
        
        # Calculate day volume
        day_volume = 0
        for log in day_logs:
            if log.weight_kg:
                day_volume += log.sets_completed * log.reps_completed * log.weight_kg
        
        chart_labels.append(day.strftime('%a, %b %d'))
        chart_data.append(day_count)
        volume_data.append(day_volume)
        
        # Weekly data aggregation
        weekday_name = day.strftime('%A')
        if weekday_name in ['Saturday', 'Sunday']:
            weekly_data['Weekend'] += day_count
        else:
            weekly_data[weekday_name] += day_count
    
    # Exercise type distribution (prepare for chart)
    exercise_type_labels = []
    exercise_type_data = []
    exercise_type_mapping = {
        'strength': 'Strength Training',
        'cardio': 'Cardio',
        'flexibility': 'Flexibility',
        'balance': 'Balance',
        'hiit': 'HIIT',
    }
    
    for ex_type, count in sorted(exercise_type_counts.items(), key=lambda x: x[1], reverse=True):
        label = exercise_type_mapping.get(ex_type, ex_type.capitalize() if ex_type else 'Other')
        exercise_type_labels.append(label)
        exercise_type_data.append(count)
    
    # Top exercises
    top_exercises_list = []
    for name, count in sorted(exercise_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
        top_exercises_list.append({
            'name': name,
            'count': count,
            'total_sets': exercise_sets.get(name, 0),
            'percentage': 0
        })
    
    # Calculate percentages for top exercises
    if top_exercises_list:
        max_count = top_exercises_list[0]['count']
        for exercise in top_exercises_list:
            exercise['percentage'] = (exercise['count'] / max_count) * 100
    
    # Recent logs (already ordered)
    recent_logs = user_logs[:10]
    
    context = {
        'current_date': timezone.now(),
        'total_workouts': total_workouts,
        'total_exercises': total_exercises,
        'total_sets': total_sets,
        'total_reps': total_reps,
        'total_volume': int(total_volume),  # Convert to int for display
        'total_duration': total_duration,
        'average_sets_per_workout': round(average_sets_per_workout, 1),
        'average_reps_per_set': round(average_reps_per_set, 1),
        'most_active_day': most_active_day,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'volume_data': [int(v) for v in volume_data],  # Convert to int
        'weekly_data': weekly_data,
        'exercise_type_labels': exercise_type_labels,
        'exercise_type_data': exercise_type_data,
        'top_exercises': top_exercises_list,
        'recent_logs': recent_logs,
    }
    
    return render(request, 'dashboard.html', context)