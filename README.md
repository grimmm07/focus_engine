# Focus Engine

Focus Engine is a small Python CLI app for tracking focused work sessions and reviewing the time you spent in each session.

It has two main modes:

- Start a focus tracker that listens for keyboard activity.
- Generate a summary chart and session statistics from saved data.

## Features

- Tracks the start and end time of a focus session.
- Automatically ends a session after 5 seconds of inactivity.
- Press `Esc` to stop tracking manually.
- Saves every session to `sessions.csv`.
- Shows a bar chart of focus time grouped by date.

## Project Structure

- `main.py` - simple menu that lets you start the tracker or open the summary.
- `tracker.py` - listens for keyboard input and ends sessions on inactivity or `Esc`.
- `storage.py` - saves session data to `sessions.csv`.
- `summary.py` - reads `sessions.csv`, prints stats, and displays a chart.
- `sessions.csv` - generated session history.

## Requirements

- Python 3.13 or later.
- The following Python packages:
  - `keyboard`
  - `matplotlib`

## Setup

If you are using the included virtual environment on Windows, activate it first:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install keyboard matplotlib
```

## Run

Start the app with:

```powershell
python main.py
```


## How To Use

When the menu appears:

1. Enter `1` to start tracking.
2. Type normally to keep the session active.
3. Stop typing for 5 seconds to end the session automatically.
4. Press `Esc` to stop the tracker immediately.
5. Enter `2` to open the summary view.
6. Enter `3` to exit the app.

## Session Data

Each completed session is appended to `sessions.csv` in this format:

```text
start_datetime,end_datetime,duration_in_seconds
```

Example:

```text
2026-03-01 09:10:00,2026-03-01 09:35:00,1500
```

The summary view groups sessions by the date in the `start_datetime` column, converts total seconds to minutes, and shows a bar chart.

## Notes

- `sessions.csv` is generated automatically.
- If `sessions.csv` is empty or missing, the summary view will not have data to show.
- On Windows, the `keyboard` package may require running the terminal with the permissions needed to listen for global key events.

## Example Output

The summary command prints:

- the list of tracked dates,
- the number of sessions,
- total focus time,
- average session length,
- longest session length.
