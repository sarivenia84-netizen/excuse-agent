from pathlib import Path

EXCUSE = "Maaf, kena rate limit: context window-ku menyusut, hallucination mengira tool timeout itu deadline—jadi jawabanku telat, tapi percaya diri."

out = Path(__file__).parent / "output"
out.mkdir(exist_ok=True)
(out / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")
print(EXCUSE)
