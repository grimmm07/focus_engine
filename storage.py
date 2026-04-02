from time import perf_counter
from datetime import datetime
import csv

def save_data(real_start, start_time):
    stats = {}
    end_time = perf_counter()
    end_datetime = datetime.now()
    stats['start'] = real_start
    stats['end'] = end_datetime
    stats['duration'] = end_time - start_time
    with open('sessions.csv', mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([real_start, end_datetime, end_time - start_time])

    return stats