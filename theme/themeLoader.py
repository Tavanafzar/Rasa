from module.systemTheme import ThemeManager


DARK_COLORS = {
    "bg_start": "#18181B",
    "bg_stop": "#000000",
    "text_color": "#F2F2F2",
}

LIGHT_COLORS = {
    "bg_start": "#ECEEF2",
    "bg_stop": "#D1D3E0",
    "text_color": "#242425",
}


class ThemeLoader:

    @staticmethod
    def _gradient(start: str, stop: str, dark: bool) -> str:
        if dark:
            return (
                "qlineargradient("
                "spread:pad, "
                "x1:0, y1:0, "
                "x2:1, y2:1, "
                f"stop:0 {start}, "
                f"stop:1 {stop}"
                ")"
            )

        return (
            "qlineargradient("
            "spread:pad, "
            "x1:0.716, y1:0.000636364, "
            "x2:0.516818, y2:1, "
            f"stop:0 {start}, "
            f"stop:1 {stop}"
            ")"
        )

    def apply_theme(self):
        dark = ThemeManager.get_system_theme()

        if dark:
            return self.dark_theme()

        return self.light_theme()

    def dark_theme(self):
        c = DARK_COLORS
        gradient = self._gradient(
            c["bg_start"],
            c["bg_stop"],
            dark=True
        )

        return f"""
            QMenu {{
                background: {gradient};
                color: {c["text_color"]};
                min-width: 120px;
                min-height: 60px;
                font-size: 10pt;
                border-radius: 10px;
                padding: 10px;
            }}
        """

    def light_theme(self):
        c = LIGHT_COLORS
        gradient = self._gradient(
            c["bg_start"],
            c["bg_stop"],
            dark=False
        )

        return f"""
            QMenu {{
                background: {gradient};
                color: {c["text_color"]};
                min-width: 120px;
                min-height: 60px;
                font-size: 10pt;
                border-radius: 10px;
                padding: 10px;
            }}
        """