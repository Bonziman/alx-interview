#!/usr/bin/env python3
"""
This script solves the lockboxes puzzle
"""


def canUnlockAll(boxes):
    unlocked = set()
    unlocked.add(0)
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)
