# Reads the last 10 lines of any log file (like /var/log/messages)

# Define a function to read the last 'n' lines from a log file
def tail_log(file_path, lines=10):
    # Open the file in read mode
    with open(file_path, "r") as f:
        # Read all lines from the file into a list
        all_lines = f.readlines()

        # Print the last 'lines' number of lines from the list
        for line in all_lines[-lines:]:
            # Strip removes leading/trailing whitespace (like newline characters)
            print(line.strip())

# Call the function with a sample log file path (replace with any log file you want)
tail_log("/var/log/messages")


# | Line                                 | Explanation                                                                                                                                  |
# | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
# | `def tail_log(file_path, lines=10):` | Defines a function `tail_log` that takes two arguments: `file_path` (the log file path) and `lines` (how many lines to show; default is 10). |
# | `with open(file_path, "r") as f:`    | Opens the file in read mode using a `with` block (auto-closes after use).                                                                    |
# | `all_lines = f.readlines()`          | Reads the entire file line by line into a **list** called `all_lines`.                                                                       |
# | `for line in all_lines[-lines:]:`    | Slices the list to get the **last `lines` number of entries**.                                                                               |
# | `print(line.strip())`                | Prints each line, removing any newline (`\n`) or extra spaces using `.strip()`.                                                              |
# | `tail_log("/var/log/messages")`      | Calls the function and gives it a real system log file as input. Replace this with any log file path you need to check.                      |
