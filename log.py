from datetime import datetime
import os


def log(info: str):
    """This function logs information about the program in folder 'logs'"""

    currentdate = datetime.now()

    if not os.path.exists('logs'):  # If there is no 'logs' folder it will be created
        os.mkdir("logs")

    with open(f"logs/log{currentdate.date()}.txt", "a") as file:
        file.write(f"{currentdate}| {info}\n")
