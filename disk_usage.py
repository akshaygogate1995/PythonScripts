# Import the shutil module which provides functions for disk and file operations
import shutil

# Define a function to check disk usage of a given path
def check_disk_usage(path="/"):
    # Get total, used, and free disk space for the given path
    total, used, free = shutil.disk_usage(path)

    # Calculate the percentage of used disk space
    percent_used = (used / total) * 100

    # Print disk usage with 2 decimal places
    print(f"Disk Usage: {percent_used:.2f}%")

    # If disk usage is above 80%, show a warning
    if percent_used > 80:
        print("⚠️ Warning: Disk usage is above 80%!")

# Call the function with the default path ("/" is root directory)
check_disk_usage()


# import shutil	Built-in Python module for disk and file handling
# shutil.disk_usage(path)	Returns total, used, and free bytes for the specified path
# /	Root directory (on Linux) — use "C:\\" on Windows if testing there
# percent_used	Simple math to calculate disk usage in percentage
# print(f"...")	f-strings are used for clean, formatted output
# if percent > 80:	Basic conditional to trigger warnings
