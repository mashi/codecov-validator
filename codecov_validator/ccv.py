import requests


def run_request():
    with open("codecov.yml", "rb") as myconfig:
        file = myconfig.read()
    received = requests.post("https://codecov.io/validate", data=file)
    message = received.content.decode("utf-8")
    if "Valid!" not in message:
        print(message)
        exit(1)


if __name__ == "__main__":
    run_request()
