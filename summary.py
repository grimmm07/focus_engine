import csv
from pathlib import Path

import matplotlib.pyplot as plt
from ui import section, info, warning, success, format_duration

def summary():
    duration = []
    data_by_date = {}
    skipped_rows = 0
    section("Session Summary")

    sessions_file = Path("sessions.csv")
    if not sessions_file.exists():
        warning("No sessions.csv file found yet. Start a few sessions first.")
        return

    with sessions_file.open(mode="r", newline="") as f:
        data = csv.reader(f)
        for row in data:
            if len(row) < 3:
                skipped_rows += 1
                continue
            try:
                seconds = float(row[2])
            except ValueError:
                skipped_rows += 1
                continue

            test = row[0].split(' ')
            if test[0] not in data_by_date:
                data_by_date[test[0]] = 0
            data_by_date[test[0]] += seconds
            duration.append(seconds)
    if len(duration) == 0:
        warning("There is no session data yet. Come back after tracking a few sessions.")
        return
    dates = list(data_by_date.keys())
    minutes = [seconds / 60 for seconds in data_by_date.values()]

    plt.style.use("seaborn-v0_8")
    plt.figure(figsize=(10, 5))
    plt.bar(dates, minutes, color='#4da3ff', edgecolor='#123b75')
    plt.title('Focus time by date')
    plt.xlabel('Date')
    plt.ylabel('Minutes')
    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()
    info(f"Tracked dates: {', '.join(dates)}")
    success(f"Sessions: {len(duration)}")
    if skipped_rows:
        warning(f"Skipped {skipped_rows} corrupted row(s) in sessions.csv.")
    print(f"Total focus time   : {format_duration(sum(duration))}")
    print(f"Average session    : {format_duration(sum(duration) / len(duration))}")
    print(f"Longest session    : {format_duration(max(duration))}")