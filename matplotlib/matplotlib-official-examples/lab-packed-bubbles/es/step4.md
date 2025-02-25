# Definir métodos de movimiento de burbujas

La clase `BubbleChart` también contiene métodos para mover las burbujas hacia el centro de masa y comprobar si chocan con otras burbujas. El método `center_of_mass` calcula el centro de masa de todas las burbujas, y el método `center_distance` calcula la distancia entre una burbuja y el centro de masa. El método `outline_distance` calcula la distancia entre el contorno de una burbuja y los contornos de otras burbujas, y el método `check_collisions` comprueba si una nueva posición de burbuja choca con otras burbujas.

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
