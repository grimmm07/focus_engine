from tracker import tracker
from summary import summary
print("1 - Start focus tracker ")
print("2 - to get a summary ")
print("3 - Exit")
data = ""
while data != '3':
    data = input ("Can you chose a number from the menu: ")
    if data == "1":
        tracker()
    if data == "2":
        summary()

