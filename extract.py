"""Pull mod cards out of a saved "My Content" page into assets/cards.json and copy their thumbnails.

Usage: python -I extract.py "<path to saved My Content .html>" [output name, default cards.json]
"""
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

src = Path(sys.argv[1])
out = Path(__file__).parent / "assets"
out.mkdir(exist_ok=True)
page = src.read_text(encoding="utf-8", errors="replace")

cards = []
for tile in re.split(r'<li class="mod-tile"', page)[1:]:
    def grab(pattern):
        m = re.search(pattern, tile, re.S)
        return m.group(1) if m else ""

    img = grab(r'<img src="\./([^"]+)"')
    name = os.path.basename(img)
    if img:
        shutil.copy(src.parent / html.unescape(img), out / name)
    links = re.findall(r'<li>\s*<a href="[^"]*/edit/(\w+)">([^<]+)</a>\s*(\([^)]*\))?', tile)
    cards.append(dict(
        title=html.unescape(grab(r'<h3><a[^>]*>([^<]+)</a>')),
        game=grab(r'<small><i>([^<]+)</i>'),
        cat=html.unescape(grab(r'\| <a[^>]*>([^<]+)</a>')),
        img="assets/" + name,
        links=[[l[1], l[2]] for l in links],
        hidden='value="0" checked' in tile,
        endorse=grab(r'endorsecount.*?flex-label">([^<]+)'),
        dl=grab(r'downloadcount.*?flex-label">([^<]+)'),
        comments=grab(r'tab=posts">([^<]+)'),
        disc=grab(r'tab=forum">([^<]+)'),
        last=grab(r'Last comment at : ([^<]+)'),
    ))

name = sys.argv[2] if len(sys.argv) > 2 else "cards.json"
(out / name).write_text(json.dumps(cards, ensure_ascii=False), encoding="utf-8")
print(f"{len(cards)} cards written to assets/{name}")
