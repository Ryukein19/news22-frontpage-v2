"""news-image-20261122 v2 entrypoint.

Copies the shipped front-page image (entry.png, rendered from
frontpage.html: 34 verified stories from Sunday 22 November 2026,
art-first layout) to the grader's output directory.

Standard library only. No network. Deterministic: the output bytes
are identical to the shipped entry.png on every run.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
