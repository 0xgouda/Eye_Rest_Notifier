# Eye Rest Notifier
- A simple Python script that helps you take periodic breaks from your screen to protect your eyes. It notifies you when it's time to rest your eyes and when it's time to get back to work.
- Cross-platform: Works on Windows, macOS, and Linux.

# Requirements
- Python 3.x
- plyer (for cross-platform notifications)
```bash
pip install plyer
```
# Usage
```bash
python3 notifier.py -h
usage: python3 notifier.py [-h] [--rest-time REST_TIME] [--work-time WORK_TIME]

Eye Rest Notifier Script

options:
  -h, --help            show this help message and exit
  --rest-time REST_TIME
                        Specify the rest time (default: 20s)
  --work-time WORK_TIME
                        Specify the work time (default: 30m)

Note: Time values default to seconds if no unit (s/m/h) is specified.
```

```bash
python3 notifier.py --work-time 45m --rest-time 3s
```

- set the timers to what fits you and make the command a startup application :)
