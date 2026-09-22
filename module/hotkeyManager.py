from pynput import keyboard
from module.clipboard import RasaClipboard


class HotkeyManager:
    def __init__(self) -> None:
        super().__init__()
        self.clipboard = RasaClipboard()

        self._send_txt_to_clipboard()

    def _on_hotkey(self):
        # pynput's listener thread stops permanently if a callback raises,
        # which would silently disable the hotkey for the rest of the
        # session. Catch anything unexpected and keep listening instead.
        try:
            self.clipboard._get_windows_clipboard_content()
        except Exception as exc:
            print(f"Hotkey handler error: {exc}")

    def _send_txt_to_clipboard(self):
        hotkeyListener = keyboard.GlobalHotKeys({
            '<F10>': self._on_hotkey
        })
        hotkeyListener.start()
        hotkeyListener.join()
