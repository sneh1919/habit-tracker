import json
import sys

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

    # Each habit has a list of dates we completed it (we’ll add that later)
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


def help_message() -> None:
    print(
        """
Habit Tracker (Day 1)

Commands:
  python habit_tracker.py add "Habit Name"
  python habit_tracker.py list

Examples:
  python habit_tracker.py add "Study"
  python habit_tracker.py list
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
    else:
        help_message()


if __name__ == "__main__":
    main()
