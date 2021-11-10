"""Facilities for working with ANSI escape sequences."""


import re
from typing import Iterable, Pattern, Text

PATTERN = re.compile(r"(\N{ESC}\[[\d;]*[a-zA-Z])")


def isplit(
    pattern: Pattern[Text], text: Text, include_separators: bool = False
) -> Iterable[Text]:
    """
    Split text into parts separated by the given pattern.

    This yields the text before the first match, then the match, then the text after
    the match and so on. If include_separators is False (the default), the separator is
    not included in the result. In any case, empty strings are never yielded.
    """
    start, end = 0, 0
    for match in pattern.finditer(text):
        # Yield the text before the match.
        end = match.start()
        if piece := text[start:end]:
            yield piece

        # Yield the match.
        if include_separators and (piece := match.group(0)):
            yield piece

        # Update the start position.
        start = match.end()

    # Yield the text after the last match.
    if piece := text[start:]:
        yield piece
