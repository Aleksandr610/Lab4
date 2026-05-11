from deep_translator import GoogleTranslator
from langdetect import detect_langs


LANGUAGES = {
    "uk": "Ukrainian",
    "en": "English",
    "de": "German",
    "fr": "French",
    "es": "Spanish"
}

def TransLate(text: str, scr: str, dest: str) -> str:
    """Переклад тексту з мови scr на мову dest"""
    try:
        return GoogleTranslator(source=scr, target=dest).translate(text)
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначення мови тексту та коефіцієнта довіри"""
    try:
        langs = detect_langs(text)[0]
        lang = langs.lang
        conf = langs.prob
        if set == "lang":
            return lang
        elif set == "confidence":
            return str(conf)
        else:
            return f"{lang}, {conf}"
    except Exception as e:
        return f"Помилка: {e}"

def CodeLang(lang: str) -> str:
    """Перетворення коду ↔ назви мови"""
    try:
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        elif lang.lower() in [name.lower() for name in LANGUAGES.values()]:
            for code, name in LANGUAGES.items():
                if name.lower() == lang.lower():
                    return code
        return "Помилка: невідома мова"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Вивід списку мов з перекладом (на екран або у файл)"""
    try:
        rows = []
        for code, name in LANGUAGES.items():
            if text:
                translated = TransLate(text, "auto", code)
                rows.append(f"{code:<5} {name:<15} {translated}")
            else:
                rows.append(f"{code:<5} {name:<15}")
        if out == "screen":
            print("Код   Мова           Переклад")
            print("\n".join(rows))
        else:
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write("Код   Мова           Переклад\n")
                f.write("\n".join(rows))
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
