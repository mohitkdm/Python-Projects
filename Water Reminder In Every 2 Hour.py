import time
from win10toast import ToastNotifier

def display_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)

if __name__ == "__main__":
    notification_title = "Hello"
    notification_message = "This is a notification from your Health TO drink Water!"
    
    while True:
        display_notification(notification_title, notification_message)
        # Wait for 10 minutes (600 seconds) before displaying the next notification
        time.sleep(7200)
