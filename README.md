# Collision Detection System in Pygame

This repository contains an object-oriented collision detection system implemented in Python using the Pygame library. The system allows you to detect and handle precise collisions between rectangular objects, including top, bottom, left, right, and diagonal collisions.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Example](#example)
  - [Collision Flags](#collision-flags)
- [How It Works](#how-it-works)
  - [Quadrant-Based Detection](#quadrant-based-detection)
  - [Slope and Diagonal Comparison](#slope-and-diagonal-comparison)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Object-Oriented Design**: Collision detection is encapsulated in a class, making it easy to manage and scale in larger projects.
- **Quadrant-Based Detection**: Detects collisions based on the relative position (quadrant) of two rectangles.
- **Slope-Based Collision**: Uses the slope between object corners and centers to handle precise diagonal collisions.
- **Separate Collision Flags**: Detects collisions on all sides (`top`, `bottom`, `left`, `right`), including diagonal cases.
- **Simple to Use**: Just instantiate objects with their rectangles and call the detection method.

---

## Installation
To use this collision detection system, you'll need to install [Pygame](https://www.pygame.org/), which can be done via `pip`:

```bash
pip install pygame
```

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/collision-detection-pygame.git
cd collision-detection-pygame
```

---

## Usage

1. **Import the Required Libraries**:
   Make sure Pygame is installed, and then import the necessary modules and classes.

2. **Define Objects**:
   You can create two or more objects with their respective rectangles and detect collisions between them.

### Example

```python
import pygame
from myobject import MyObject

# Initialize Pygame
pygame.init()

# Define two rectangles
rect1 = pygame.Rect(50, 50, 100, 100)
rect2 = pygame.Rect(120, 80, 100, 100)

# Create objects using the rectangles
obj1 = MyObject(rect1)
obj2 = MyObject(rect2)

# Detect collisions between obj1 and obj2
obj1.detectCollisions(obj2)

# Print which sides of obj1 are colliding with obj2
print("Top collision:", obj1.topcol)
print("Bottom collision:", obj1.bottomcol)
print("Left collision:", obj1.leftcol)
print("Right collision:", obj1.rightcol)

pygame.quit()
```

### Collision Flags
After calling `detectCollisions()`, the object will have the following flags available:

- `topcol`: Indicates if a collision occurred at the top.
- `bottomcol`: Indicates if a collision occurred at the bottom.
- `leftcol`: Indicates if a collision occurred on the left side.
- `rightcol`: Indicates if a collision occurred on the right side.

These flags will be set to `True` if a collision occurs in the corresponding direction.

---

## How It Works

### Quadrant-Based Detection
The collision detection system works by determining which quadrant `self.rect` is relative to `other.rect`. This helps narrow down the potential collision type and selects a relevant corner of the object to compare against the center of the other rectangle.

### Slope and Diagonal Comparison
To further refine the collision detection:
- The slope between the selected corner of `self.rect` and the center of `other.rect` is calculated.
- If the slope matches the diagonal slope of `other.rect`, the system triggers both horizontal and vertical collisions (for example, top and left for a top-left diagonal collision).
- If the slope is greater or less than the diagonal, it triggers vertical or horizontal collisions accordingly.

This approach ensures precise collision detection, especially for objects colliding along diagonal edges.

---

## Contributing
Contributions are welcome! If you'd like to improve the system or add new features, feel free to fork the repository and submit a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

Please make sure to test any changes thoroughly before submitting.

---

## License
This project is licensed under the MIT License.
