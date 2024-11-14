from time import sleep
from platform import system
from subprocess import run
import argparse

parser = argparse.ArgumentParser(prog="python3 main.py",
                                description="Eye Rest Notifier Script", 
                                epilog="Note: Time values default to seconds if no unit (s/m/h) is specified.")
parser.add_argument('--rest-time', type=str, default='20s', help='Specify the rest time (default: 20s)')
parser.add_argument('--sleep-time', type=str, default='30m', help='Specify the sleep time (default: 30m)')
args = parser.parse_args()

def parse_time_in_seconds(time):
    if (time[-1] == 's'):
        return int(time[:-1])
    elif (time[-1] == 'm'):
        return int(time[:-1]) * 60
    elif (time[-1] == 'h'):
        return int(time[:-1]) * 3600
    
    return int(time)

SLEEP_SECONDS = parse_time_in_seconds(args.sleep_time)
REST_SECONDS = parse_time_in_seconds(args.rest_time)

REST_NOTIFY_TITLE = "Protect Your Eyes!"
REST_NOTIFY_BODY = f"Look at Something 6 meters away for {REST_SECONDS} seconds"

WORK_NOTIFY_TITLE = "Eye Rest End"
WORK_NOTIFY_BODY = "Time to get Back to Work" 

HOST = system()
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