# Definieren der Blasen-Kollisions-Methode

Die `BubbleChart`-Klasse enthält auch eine Methode, um Blasen-Kollisionen zu prüfen und kollidierende Blasen umzugehen. Die `collides_with`-Methode berechnet die Entfernung zwischen einer neuen Blasenposition und den Positionen anderer Blasen. Wenn die Entfernung kleiner als Null ist, bedeutet dies, dass es eine Kollision gibt, und die Methode gibt den Index der kollidierenden Blase zurück. Die `collapse`-Methode bewegt die Blasen zum Massenmittelpunkt und um kollidierende Blasen herum, und die `plot`-Methode zeichnet die Blasen auf dem Diagramm.

```python
    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        idx_min = np.argmin(distance)
        return idx_min if type(idx_min) == np.ndarray else [idx_min]

    def collapse(self, n_iterations=50):
        """
        Bewege Blasen zum Massenmittelpunkt.

        Parameters
        ----------
        n_iterations : int, Standardwert: 50
            Anzahl der Bewegungen, die ausgeführt werden sollen.
        """
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bubbles)):
                rest_bub = np.delete(self.bubbles, i, 0)
                # versuche, direkt zum Massenmittelpunkt zu bewegen
                # Richtungsvektor von der Blase zum Massenmittelpunkt
                dir_vec = self.com - self.bubbles[i, :2]

                # Verkürze den Richtungsvektor, um die Länge 1 zu haben
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                # Berechne die neue Blasenposition
                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                # Prüfe, ob die neue Blase mit anderen Blasen kollidiert
                if not self.check_collisions(new_bubble, rest_bub):
                    self.bubbles[i, :] = new_bubble
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    # Versuche, um eine Blase zu bewegen, mit der du kollidierst
                    # finde die kollidierende Blase
                    for colliding in self.collides_with(new_bubble, rest_bub):
                        # Berechne den Richtungsvektor
                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        # Berechne den orthogonalen Vektor
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        # Teste, in welche Richtung zu gehen
                        new_point1 = (self.bubbles[i, :2] + orth *
                                      self.step_dist)
                        new_point2 = (self.bubbles[i, :2] - orth *
                                      self.step_dist)
                        dist1 = self.center_distance(
                            self.com, np.array([new_point1]))
                        dist2 = self.center_distance(
                            self.com, np.array([new_point2]))
                        new_point = new_point1 if dist1 < dist2 else new_point2
                        new_bubble = np.append(new_point, self.bubbles[i, 2:4])
                        if not self.check_collisions(new_bubble, rest_bub):
                            self.bubbles[i, :] = new_bubble
                            self.com = self.center_of_mass()

            if moves / len(self.bubbles) < 0.1:
                self.step_dist = self.step_dist / 2

    def plot(self, ax, labels, colors):
        """
        Zeichne das Blasen-Diagramm.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
        labels : Liste
            Labels der Blasen.
        colors : Liste
            Farben der Blasen.
        """
        for i in range(len(self.bubbles)):
            circ = plt.Circle(
                self.bubbles[i, :2], self.bubbles[i, 2], color=colors[i])
            ax.add_patch(circ)
            ax.text(*self.bubbles[i, :2], labels[i],
                    horizontalalignment='center', verticalalignment='center')
```
