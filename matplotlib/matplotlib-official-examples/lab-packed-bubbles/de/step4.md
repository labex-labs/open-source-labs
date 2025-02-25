# Definieren von Blasenbewegungs-Methoden

Die `BubbleChart`-Klasse enthält auch Methoden, um die Blasen zum Massenmittelpunkt zu bewegen und auf Kollisionen mit anderen Blasen zu prüfen. Die `center_of_mass`-Methode berechnet den Massenmittelpunkt aller Blasen, und die `center_distance`-Methode berechnet die Entfernung zwischen einer Blase und dem Massenmittelpunkt. Die `outline_distance`-Methode berechnet die Entfernung zwischen der Kontur einer Blase und den Konturen anderer Blasen, und die `check_collisions`-Methode prüft, ob eine neue Blasenposition mit anderen Blasen kollidiert.

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
