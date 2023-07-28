# Define Bubble Movement Methods

The `BubbleChart` class also contains methods to move the bubbles towards the center of mass and check for collisions with other bubbles. The `center_of_mass` method calculates the center of mass of all the bubbles, and the `center_distance` method calculates the distance between a bubble and the center of mass. The `outline_distance` method calculates the distance between a bubble's outline and the outlines of other bubbles, and the `check_collisions` method checks if a new bubble position collides with other bubbles.

```python
    def center_of_mass(self):
        return np.average(
            self.bubbles[:, :2], axis=0, weights=self.bubbles[:, 3]
        )

    def center_distance(self, bubble, bubbles):
        return np.hypot(bubble[0] - bubbles[:, 0],
                        bubble[1] - bubbles[:, 1])

    def outline_distance(self, bubble, bubbles):
        center_distance = self.center_distance(bubble, bubbles)
        return center_distance - bubble[2] - \
            bubbles[:, 2] - self.bubble_spacing

    def check_collisions(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        return len(distance[distance < 0])
```
