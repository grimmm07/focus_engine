from tracker import tracker
from summary import summary
from ui import menu_header, prompt, section, info, warning, error

section("Focus Engine")
menu_header()
data = ""
while data != '3':
    data = input(prompt("Choose an option from the menu: "))
    if data == "1":
        tracker()
    if data == "2":
        summary()
    if data not in {"1", "2", "3", ""}:
        warning("Please choose 1, 2, or 3.")

