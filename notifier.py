
from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify( 
            title = "***Notify Me****",
            message = "This is a desktop notification",
            timeout = 5
    )

        time.sleep(60*60)

#pythonw file.py = to run the app in background.