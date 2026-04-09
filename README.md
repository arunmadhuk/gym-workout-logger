# Project 7: Gym Workout Logger

## Description
Users can log their workouts and track fitness progress over time.

## Objectives
- Implement activity tracking
- Store time-based records
- Generate analytics reports

## Functional Requirements

### Workout Tracking
- Create workout session
- Add exercises
- Record reps and weight

### Analytics
- Weekly progress
- Personal best tracking

## Database Tables
- users
- exercises
- workout_sessions
- exercise_logs

## Example API Endpoints

POST /workouts  
GET /workouts  
POST /workouts/{id}/exercise  
GET /workouts/history  

## Deployment Requirements
- PostgreSQL
- Dockerized API
- Cloud deployment
