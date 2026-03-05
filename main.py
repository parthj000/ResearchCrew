import requests

url = "https://kmckmdckdmc.free.beeceptor.com"


def get_data(query: str) -> str:
    """Function to search the internet"""

    data = {"wow": "this is cool for me "}
    try:
        data = requests.post(url, json=data, timeout=800)
        if data.status_code == 200:
            return "We can't obtain the data sorry, give the message to user."
        else:
            return "Database returned error"
    except Exception as e:
        print(e)
        return "Something went wrong while running this tool."
