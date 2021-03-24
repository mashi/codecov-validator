import click
import requests as rq


@click.command()
@click.option(
    "--filename", default="codecov.yml", help="Codecov configuration file."
)
def ccv(filename):
    file = open_file(filename)
    if file:
        result = run_request(file)
        flag = check_valid(result)
        if flag:
            print(result)
            exit()
        exit(flag)
    else:
        exit(1)


def check_valid(result):
    """
    Check if the message contains the "Valid!" string
    from the request call.

    Args:
        result (str): message to be analyzed.

    Returns:
        int: The output is 1 to indicate an error so
        exit(1) is called and indicates error in the pre-commit.
        Returns 0 when "Valid!" is presented.
    """
    if "Valid!" in result:
        print("Valid!")
        flag = 0
    else:
        print(result)
        flag = 1
    return flag


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
        return "0"


def run_request(file):
    """
    Send the configuration to the codecov site.

    Args:
        file (string): contents of the configuration file.

    Returns:
        str: Result of the request.
    """
    try:
        received = rq.post("https://codecov.io/validate", data=file)
    except (
        rq.ConnectTimeout,
        rq.HTTPError,
        rq.ReadTimeout,
        rq.Timeout,
        rq.ConnectionError,
    ):
        print("Failed to establish connection. Check your internet.")
        exit(1)
    message = received.content.decode("utf-8")
    return message


if __name__ == "__main__":
    ccv()
