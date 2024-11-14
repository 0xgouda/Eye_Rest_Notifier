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
WORK_NOTIFY_BODY = "Time to get Back to Work" 

def command(Title, Body):
    if (HOST == "Linux"):
        return ['notify-send', Title, Body]
    elif (HOST == "Darwin"):
        return ['osascript', '-e', f"display notification {Body} with title {Title}"]


while (True):
    sleep(SLEEP_SECONDS)
    run(command(REST_NOTIFY_TITLE, REST_NOTIFY_BODY))
    
    sleep(REST_SECONDS)
    run(command(WORK_NOTIFY_TITLE, WORK_NOTIFY_BODY))