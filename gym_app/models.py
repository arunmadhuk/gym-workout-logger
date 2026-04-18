from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime, timedelta

class UserManager(BaseUserManager):
    def create_user(self, email, password, full_name=None, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("The password must be set")
        email = self.normalize_email(email)
        print(f"User creation request received - email {email}, fullname- {full_name}, extra_fields -{extra_fields}")
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        print(f"user {user} created succesfully")
        return user

    def create_superuser(self, email, password,full_name=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        print(f"Superuser create request received for {email} , {full_name}")
        return self.create_user(email, password,full_name or 'Admin' **extra_fields)

    
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email


class WorkoutSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_duration(self):
        """Calculate duration in minutes from start_time and end_time"""
        if self.start_time and self.end_time:
            start_datetime = datetime.combine(self.session_date, self.start_time)
            end_datetime = datetime.combine(self.session_date, self.end_time)
            
            # Handle overnight sessions
            if end_datetime < start_datetime:
                end_datetime += timedelta(days=1)
            
            duration = (end_datetime - start_datetime).total_seconds() / 60
            return int(round(duration))
        return None
    
    def save(self, *args, **kwargs):
        """Auto-calculate duration before saving"""
        if self.start_time and self.end_time:
            self.duration_minutes = self.calculate_duration()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.full_name} - {self.session_date}"
    

class Exercise(models.Model):
    EXERCISE_TYPE_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
    ]
    EQUIPMENT_CHOICES = [
        ('none', 'None'),
        ('dumbbells', 'Dumbbells'),
        ('barbell', 'Barbell'),
        ('kettlebell', 'Kettlebell'),
        ('resistance_bands', 'Resistance Bands'),
        ('machine', 'Machine'),
    ]
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_TYPE_CHOICES)
    equipment = models.CharField(max_length=20, choices=EQUIPMENT_CHOICES, null=True, blank=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight_kg = models.FloatField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.exercise_type}"
    

class ExerciseLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    sets_completed = models.PositiveIntegerField()
    reps_completed = models.PositiveIntegerField()
    weight_kg = models.FloatField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.workout_session} - {self.exercise.name}"

