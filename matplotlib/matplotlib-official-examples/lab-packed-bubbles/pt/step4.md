# Definir Métodos de Movimento das Bolhas

A classe `BubbleChart` também contém métodos para mover as bolhas em direção ao centro de massa e verificar colisões com outras bolhas. O método `center_of_mass` calcula o centro de massa de todas as bolhas, e o método `center_distance` calcula a distância entre uma bolha e o centro de massa. O método `outline_distance` calcula a distância entre o contorno de uma bolha e os contornos de outras bolhas, e o método `check_collisions` verifica se uma nova posição de bolha colide com outras bolhas.

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
