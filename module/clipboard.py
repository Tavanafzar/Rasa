
import time
import pyperclip
from module.langSwitcher import LangSwitcher
from pynput.keyboard import Key, Controller

# Delay (seconds) given to Windows to actually update the clipboard after a
# simulated Ctrl+C / Ctrl+V. Without this, pyperclip.paste() often reads the
# *previous* clipboard content because the copy hasn't landed yet.
CLIPBOARD_SYNC_DELAY = 0.15


class RasaClipboard:
    def __init__(self) -> None:
        super().__init__()
        self.switcher = LangSwitcher()

    def _get_windows_clipboard_content(self):
        try:
            previous_clipboard = pyperclip.paste()
        except pyperclip.PyperclipException:
            previous_clipboard = None

        self._display_final_result(Key.ctrl, 'c')
        time.sleep(CLIPBOARD_SYNC_DELAY)

        try:
            content = pyperclip.paste()
        except pyperclip.PyperclipException as exc:
            print(f"Could not read clipboard: {exc}")
            return

        # Nothing was actually selected/copied (clipboard unchanged) -
        # bail out instead of converting stale/unrelated text.
        if previous_clipboard is not None and content == previous_clipboard:
            print("No new text was copied; nothing to convert.")
            return

        finalResult = self.switcher.auto_convert(content)
        print(finalResult)

        try:
            pyperclip.copy(finalResult)
        except pyperclip.PyperclipException as exc:
            print(f"Could not write clipboard: {exc}")
            return
        time.sleep(CLIPBOARD_SYNC_DELAY)

        self._display_final_result(Key.ctrl, 'v')
        time.sleep(CLIPBOARD_SYNC_DELAY)
        self._display_final_result(Key.cmd, Key.space)

        # Restore whatever the user had on their clipboard before the
        # hotkey was pressed, so it isn't silently lost.
        if previous_clipboard is not None:
            time.sleep(CLIPBOARD_SYNC_DELAY)
            try:
                pyperclip.copy(previous_clipboard)
            except pyperclip.PyperclipException:
                pass

    def _display_final_result(self, *keys):
        keyboard = Controller()

        for key in keys:
            keyboard.press(key)

        for key in reversed(keys):
            keyboard.release(key)
