#!/usr/bin/python3
"""Module for solving the Lockboxes problem."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): A list of boxes, where each box contains
                               keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Initialize with keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
