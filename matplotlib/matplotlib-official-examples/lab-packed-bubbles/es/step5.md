# Definir el método de colisión de burbujas

La clase `BubbleChart` también contiene un método para comprobar las colisiones de burbujas y moverse alrededor de las burbujas en colisión. El método `collides_with` calcula la distancia entre una nueva posición de burbuja y las posiciones de otras burbujas. Si la distancia es menor que cero, significa que hay una colisión y el método devuelve el índice de la burbuja en colisión. El método `collapse` mueve las burbujas hacia el centro de masa y alrededor de las burbujas en colisión, y el método `plot` dibuja las burbujas en el gráfico.

```python
    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        idx_min = np.argmin(distance)
        return idx_min if type(idx_min) == np.ndarray else [idx_min]

    def collapse(self, n_iterations=50):
        """
        Mueve las burbujas hacia el centro de masa.

        Parámetros
        ----------
        n_iterations : int, valor predeterminado: 50
            Número de movimientos a realizar.
        """
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bubbles)):
                rest_bub = np.delete(self.bubbles, i, 0)
                # intenta moverse directamente hacia el centro de masa
                # vector de dirección desde la burbuja hasta el centro de masa
                dir_vec = self.com - self.bubbles[i, :2]

                # acorta el vector de dirección para que tenga una longitud de 1
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                # calcula la nueva posición de la burbuja
                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                # comprueba si la nueva burbuja choca con otras burbujas
                if not self.check_collisions(new_bubble, rest_bub):
                    self.bubbles[i, :] = new_bubble
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    # intenta moverse alrededor de una burbuja con la que chocas
                    # encuentra la burbuja en colisión
                    for colliding in self.collides_with(new_bubble, rest_bub):
                        # calcula el vector de dirección
                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        # calcula el vector ortogonal
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        # prueba en qué dirección ir
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
        Dibuja el gráfico de burbujas.

        Parámetros
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Etiquetas de las burbujas.
        colors : list
            Colores de las burbujas.
        """
        for i in range(len(self.bubbles)):
            circ = plt.Circle(
                self.bubbles[i, :2], self.bubbles[i, 2], color=colors[i])
            ax.add_patch(circ)
            ax.text(*self.bubbles[i, :2], labels[i],
                    horizontalalignment='center', verticalalignment='center')
```
