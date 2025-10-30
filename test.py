import re
from typing import Iterator, List

# Precompiled patterns
# quoted pattern supports simple escaped single quotes like \'
QUOTED_RE = re.compile(r"'(?:[^'\\]|\\.)*'")       # finds single-quoted spans
HASH_RE = re.compile(r"#{2,}")                    # matches runs of 2+ # (change to {1,} if needed)

# C-level replacement string to wrap matched hashes with single quotes
# Uses backreference \g<0> to preserve the matched run
HASH_REPL = r"'\g<0>'"

def quote_hashes_fast(s: str) -> str:
    """
    Fast approach:
    - iterate through quoted spans (via QUOTED_RE.finditer)
    - for each gap (unquoted segment) run HASH_RE.sub with a C-level replacement
    - append quoted spans unchanged
    """
    out_parts: List[str] = []
    last = 0
    for m in QUOTED_RE.finditer(s):
        # unquoted segment from last -> m.start()
        if last < m.start():
            seg = s[last:m.start()]
            # C-level regex substitution (fast)
            out_parts.append(HASH_RE.sub(HASH_REPL, seg))
        # append quoted token unchanged
        out_parts.append(m.group(0))
        last = m.end()
    # trailing unquoted part
    if last < len(s):
        out_parts.append(HASH_RE.sub(HASH_REPL, s[last:]))
    return "".join(out_parts)
