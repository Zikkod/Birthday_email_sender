from log import log

def getmessagetemplate():
    """This function reads and returns your letter template"""

    try:
        with open('message.html', 'r', encoding='utf-8') as msg:
            message = msg.read()
            return message
    except Exception:
        return "Error:Couldn't get a message template"