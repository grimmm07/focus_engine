import csv
import matplotlib.pyplot as plt

def summary():
    duration = []
    data_by_date = {}
    with open('sessions.csv', mode="r") as f:
        data = csv.reader(f)
        for row in data:
            test = row[0].split(' ')
            if test[0] not in data_by_date:
                data_by_date[test[0]] = 0
            data_by_date[test[0]] += float(row[2])
            duration.append(float(row[2]))
    if len(duration) == 0:
        print("there is no data for now come later")
        return
    dates = list(data_by_date.keys())
    minutes = [seconds / 60 for seconds in data_by_date.values()]

    plt.bar(dates, minutes, color='skyblue', edgecolor='navy')
    plt.xticks(rotation=45) 
    plt.show()
    print(dates)
    print(f"Sessions: {len(duration)}")
    print(f"{'Total focus time ':<20} : {int(sum(duration) // 60)} min {int (sum(duration) % 60)} sec")
    print(f"{'Average session ':<20} : {int((sum(duration) // len(duration)) // 60)} min {int ((sum(duration) // len(duration)) % 60)} sec")
    print(f"{'Longest session ':<20} : {int(max(duration) // 60)} min {int (max(duration) % 60)} sec")