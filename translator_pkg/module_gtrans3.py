import sys
from googletrans import Translator, LANGUAGES

# Перевірка версії Python
def check_version():
    if sys.version_info.major == 3 and sys.version_info.minor >= 13:
        raise RuntimeError("Помилка: модуль gtrans3 працює тільки з Python 3.11–3.12")

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    """Переклад тексту з мови scr на мову dest"""
    try:
        check_version()
        return translator.translate(text, src=scr, dest=dest).text
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначення мови тексту та коефіцієнта довіри"""
    try:
        check_version()
        result = translator.detect(text)
        lang = result.lang
        conf = result.confidence
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
        check_version()
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
        check_version()
        rows = []
        for code, name in LANGUAGES.items():
            if text:
                translated = translator.translate(text, src="auto", dest=code).text
                rows.append(f"{code:<5} {name:<20} {translated}")
            else:
                rows.append(f"{code:<5} {name:<20}")
        if out == "screen":
            print("Код   Мова                 Переклад")
            print("\n".join(rows))
        else:
            with open("languages_gtrans3.txt", "w", encoding="utf-8") as f:
                f.write("Код   Мова                 Переклад\n")
                f.write("\n".join(rows))
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
