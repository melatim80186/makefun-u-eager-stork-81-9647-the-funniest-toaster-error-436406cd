"""The Funniest Toaster Error Message — make.fun entry.

Writes one original toaster error message (<=120 chars) to
/output/entry.txt. Deterministic, Python stdlib only, no network.

The line: a real error message on a real appliance display — the toast
came out burnt, and the toaster confesses it did that on purpose,
because the owner needed a sign. Deadpan, one voice, lands on the
last two words. Chosen after 3 review rounds (see ../REVIEW.md):
it beats the field's crowded lanes (bread union, crumb tray, bagel,
ERROR 404) on freshness, reports a genuine error condition first,
and every word earns its place.
"""

import os

LINE = "E04: The toast is burnt. I did that on purpose. You needed a sign."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert all(ch.isprintable() or ch == " " for ch in text), "entry must be printable text"
    assert text == LINE, "entry must match the reviewed line exactly"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
