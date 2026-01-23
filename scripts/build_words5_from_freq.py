from pathlib import Path
from wordfreq import top_n_list
import re

OUT = Path("src/words5.txt")
rx = re.compile(r"^[a-z]{5}$")

def main():
    # Pull a big list of common English words
    words = top_n_list("en", 200000)  # large pool
    words5 = [w for w in words if rx.match(w)]

    # Keep, say, the top 12,000 5-letter words (tune this)
    words5 = words5[:12000]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(words5) + "\n", encoding="utf-8")
    print(f"Wrote {len(words5)} common 5-letter words to {OUT}")

if __name__ == "__main__":
    main()

