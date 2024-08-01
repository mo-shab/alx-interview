#!/usr/bin/python3
"""The main module for the lockboxes project"""

def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked"""
    if (len(boxes) == 0):
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)
