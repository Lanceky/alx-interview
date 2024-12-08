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

    # Iterate through each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if current cell is land
            if grid[row][col] == 1:
                # Start with 4 sides for each land cell
                sides = 4

                # Check adjacent cells and reduce sides accordingly
                # Check cell above
                if row > 0 and grid[row-1][col] == 1:
                    sides -= 1
                
                # Check cell below
                if row < len(grid) - 1 and grid[row+1][col] == 1:
                    sides -= 1
                
                # Check cell to the left
                if col > 0 and grid[row][col-1] == 1:
                    sides -= 1
                
                # Check cell to the right
                if col < len(grid[row]) - 1 and grid[row][col+1] == 1:
                    sides -= 1
                
                # Add the remaining sides to the perimeter
                perimeter += sides

    return perimeter
