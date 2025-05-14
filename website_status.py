# Import the requests module to make HTTP requests
import requests

# Define a function that checks if a given website is up
def check_website(url):
    try:
        # Send a GET request to the specified URL with a timeout of 5 seconds
        response = requests.get(url, timeout=5)

        # If the response status code is 200 (OK), the site is reachable
        if response.status_code == 200:
            print(f"{url} is UP ✅")
        else:
            # If not 200, print the actual HTTP status code returned
            print(f"{url} returned status {response.status_code}")

    # Catch any exceptions that may occur (e.g., connection error, timeout)
    except requests.RequestException as e:
        print(f"{url} is DOWN ❌\nError: {e}")

# Call the function with a sample website (you can replace this with any URL)
check_website("https://www.github.com")


# | Concept              | Explanation                                                         |
# | -------------------- | ------------------------------------------------------------------- |
# | `requests.get()`     | Sends an HTTP GET request to a URL                                  |
# | `timeout=5`          | If the site doesn’t respond in 5 seconds, it triggers an error      |
# | `status_code == 200` | `200` means "OK" — the website is reachable and working             |
# | `try-except`         | Used to **gracefully handle errors**, like timeouts or invalid URLs |
# | `RequestException`   | A base exception that catches **all request-related errors**        |
# | `f"{url} is UP"`     | Uses **f-strings** to include the URL in the output                 |
