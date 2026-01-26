# Habit Tracker (Python CLI)

A simple command-line habit tracker that saves habits and check-ins in a local JSON file (`habits.json`).  
You can add habits, mark them as done, view your streak, and see completion stats.

## Features
- Add and list habits
- Mark a habit as done (today or a specific date)
- Prevent duplicate check-ins for the same day
- Show current streak
- Show completion stats for the last N days

## How to Run (Windows)

Clone the repo and go into the folder:
```bash
git clone https://github.com/sneh1919/habit-tracker.git
cd habit-tracker

## Run commands using Python launcher (py):
py habit_tracker.py list

## Commands

## Add a habit:
py habit_tracker.py add "Study"


## List habits:
py habit_tracker.py list


## Mark done (today):
py habit_tracker.py done "Study"


## Mark done (specific date):
py habit_tracker.py done "Study" 2026-01-16


## Show streak:
py habit_tracker.py streak "Study"


## Show stats (last 7 days by default):
py habit_tracker.py stats "Study"


## Show stats (last N days)
py habit_tracker.py stats "Study" 30

## Example Output
Marked 'Study' done for 2026-01-16 ✅
Current streak for 'Study' = 1 day(s) 🔥
Last 7 days for 'Study': 1/7 (14%) ✅