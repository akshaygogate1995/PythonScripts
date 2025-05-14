# This script reads system uptime from the /proc/uptime file (Linux only)

def get_uptime():
    # Open and read the uptime file
    with open("/proc/uptime", "r") as file:
        uptime_seconds = float(file.readline().split()[0])  # First value is uptime in seconds

    # Convert uptime to hours, minutes, and seconds
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    seconds = int(uptime_seconds % 60)

    # Print nicely formatted uptime
    print(f"Uptime: {hours}h {minutes}m {seconds}s")

get_uptime()


# | Concept          | Usage                               |
# | ---------------- | ----------------------------------- |
# | `with open(...)` | Safely read a file                  |
# | `float()`        | Convert string to number            |
# | `split()`        | Break string by space               |
# | `//` and `%`     | Used for time conversion            |
# | `f""`            | Format strings cleanly and readably |
