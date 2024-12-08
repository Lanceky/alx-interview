#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A 2D grid representing land and water.
                                    0 represents water, 1 represents land.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0

    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] == 1:
                sides = 4

                # Check cell above
                if row_index > 0 and grid[row_index - 1][col_index] == 1:
                    sides -= 1

                # Check cell below
                if row_index < len(grid) - 1 and grid[row_index + 1][col_index] == 1:
                    sides -= 1

                # Check cell to the left
                if col_index > 0 and grid[row_index][col_index - 1] == 1:
                    sides -= 1

                # Check cell to the right
                if col_index < len(grid[row_index]) - 1 and \
                   grid[row_index][col_index + 1] == 1:
                    sides -= 1

                perimeter += sides

    return perimeter
