# Import the subprocess module to run system-level commands
import subprocess

# Define the name of the service you want to check
service = "nginx"

# Define a function that checks if the service is running
def is_service_running(service):
    try:
        # Run the command: systemctl is-active <service>
        # This checks the current status of the service
        output = subprocess.check_output(
            ["systemctl", "is-active", service],  # Command broken into parts
            universal_newlines=True  # Converts output from bytes to string
        ).strip()  # Remove leading/trailing whitespace/newlines

        # Return True if the output is exactly "active"
        return output == "active"

    except subprocess.CalledProcessError:
        # If the command fails (e.g., service not found), return False
        return False

# Call the function and print result based on the outcome
if is_service_running(service):
    # If the service is active, print a success message
    print(f"{service} is running.")
else:
    # If the service is not active or an error occurred, print this
    print(f"{service} is NOT running.")


# import brings in a built-in Python module.

# def is how you define a reusable function.

# try-except is how you handle errors safely.

# subprocess.check_output() runs system commands.

# f"{variable}" inside strings is called an f-string, used for formatting.

# strip() removes whitespace from both ends of the string.
