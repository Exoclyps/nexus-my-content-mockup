# My Content cards: refresh mockup

An unofficial, interactive mockup of the **My Content** mod management cards on Nexus Mods, made by a mod author as feedback on the proposed tile redesign. It is not affiliated with Nexus Mods.

**Open `index.html`** (or the GitHub Pages link) to compare:

- **Current**: the cards as they are today
- **Refreshed**: same layout, new colors
- **Middle ground**: front-page style image tile, every action still visible
- **Compact**: four per row, small thumbnail, metrics in the footer

Use **Latest / Most endorsed** to switch between two sets of real cards. Bug counts, tag counts, quarantines, and "new" states are demo values.

The design was iterated live with community feedback: blue AI tags, a red Adult tag, DP status by the visibility switch, orange "unseen" counts, badges that wrap instead of overlapping, and more.

## Rebuilding

The page is generated from `template.html` and the card data in `assets/`.

```bash
python -I extract.py "<saved My Content page>.html"                     # Latest
python -I extract.py "<saved My Content page>.html" cards-endorsed.json # Most endorsed
python -I build.py
```

`nexus-my-content-refresh.user.css` is an optional Stylus userstyle that recolors the live classic cards.
