# This script lists all running processes using the psutil module

# Import the psutil module which provides an interface for retrieving information on running processes
import psutil

# Define a function to list processes
def list_processes():
    # Iterate over all running processes
    # 'psutil.process_iter' returns an iterator over Process objects
    # We only ask for 3 specific attributes for efficiency: pid, name, and username
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        # Each 'proc' is a Process object, and 'proc.info' is a dictionary with the requested info
        # Print process ID, process name, and the username that started the process
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")

# Call the function to run the process listing
list_processes()


# | Line                       | Description                                                                                                                                           |
# | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
# | `import psutil`            | Imports the **psutil** library, which allows you to fetch info about running processes, CPU, memory, etc.                                             |
# | `def list_processes():`    | Defines a function named `list_processes`.                                                                                                            |
# | `psutil.process_iter(...)` | Returns an iterator over all running processes. The list `['pid', 'name', 'username']` tells psutil to **only fetch these 3 fields** for performance. |
# | `for proc in ...`          | Loops over each running process.                                                                                                                      |
# | `proc.info[...]`           | Accesses the values of process attributes like process ID, name, and the user who started it.                                                         |
# | `print(...)`               | Nicely prints the info using an **f-string**.                                                                                                         |
# | `list_processes()`         | Calls the function to execute it.                                                                                                                     |
