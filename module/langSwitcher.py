class LangSwitcher:
    def __init__(self) -> None:
        super().__init__()

        self.english_to_farsi = {
            "H": "آ",
            "J": "ـ",
            "R": "تومان",
            "q": "ض",
            "w": "ص",
            "e": "ث",
            "r": "ق",
            "t": "ف",
            "y": "غ",
            "u": "ع",
            "i": "ه",
            "o": "خ",
            "p": "ح",
            "[": "ج",
            "]": "چ",
            "\\": "پ",
            "a": "ش",
            "s": "س",
            "d": "ی",
            "f": "ب",
            "g": "ل",
            "h": "ا",
            "j": "ت",
            "k": "ن",
            "l": "م",
            ";": "ک",
            "'": "گ",
            "z": "ظ",
            "x": "ط",
            "c": "ز",
            "v": "ر",
            "b": "ذ",
            "n": "د",
            "m": "ئ",
            ",": "و"

        }
        
        self.farsi_to_english = {v: k for k,
                                 v in self.english_to_farsi.items() if v != k}

    def detect_lang(self, text) -> dict | None:
        for ch in text:
            if ch in self.english_to_farsi:
                return self.english_to_farsi
            
            if ch in self.farsi_to_english:
                return self.farsi_to_english
            
        print("unknown")
        return None

    def convert_layout(self, text: str, mapping: dict) -> str:
        return ''.join(mapping.get(ch, ch) for ch in text)

    def auto_convert(self, text: str) -> str:
        mapping = self.detect_lang(text)
        if mapping is None:
            return text
        return self.convert_layout(text, mapping)
