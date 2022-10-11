from datetime import datetime
import openpyxl
from log import log


def transformdate(date):
    """This function converts the date to DD.MM format
    for easy date comparison

    :return: 'DD.MM'
    """

    year, month, day = str(date).split("-")
    return f"{day}.{month}"


def checkdb():
    """This function reads data from an excel spreadsheet and adds names and email
     addresses of people who have a birthday to the sendlist for further congratulation

     :return: sendlist = [[name1, email1], [name2, email2], [name3, email3], ...]
     """

    try:
        book = openpyxl.open("db.xlsx", read_only=True)  # Opening your db
        sheet = book.active
        sendlist = list()
        current_date = datetime.now().date()

        for row in range(2, sheet.max_row + 1):
            id = sheet[row][0].value
            name = sheet[row][1].value
            email = sheet[row][2].value
            birthdate = sheet[row][3].value

            try:
                if None not in [name, email, birthdate]:  # Checking for empty table cells
                    if transformdate(current_date) == transformdate(birthdate.date()):
                        sendlist.append([name, email])
            except Exception:
                log(f"Error occurred adding id:{id} name:{name} email:{email} to sendlist - {Exception}")

        return sendlist

    except Exception:
        log(f"An error occurred while reading the database\n{Exception}")
        return []
