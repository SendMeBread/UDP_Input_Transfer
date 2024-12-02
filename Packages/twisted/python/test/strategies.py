# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Hypothesis strategies for values related to L{twisted.python}.
"""

from hypothesis.strategies import SearchStrategy, characters, text
from typing import Literal


def systemdDescriptorNames() -> SearchStrategy[str]:
    """
    Build strings that are legal values for the systemd
    I{FileDescriptorName} field.
    """
    # systemd.socket(5) says:
    #
    # > Names may contain any ASCII character, but must exclude control
    # > characters and ":", and must be at most 255 characters in length.
    control_characters: Literal["Cc"] = "Cc"
    return text(
        # The docs don't say there is a min size so I'm guessing...
        min_size=1,
        max_size=255,
        alphabet=characters(
            # These constraints restrict us to ASCII.
            min_codepoint=0,
            max_codepoint=127,
            # This one excludes control characters.
            blacklist_categories=(control_characters,),
            # And this excludes the separator.
            blacklist_characters=(":",),
        ),
    )
