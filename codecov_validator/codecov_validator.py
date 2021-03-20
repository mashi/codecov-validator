import requests


file = open("codecov.yml", "rb").read()
received = requests.post("https://codecov.io/validate", data=file)
message = received.content.decode("utf-8")
if "Valid!" not in message:
    print(message)
    exit(1)
