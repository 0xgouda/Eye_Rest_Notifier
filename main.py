from time import sleep
from platform import system
from subprocess import run

SLEEP_MINUTES = 30
SLEEP_SECONDS = SLEEP_MINUTES * 60
REST_SECONDS = 20
HOST = system()

REST_NOTIFY_TITLE = "Protect Your Eyes!"
REST_NOTIFY_BODY = f"Look at Something 6 meters away for {REST_SECONDS} seconds"

WORK_NOTIFY_TITLE = "Eye Rest End"
WORK_NOTIFY_BODY = "Time to get Back Work" 

while (True):
    sleep(SLEEP_SECONDS)
    
    if (HOST == "Linux"):
        run(['notify-send', REST_NOTIFY_TITLE, REST_NOTIFY_BODY])
    elif (HOST == "Darwing"):
        APPLE_NOTIFICATION = f"display notification {REST_NOTIFY_BODY} with title {REST_NOTIFY_TITLE}"
        run(['osascript', '-e', APPLE_NOTIFICATION])
    
    sleep(REST_SECONDS)

    if (HOST == "Linux"):
        run(['notify-send', WORK_NOTIFY_TITLE, WORK_NOTIFY_BODY])
    elif (HOST == "Darwing"):
        APPLE_NOTIFICATION = f"display notification {WORK_NOTIFY_BODY} with title {WORK_NOTIFY_TITLE}"
        run(['osascript', '-e', APPLE_NOTIFICATION])