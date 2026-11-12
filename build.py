"""Inline the card data sets into template.html -> index.html (so it opens straight from disk).

assets/cards.json          -> "Latest" (required)
assets/cards-endorsed.json -> "Most endorsed" (optional)
"""
import json
from pathlib import Path

here = Path(__file__).parent
sets = {"latest": json.loads((here / "assets" / "cards.json").read_text(encoding="utf-8"))}
endorsed = here / "assets" / "cards-endorsed.json"
if endorsed.exists():
    sets["endorsed"] = json.loads(endorsed.read_text(encoding="utf-8"))
page = (here / "template.html").read_text(encoding="utf-8")
page = page.replace("__SETS__", json.dumps(sets, ensure_ascii=False).replace("</", "<\\/"))
(here / "index.html").write_text(page, encoding="utf-8")
print("index.html written: " + ", ".join(f"{k} {len(v)} cards" for k, v in sets.items()))
