
from time import perf_counter
from datetime import datetime

def save_data(real_start, start_time):
    stats = {}
    end_time = perf_counter()
    stats['start'] = real_start
    stats['end'] = datetime.now()
    stats['duration'] = end_time - start_time
    with open('sessions.csv', mode="a") as f:
        line = ",".join([str(real_start), str(datetime.now()), str(end_time - start_time)])
        f.write(line + '\n')

    return stats