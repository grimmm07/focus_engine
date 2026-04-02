import csv

def summary():
    duration = []
    with open('sessions.csv', mode="r") as f:
        data = csv.reader(f)
        for row in data:
            duration.append(float(row[2]))
    if len(duration) == 0:
        print("there is no data for now come later")
        return
    print(f"Sessions: {len(duration)}")
    print(f"{'Total focus time ':<20} : {int(sum(duration) // 60)} min {int (sum(duration) % 60)} sec")
    print(f"{'Average session ':<20} : {int((sum(duration) // len(duration)) // 60)} min {int ((sum(duration) // len(duration)) % 60)} sec")
    print(f"{'Longest session ':<20} : {int(max(duration) // 60)} min {int (max(duration) % 60)} sec")