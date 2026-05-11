import asyncio
from translator_pkg.module_gtrans4 import TransLate, LangDetect

async def main():
    print(await TransLate("Добрий день", "uk", "en"))
    print(await LangDetect("Bonjour", "all"))

asyncio.run(main())
