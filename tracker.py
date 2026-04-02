import keyboard
from time import perf_counter, sleep
from datetime import datetime
from storage import save_data

last_time_activity = None
start_time = None
is_active = False
stop_flag = False
real_start = None
TIMEOUT_SECONDS = 5

def on_key_press(event):
    global last_time_activity, start_time, stop_flag, real_start, is_active
    if event.name == 'esc':
        stop_flag = True
        return
    if is_active == False:
        print("Started session")
        start_time = perf_counter()
        real_start = datetime.now()
        is_active = True

    last_time_activity = perf_counter()

def tracker():
    print("Tracker started")
    global is_active, start_time, last_time_activity, stop_flag, real_start
    sessions = []
    keyboard.on_press(on_key_press)
    while True:
        if stop_flag:
            if is_active:
                stats = save_data(real_start, start_time)
                sessions.append(stats)
            break
        if not is_active:
            sleep(0.5)
            continue
        if perf_counter() - last_time_activity  > TIMEOUT_SECONDS:
            print("session ended")
            stats = save_data(real_start, start_time)
            sessions.append(stats)
            is_active = False
            start_time = None
            last_time_activity = None
            real_start = None

        sleep(0.5)
    print(sessions)
    print("Tracking ended")