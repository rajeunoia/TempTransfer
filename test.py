import re
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

pattern = re.compile(r"(?:'[^']*')|(?:#{2,})")

def quote_unquoted_hashes(s: str) -> str:
    def repl(m):
        token = m.group(0)
        # if it's a quoted substring, return as-is
        if token.startswith("'") and token.endswith("'"):
            return token
        # otherwise it's a run of hashes that is unquoted — wrap it
        return f"'{token}'"
    return pattern.sub(repl, s)


# Test the problematic example + other cases
tests = [
    "Some text with #### and '###' and ### and '#####' and ##",
    "Some text with####and '###' and ### and'#####'and ##",
    "Some text (with####and CAST('#############'/#### as integer)/#####) and'#####'and ##",
    "start###middle '##' end##",
    "###",         # at start
    "'###'",       # already quoted
    "before'##'after",
]

for t in tests:
    print(t, "->")
    print(quote_hashes_fast(t))
    print()

