from module.hotkeyManager import HotkeyManager
from module.notification import NotificationManager
from theme.themeLoader import ThemeLoader

from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from pathlib import Path
import sys


def main():
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

    notification = NotificationManager()
    notification.program_running()

    # رفرنس رو روی app نگه می‌داریم تا GC نشه
    app.hotkey_manager = HotkeyManager()  # type: ignore

    if not QSystemTrayIcon.isSystemTrayAvailable():
        print("سیستم تری در دسترس نیست!")

    icon_path = Path(__file__).parent / "assets" / "rasa.ico"
    tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), app)
    tray_icon.setToolTip("Rasa")

    tray_menu = QMenu()

    hint_action = tray_menu.addAction("کلید میانبر :")
    hint_action.setShortcut("F10")

    exit_action = tray_menu.addAction("خروج")
    exit_action.triggered.connect(app.quit)

    theme_loader = ThemeLoader()
    stylesheet = theme_loader.apply_theme()

    tray_menu.setStyleSheet(stylesheet)

    tray_icon.setContextMenu(tray_menu)
    tray_icon.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
