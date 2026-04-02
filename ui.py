from datetime import datetime, timedelta

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
UNDERLINE = "\033[4m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"


def color_text(text, color=""):
    return f"{color}{text}{RESET}" if color else str(text)


def section(title):
    print()
    print(color_text("=" * 52, BRIGHT_BLUE))
    print(color_text(title, BOLD + BRIGHT_CYAN))
    print(color_text("=" * 52, BRIGHT_BLUE))


def subtitle(text):
    print(color_text(text, BRIGHT_BLACK))


def success(text):
    print(color_text(text, BRIGHT_GREEN))


def info(text):
    print(color_text(text, BRIGHT_CYAN))


def warning(text):
    print(color_text(text, BRIGHT_YELLOW))


def error(text):
    print(color_text(text, BRIGHT_RED))


def format_duration(seconds):
    seconds = int(seconds)
    minutes, remaining_seconds = divmod(seconds, 60)
    return f"{minutes} min {remaining_seconds} sec"


def format_timestamp(value):
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return str(value)


def menu_header():
    print()
    print(color_text("FOCUS ENGINE", BOLD + BRIGHT_MAGENTA))
    print(color_text("Track focus sessions and review your history.", BRIGHT_BLACK))
    print()
    print(color_text("  1)", BRIGHT_GREEN), "Start focus tracker")
    print(color_text("  2)", BRIGHT_CYAN), "View summary")
    print(color_text("  3)", BRIGHT_RED), "Exit")


def prompt(text):
    return color_text(text, BRIGHT_YELLOW)
