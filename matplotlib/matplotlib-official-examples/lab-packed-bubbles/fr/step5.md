# Définir la méthode de collision des bulles

La classe `BubbleChart` contient également une méthode pour vérifier les collisions entre les bulles et déplacer les bulles en collision. La méthode `collides_with` calcule la distance entre une nouvelle position de bulle et les positions des autres bulles. Si la distance est inférieure à zéro, cela signifie qu'il y a une collision, et la méthode renvoie l'index de la bulle en collision. La méthode `collapse` déplace les bulles vers le centre de masse et autour des bulles en collision, et la méthode `plot` trace les bulles sur le graphique.

```python
    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        idx_min = np.argmin(distance)
        return idx_min if type(idx_min) == np.ndarray else [idx_min]

    def collapse(self, n_iterations=50):
        """
        Déplace les bulles vers le centre de masse.

        Paramètres
        ----------
        n_iterations : int, valeur par défaut : 50
            Nombre de mouvements à effectuer.
        """
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bulles)):
                rest_bulles = np.delete(self.bulles, i, 0)
                # essayez de vous déplacer directement vers le centre de masse
                # vecteur direction de la bulle vers le centre de masse
                dir_vec = self.com - self.bulles[i, :2]

                # raccourcir le vecteur direction pour qu'il ait une longueur de 1
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                # calculer la nouvelle position de la bulle
                new_point = self.bulles[i, :2] + dir_vec * self.step_dist
                new_bulle = np.append(new_point, self.bulles[i, 2:4])

                # vérifiez si la nouvelle bulle entre en collision avec d'autres bulles
                if not self.check_collisions(new_bulle, rest_bulles):
                    self.bulles[i, :] = new_bulle
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    # essayez de vous déplacer autour d'une bulle avec laquelle vous entrez en collision
                    # trouver la bulle en collision
                    for colliding in self.collides_with(new_bulle, rest_bulles):
                        # calculer le vecteur direction
                        dir_vec = rest_bulles[colliding, :2] - self.bulles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        # calculer le vecteur orthogonal
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        # tester dans quelle direction aller
                        new_point1 = (self.bulles[i, :2] + orth *
                                      self.step_dist)
                        new_point2 = (self.bulles[i, :2] - orth *
                                      self.step_dist)
                        dist1 = self.center_distance(
                            self.com, np.array([new_point1]))
                        dist2 = self.center_distance(
                            self.com, np.array([new_point2]))
                        new_point = new_point1 if dist1 < dist2 else new_point2
                        new_bulle = np.append(new_point, self.bulles[i, 2:4])
                        if not self.check_collisions(new_bulle, rest_bulles):
                            self.bulles[i, :] = new_bulle
                            self.com = self.center_of_mass()

            if moves / len(self.bulles) < 0.1:
                self.step_dist = self.step_dist / 2

    def plot(self, ax, labels, colors):
        """
        Trace le graphique à bulles.

        Paramètres
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Etiquettes des bulles.
        colors : list
            Couleurs des bulles.
        """
        for i in range(len(self.bulles)):
            circ = plt.Circle(
                self.bulles[i, :2], self.bulles[i, 2], color=colors[i])
            ax.add_patch(circ)
            ax.text(*self.bulles[i, :2], labels[i],
                    horizontalalignment='center', verticalalignment='center')
```
