# Définir les méthodes de mouvement des bulles

La classe `BubbleChart` contient également des méthodes pour déplacer les bulles vers le centre de masse et vérifier s'il y a des collisions avec d'autres bulles. La méthode `center_of_mass` calcule le centre de masse de toutes les bulles, et la méthode `center_distance` calcule la distance entre une bulle et le centre de masse. La méthode `outline_distance` calcule la distance entre la périphérie d'une bulle et les périphéries d'autres bulles, et la méthode `check_collisions` vérifie si une nouvelle position de bulle entre en collision avec d'autres bulles.

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
