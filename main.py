from time import sleep
from platform import system
from subprocess import run

SLEEP_MINUTES = 25
SLEEP_SECONDS = SLEEP_MINUTES * 60
HOST = system()
NOTIFY_TITLE = "Protect Your Eyes!"
NOTIFY_BODY = "Look at Something 20 feet away for 20 seconds"

while (True):
    sleep(5)
    if (HOST == "Linux"):
        run(['notify-send', NOTIFY_TITLE, NOTIFY_BODY])
    elif (HOST == "Darwing"):
        APPLE_NOTIFICATION = f"display notification {NOTIFY_BODY} with title {NOTIFY_TITLE}"
        run(['osascript', '-e', APPLE_NOTIFICATION])