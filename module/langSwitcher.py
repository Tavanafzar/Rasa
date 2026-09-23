from pathlib import Path
import json


class LangSwitcher:
    def __init__(self) -> None:
        super().__init__()
        self.langData = {}
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        langPack = BASE_DIR /"langpack" / "default.lg"
        
        with open(langPack, "r", encoding="utf-8") as pack:
            self.langData = json.load(pack)

        self.ReversedData = {v: k for k,
                             v in self.langData.items() if v != k}

    def detect_lang(self, text) -> dict | None:
        for ch in text:
            if ch in self.langData:
                return self.langData

            if ch in self.ReversedData:
                return self.ReversedData

        print("unknown")
        return None

    def convert_layout(self, text: str, mapping: dict) -> str:
        return ''.join(mapping.get(ch, ch) for ch in text)

    def auto_convert(self, text: str) -> str:
        mapping = self.detect_lang(text)
        if mapping is None:
            return text
        return self.convert_layout(text, mapping)
