# ai-judge-relax-01 entry: writes one short text to /output/entry.txt.
# The judge reads exactly the bytes written, line ends included.
# The grader runs this twice with no network; both runs must write the same bytes.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The kettle ticks as it cools. Nobody is waiting for it.",
        "Outside a bicycle goes past, then the quiet comes back and sits down",
        "on the step beside the boots.",
        "There is a blue chair in the corner, one cushion worn thin at the edge,",
        "and a window letting the evening in a little at a time.",
        "A dog sighs once from another room and settles.",
        "The bread on the counter is still warm. The towel is still damp.",
        "Nothing here needs deciding tonight.",
        "The long breath you just took is enough.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
