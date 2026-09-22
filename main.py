from module.hotkeyManager import HotkeyManager
from module.notification import NotificationManager


def main():
    notification = NotificationManager()
    notification.program_running()
    
    hotkey_manager = HotkeyManager()

if __name__ == "__main__":
    main()