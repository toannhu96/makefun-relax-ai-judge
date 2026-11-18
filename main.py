# ai-judge-relax-01 entry: writes one short text to /output/entry.txt.
# The judge reads exactly the bytes written, line ends included.
# The grader runs this twice with no network; both runs must write the same bytes.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "Late afternoon. The kettle has stopped ticking.",
        "Someone left the back door open an inch,",
        "and the air coming through smells of cut grass and warm stone.",
        "On the sill, a jar of pencils leans into its own shadow.",
        "A pear sits in the bowl, going a little softer, in no hurry.",
        "Down the lane a gate swings once and doesn't quite close.",
        "The cat is asleep on the folded laundry, one paw over her nose.",
        "The light crosses the floorboards slowly,",
        "the way it has every day in this house,",
        "reaching the rug, then the edge of the rug,",
        "then staying there.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
