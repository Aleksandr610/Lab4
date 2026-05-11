import os
import json
from translator_pkg import module_deeptr

def read_config(config_file="config.json"):
    with open(config_file, "r", encoding="utf-8") as f:
        return json.load(f)

def read_text(file_name, sentences_limit):
    if not os.path.exists(file_name):
        raise FileNotFoundError("Файл не знайдено")
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]
    return text, ". ".join(sentences[:sentences_limit]), len(sentences)

def translate_text(text, lang):
    return module_deeptr.TransLate(text, "auto", lang)

def main():
    try:
        config = read_config()
        file_name = config["text_file"]
        lang = config["lang"]
        output = config["output"]
        sentences_limit = config["sentences"]

        full_text, limited_text, total_sentences = read_text(file_name, sentences_limit)
        file_size = os.path.getsize(file_name)
        char_count = len(full_text)
        file_lang = module_deeptr.LangDetect(full_text, "lang")

        print(f"Назва файлу: {file_name}")
        print(f"Розмір файлу: {file_size} байт")
        print(f"Кількість символів: {char_count}")
        print(f"Кількість речень: {total_sentences}")
        print(f"Мова тексту: {file_lang}")

        translated = translate_text(limited_text, lang)

        if output == "screen":
            print(f"\nМова перекладу: {lang}")
            print(f"Перекладений текст:\n{translated}")
        else:
            out_file = f"{file_name.split('.')[0]}_{lang}.txt"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(translated)
            print("Ok")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
