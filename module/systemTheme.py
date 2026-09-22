"""خواندن تم روشن/تیره‌ی سیستم‌عامل و آیکون متناظر برنامه."""
import winreg
from pathlib import Path


class ThemeManager:
    """تعیین تم فعلی ویندوز و آیکون مناسب برای نمایش در پنجره/تری."""
    @staticmethod
    def get_system_theme() -> bool:
        """تم سیستم‌عامل ویندوز را از رجیستری می‌خواند: True برای تیره، False برای روشن."""
        try:
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
            ) as key:
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        
            return value == 0
        except (FileNotFoundError, OSError):
            return False

     