import json
import sys
from datetime import date, datetime, timedelta

DATA_FILE = "habits.json"


def load_data() -> dict:
    """Load data from habits.json. If it doesn't exist, return an empty structure."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"habits": {}}
    except json.JSONDecodeError:
        print("Error: habits.json is corrupted (invalid JSON).")
        sys.exit(1)


def save_data(data: dict) -> None:
    """Save data back to habits.json."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_habit(name: str) -> None:
    data = load_data()
    habits = data["habits"]

    if name in habits:
        print(f"Habit '{name}' already exists.")
        return

    habits[name] = {"checkins": []}
    save_data(data)
    print(f"Added habit: {name}")


def list_habits() -> None:
    data = load_data()
    habits = data["habits"]

    if not habits:
        print("No habits yet. Add one with: python habit_tracker.py add \"Study\"")
        return

    print("Your habits:")
    for habit_name in habits.keys():
        print(f"- {habit_name}")


def mark_done(name: str, done_date: str | None = None) -> None:
    data = load_data()
    habits = data["habits"]

    if name not in habits:
        print(f"Habit '{name}' not found. Use: python habit_tracker.py list")
        return

    # If user didn't provide a date, use today's date
    if done_date is None:
        done_date = date.today().isoformat()  # YYYY-MM-DD

    # Validate date format
    try:
        datetime.fromisoformat(done_date)
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD (example: 2026-01-16).")
        return

    checkins = habits[name]["checkins"]

    if done_date in checkins:
        print(f"Already marked '{name}' done for {done_date}.")
        return

    checkins.append(done_date)
    checkins.sort()  # keep dates in order
    save_data(data)
    print(f"Marked '{name}' done for {done_date} ✅")


def show_streak(name: str) -> None:
    data = load_data()
    habits = data["habits"]

    if name not in habits:
        print(f"Habit '{name}' not found.")
        return

    checkins = habits[name]["checkins"]
    if not checkins:
        print(f"No check-ins yet for '{name}'. Current streak = 0")
        return

    # Convert saved strings "YYYY-MM-DD" into real date objects
    done_dates = set(datetime.fromisoformat(d).date() for d in checkins)

    today = date.today()
    streak = 0
    current_day = today

    # Count backwards: today, yesterday, day before...
    while current_day in done_dates:
        streak += 1
        current_day = current_day - timedelta(days=1)

    print(f"Current streak for '{name}' = {streak} day(s) 🔥")


def help_message() -> None:
    print(
        """
Habit Tracker

Commands:
  python habit_tracker.py add "Habit Name"
  python habit_tracker.py list
  python habit_tracker.py done "Habit Name" [YYYY-MM-DD]
  python habit_tracker.py streak "Habit Name"

Examples:
  python habit_tracker.py add "Study"
  python habit_tracker.py list
  python habit_tracker.py done "Study"
  python habit_tracker.py done "Study" 2026-01-16
  python habit_tracker.py streak "Study"
"""
    )


def main():
    if len(sys.argv) < 2:
        help_message()
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) >= 3:
        add_habit(sys.argv[2])

    elif command == "list":
        list_habits()

    elif command == "done" and len(sys.argv) >= 3:
        habit_name = sys.argv[2]
        done_date = sys.argv[3] if len(sys.argv) >= 4 else None
        mark_done(habit_name, done_date)

    elif command == "streak" and len(sys.argv) >= 3:
        show_streak(sys.argv[2])

    else:
        help_message()


if __name__ == "__main__":
    main()
