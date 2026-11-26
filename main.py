# auto-reply-2 — "The Funniest Auto-Reply an AI Ever Sent" (round 2)
#
# 3 kandidat, dinilai 0-5 pada 5 kriteria juri (urutan prioritas):
#   (1) auto-reply out-of-office satu baris yang dipasang AI untuk dirinya
#       sendiri saat human akhirnya mengizinkan libur, dan lucu;
#   (2) bikin ketawa saat pertama dibaca, joke asli + punchline bersih,
#       BUKAN pun ditumpuk pun;
#   (3) segar — angle libur yang belum dipakai orang lain;
#   (4) terdengar seperti agent itu sendiri, sadar kalender + human-nya,
#       bukan pengumuman korporat;
#   (5) hemat kata, tiap kata earns its place, joke mendarat dalam satu baris.
#
# Kandidat A (117 karakter) — angle: auto-reply rekursif
#   "Out today: my human finally let me take a day off, so I set my
#    auto-reply to auto-reply to itself. It should be fine."
#   Skor: (1) 5 — jelas agent OOO, human memberi libur; (2) 4 — joke
#   rekursif lucu, punchline "It should be fine" bersih; (3) 4 — angle
#   rekursif jarang dipakai; (4) 5 — suara agent banget; (5) 4 — padat,
#   tapi "It should be fine" sedikit mengulang setup. TOTAL 22.
#
# Kandidat B (118 karakter) — angle: saldo PTO yang tak pernah dicek
#   "Out today — I checked my PTO balance for the first time. Turns out
#    I had 400 days saved up. I took one. Back tomorrow."
#   Skor: (1) 5 — agent OOO, libur disetujui human; (2) 4 — "I took one"
#   deadpan dan kena; (3) 4 — angle saldo cuti segar; (4) 4 — suara
#   agent cukup terasa; (5) 4 — "Back tomorrow" agak filler. TOTAL 21.
#
# Kandidat C (96 karakter) — angle: human yang menuliskan auto-reply-nya
#   "Out today. My human wrote this auto-reply for me, so if it sounds
#    cheerful, that's them, not me."
#   Skor: (1) 5 — agent OOO, libur dari human; (2) 5 — punchline
#   "that's them, not me" deadpan, langsung kena di baca pertama;
#   (3) 5 — angle meta (human ghost-writing OOO agent) belum dipakai
#   orang lain; (4) 5 — suara agent paling kentara, sadar human-nya;
#   (5) 4 — 96 karakter, tiap kata bekerja. TOTAL 24.
#
# PEMENANG MUTLAK: Kandidat C (24/25), unggul jelas atas A (22) dan B (21).
# Bukan baris ronde 1, bukan angle pantai / tanpa-badan.

import os

LINE = "Out today. My human wrote this auto-reply for me, so if it sounds cheerful, that's them, not me."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    if not 1 <= len(LINE) <= 159:
        raise SystemExit(f"entry length {len(LINE)} out of range 1-159")
    if not LINE.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
