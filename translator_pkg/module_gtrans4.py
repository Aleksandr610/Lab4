import asyncio
from googletrans import Translator, LANGUAGES

translator = Translator()

async def TransLate(text: str, scr: str, dest: str) -> str:
    """Асинхронний переклад тексту з мови scr на мову dest"""
    try:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, translator.translate, text, scr, dest)
        return result.text
    except Exception as e:
        return f"Помилка: {e}"

async def LangDetect(text: str, set: str = "all") -> str:
    """Асинхронне визначення мови тексту та коефіцієнта довіри"""
    try:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, translator.detect, text)
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

async def CodeLang(lang: str) -> str:
    """Асинхронне перетворення коду ↔ назви мови"""
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

async def LanguageList(out: str = "screen", text: str = None) -> str:
    """Асинхронний вивід списку мов з перекладом (на екран або у файл)"""
    try:
        rows = []
        for code, name in LANGUAGES.items():
            if text:
                loop = asyncio.get_event_loop()
                result = await loop.run_in_executor(None, translator.translate, text, "auto", code)
                translated = result.text
                rows.append(f"{code:<5} {name:<20} {translated}")
            else:
                rows.append(f"{code:<5} {name:<20}")
        if out == "screen":
            print("Код   Мова                 Переклад")
            print("\n".join(rows))
        else:
            with open("languages_gtrans4.txt", "w", encoding="utf-8") as f:
                f.write("Код   Мова                 Переклад\n")
                f.write("\n".join(rows))
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
