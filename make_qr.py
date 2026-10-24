"""Рисует QR-коды: ссылка на онлайн-резюме и контакт (vCard, без телефона). Нужен пакет segno."""
import pathlib
import segno

OUT = pathlib.Path(__file__).parent / "qr"
URL = "https://victor-dev-coder.github.io/cv/"
VCARD = "\n".join([
    "BEGIN:VCARD", "VERSION:3.0", "N:Croitoru;Victor;;;", "FN:Victor Croitoru",
    "TITLE:iOS Developer",
    "URL:https://www.linkedin.com/in/victor-croitoru-dev001",
    "URL:https://www.facebook.com/victor.croitoru.dev",
    "ADR;TYPE=HOME:;;;Chișinău;;;Moldova",
    "END:VCARD",
])

for name, data in (("cv-link", URL), ("contact-vcard", VCARD)):
    code = segno.make(data, error="m", encoding="utf-8")
    code.save(OUT / f"{name}.png", scale=14, border=4)
    code.save(OUT / f"{name}.svg", scale=14, border=4)
    print(name, "version", code.version, "size", code.symbol_size())
