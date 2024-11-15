from time import sleep
from plyer import notification
import argparse

def parse_cli_args():
    parser = argparse.ArgumentParser(prog="python3 main.py",
                                    description="Eye Rest Notifier Script", 
                                    epilog="Note: Time values default to seconds if no unit (s/m/h) is specified.")
    parser.add_argument('--rest-time', type=str, default='20s', help='Specify the rest time (default: 20s)')
    parser.add_argument('--work-time', type=str, default='30m', help='Specify the work time (default: 30m)')
    args = parser.parse_args()

    return args

def parse_time_in_seconds(time):
    if (time[-1] == 's'):
        return int(time[:-1])
    elif (time[-1] == 'm'):
        return int(time[:-1]) * 60
    elif (time[-1] == 'h'):
        return int(time[:-1]) * 3600
    
    return int(time)

def main():
    args = parse_cli_args()

    WORK_SECONDS = parse_time_in_seconds(args.work_time)
    REST_SECONDS = parse_time_in_seconds(args.rest_time)

    REST_NOTIFY_TITLE = "Protect Your Eyes!"
    REST_NOTIFY_BODY = f"Look at Something 6 meters away for {REST_SECONDS} seconds"

    WORK_NOTIFY_TITLE = "Eye Rest End"
    WORK_NOTIFY_BODY = "Time to get Back to Work" 

    while (True):
        sleep(WORK_SECONDS)
        notification.notify(title=REST_NOTIFY_TITLE, message=REST_NOTIFY_BODY)
        
        sleep(REST_SECONDS)
        notification.notify(title=WORK_NOTIFY_TITLE, message=WORK_NOTIFY_BODY)

if (__name__ == '__main__'):
    main()