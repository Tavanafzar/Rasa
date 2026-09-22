from winotify import Notification
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ICON_PATH = BASE_DIR / "assets" / "rasa.ico"


class NotificationManager:

    def __init__(self):
        pass

    def program_running(self):
        toast = Notification(

            app_id="رسا",
            title="رسا اجرا شد",
            msg="رسا آماده به کار است.",
            icon=str(ICON_PATH)
        )

        toast.show()
