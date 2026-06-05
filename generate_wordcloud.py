import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# --- Deine Begriffe (mit optionalen Gewichtungen) ---
begriffe = {
    "17. Jahrhundert": 7,
    "Vokalmusik um 1900": 8,
    "Max Reger": 7,
    "Digitale Edition": 9,
    "Hybride Edition": 10,
    "Datenmodellierung": 10,
    "XML": 9,
    "Musikcodierung (MEI)": 8,
    "Textcodierung (TEI)": 8,
    "G. F. Händel": 9,
    "Quellenkritik": 6,
    "Musiknotation": 5,
    "18. Jahrhundert": 8,
    "Textedition": 9,
    "Musikedition": 10,
    "Philologie": 10,
    "XSLT": 6,
    "XQuery": 8,
    "XPath": 8,
}
# Alternativ: einfache Liste ohne Gewichtung
# begriffe = ["Musikwissenschaft", "TEI", "Händel", ...]

# --- Grün-Violettes Farbschema ---
farben = [
    "#1a4a0a",  # Dunkelgrün (Anker)
    "#5a9a1a",  # Mittelgrün
    "#b1e053",  # Hellgrün (dein Grünton)
    "#cc7abf",  # Zwischenton (Misch aus beiden)
    "#993c8c",  # Violett (dein Violetton)
    "#5a1a5a",  # Dunkelviolett (Anker)
]

cmap = LinearSegmentedColormap.from_list("gruen_violett", farben)

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    """Färbt Wörter anhand ihrer Schriftgröße (größere = dunkler/gesättigter)."""
    # Normiere font_size auf [0, 1] – größte Wörter bekommen die erste Farbe
    t = random_state.uniform(0, 1) if random_state else 0.5
    rgba = cmap(t)
    r, g, b = int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255)
    return f"rgb({r},{g},{b})"

# --- Wordcloud erzeugen ---
wc = WordCloud(
    width=1200,
    height=600,
    background_color="white",   # oder "black" für dunklen Hintergrund
    color_func=color_func,
    max_words=100,
    prefer_horizontal=0.8,
    min_font_size=14,
    font_path=None,             # Pfad zu .ttf angeben, z.B. "/usr/share/fonts/..."
).generate_from_frequencies(begriffe)

# --- Anzeigen und speichern ---
plt.figure(figsize=(14, 7))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("wordcloud.png", dpi=150, bbox_inches="tight")
plt.show()
print("Gespeichert als wordcloud.png")