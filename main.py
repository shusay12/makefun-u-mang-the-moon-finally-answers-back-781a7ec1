#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

Writes the Moon's one-line comeback to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line answers everyone who has ever stared up at the Moon: the
howlers, the wishers, and the makers of late-night promises. It is
wry and old and tired of being wished upon, and the turn lands at the
end, in one read.

Standard library only. No network, no input files, no arguments.
"""

import os
import tempfile


ENTRY_TEXT = (
    "You howl at me, wish on me, promise you'll change \u2014 "
    "I've been up here four billion years and you're still "
    "texting your ex at 2 a.m."
)


def validate_entry(text):
    """Check the entry against the competition gate before writing it.

    The gate requires UTF-8 text of 1 to 240 characters, not only
    whitespace, on a single line.
    """
    if not (1 <= len(text) <= 240):
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def check_voice(text):
    """Check the line answers all three behaviours the brief names.

    The judge's first criterion is speaking as the Moon answering the
    wishes, the howls and the late-night promises. Each of those words
    must appear in the line, and the comeback -- the 2 a.m. punchline --
    must be the last thing the line says.
    """
    lowered = text.lower()
    for word in ("howl", "wish", "promise"):
        if word not in lowered:
            raise ValueError(f"entry does not answer the {word!r} behaviour")
    if not lowered.rstrip().endswith("2 a.m."):
        raise ValueError("entry must end on the late-night comeback")
    return text


def main():
    text = check_voice(validate_entry(ENTRY_TEXT))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write atomically so a reader never sees a half-written entry.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    # Read the entry back and confirm it is exactly what was intended.
    with open(path, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            raise RuntimeError(f"entry on disk does not match {text!r}")
    print(f"wrote {len(text)} character(s) to {path}")


if __name__ == "__main__":
    main()
