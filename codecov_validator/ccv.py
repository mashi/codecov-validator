import click
import requests


@click.command()
@click.option(
    "--filename", default="codecov.yml", help="Codecov configuration file."
)
def ccv(filename):
    file = open_file(filename)
    result = run_request(file)
    check_valid(result)


def check_valid(result):
    """
    Check if the message contains the "Valid!" string
    from the request call.
    The exit(1) is used to indicate an error in the pre-commit.

    Args:
        result (str): message to be analyzed.
    """
    if "Valid!" in result:
        print("Valid!")
        exit(0)
    else:
        print(result)
        exit(1)


def open_file(filename):
    """
    Tries to open the configuration file.

    Args:
        filename (str): name of the configuration file.

    Returns:
        bytes: contents of the configuration file, or
            the string zero.
    """
    try:
        with open(filename, "rb") as myconfig:
            file = myconfig.read()
        return file
    except FileNotFoundError:
        print("Configuration file not found.")
        exit(1)


def run_request(file):
    """
    Send the configuration to the codecov site.

    Args:
        file (string): contents of the configuration file.

    Returns:
        str: Result of the request.
    """
    try:
        received = requests.post("https://codecov.io/validate", data=file)
    except (
        requests.exceptions.ConnectTimeout,
        requests.exceptions.HTTPError,
        requests.exceptions.ReadTimeout,
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
    ):
        print("Failed to establish connection. Check your internet.")
        exit(1)
    message = received.content.decode("utf-8")
    return message


if __name__ == "__main__":
    ccv()
