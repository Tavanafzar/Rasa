from pynput import keyboard
from module.clipboard import RasaClipboard


class HotkeyManager:
    def __init__(self) -> None:
        super().__init__()
        self.clipboard = RasaClipboard()

        try:
            self.hotkey_listener = keyboard.GlobalHotKeys({
                '<F10>': self._on_hotkey,

            })

            self.hotkey_listener.daemon = True
            self.hotkey_listener.start()
        except Exception as exc:
            print(f"something is wrong in module/hotkeyManager.py: {exc}")

    def _on_hotkey(self):
        try:

            self.clipboard._get_windows_clipboard_content()
        except Exception as exc:
            print(f"Hotkey handler error: {exc}")
