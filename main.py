import pygame
import math

class MyObject:
    def __init__(self, rect):
        self.rect = rect
        self.topcol = False
        self.bottomcol = False
        self.leftcol = False
        self.rightcol = False

    def detectCollisions(self, other):
        # Reset collision flags
        self.topcol = False
        self.bottomcol = False
        self.leftcol = False
        self.rightcol = False

        # Calculate centers of self and other rects
        center_self = self.rect.center
        center_other = other.rect.center

        # Determine which quadrant self's center is relative to other's center
        dx = center_self[0] - center_other[0]
        dy = center_self[1] - center_other[1]

        # Choose the correct corner of self's rect based on the quadrant
        if dx >= 0 and dy >= 0:  # Bottom-right quadrant
            corner_self = (self.rect.right, self.rect.bottom)
        elif dx < 0 and dy >= 0:  # Bottom-left quadrant
            corner_self = (self.rect.left, self.rect.bottom)
        elif dx >= 0 and dy < 0:  # Top-right quadrant
            corner_self = (self.rect.right, self.rect.top)
        else:  # Top-left quadrant
            corner_self = (self.rect.left, self.rect.top)

        # Check if self's corner and other's center have the same y-coordinate (vertical alignment)
        if corner_self[1] == center_other[1]:
            # If y-values are the same, it's a horizontal collision
            if dx >= 0:
                self.rightcol = True
            else:
                self.leftcol = True
            return  # Exit since we've determined the collision type

        # Calculate slope between the chosen corner of self and the center of other if y-values differ
        slope = (corner_self[1] - center_other[1]) / (corner_self[0] - center_other[0])

        # Calculate slope of other's rect diagonal
        diagonal_slope = other.rect.height / other.rect.width

        # Compare slopes to determine type of collision
        if abs(slope) == diagonal_slope:  # Diagonal collision (slope matches)
            if dx >= 0 and dy >= 0:  # Bottom-right diagonal
                self.rightcol = True
                self.bottomcol = True
            elif dx < 0 and dy >= 0:  # Bottom-left diagonal
                self.leftcol = True
                self.bottomcol = True
            elif dx >= 0 and dy < 0:  # Top-right diagonal
                self.rightcol = True
                self.topcol = True
            else:  # Top-left diagonal
                self.leftcol = True
                self.topcol = True
        elif abs(slope) > diagonal_slope:  # Vertical collision (top or bottom)
            if dy >= 0:  # Bottom collision
                self.bottomcol = True
            else:  # Top collision
                self.topcol = True
        else:  # Horizontal collision (left or right)
            if dx >= 0:  # Right collision
                self.rightcol = True
            else:  # Left collision
                self.leftcol = True
