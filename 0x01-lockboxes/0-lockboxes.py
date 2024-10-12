#!/usr/bin/env python3
"""
This script solves the lockboxes puzzle
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from box 0.

    Args:
        boxes (list of list of int): A list of boxes,
                                     where each box contains a list of keys
                                     that can unlock other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = set()
    unlocked.add(0)
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)
