from sendmail import sendmail
from log import log


def main():
    log(sendmail())
    print("End of mailing")


if __name__ == "__main__":
    main()
