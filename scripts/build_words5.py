import re
import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
OUT = Path("src/words5.txt")

rx = re.compile(r"^[a-z]{5}$")

def main():
    print("Downloading word list...")
    with urllib.request.urlopen(URL) as resp:
        text = resp.read().decode("utf-8", errors="ignore")

    words = []
    for line in text.splitlines():
        w = line.strip().lower()
        if rx.match(w):
            words.append(w)

    words = sorted(set(words))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(words) + "\n", encoding="utf-8")

    print(f"Wrote {len(words)} words to {OUT}")

if __name__ == "__main__":
    main()

