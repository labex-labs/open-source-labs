# Определяем метод столкновения пузырьков

Класс `BubbleChart` также содержит метод для проверки столкновений пузырьков и перемещения вокруг столкнувшихся пузырьков. Метод `collides_with` вычисляет расстояние между новой позицией пузырька и позициями других пузырьков. Если расстояние меньше нуля, это означает, что есть столкновение, и метод возвращает индекс столкнувшегося пузырька. Метод `collapse` перемещает пузырьки к центру масс и вокруг столкнувшихся пузырьков, а метод `plot` рисует пузырьки на графике.

```python
    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        idx_min = np.argmin(distance)
        return idx_min if type(idx_min) == np.ndarray else [idx_min]

    def collapse(self, n_iterations=50):
        """
        Перемещает пузырьки к центру масс.

        Параметры
        ----------
        n_iterations : int, по умолчанию: 50
            Количество перемещений для выполнения.
        """
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bubbles)):
                rest_bub = np.delete(self.bubbles, i, 0)
                # пытаемся переместиться напрямую к центру масс
                # вектор направления от пузырька к центру масс
                dir_vec = self.com - self.bubbles[i, :2]

                # укорачиваем вектор направления, чтобы длина была равна 1
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                # вычисляем новую позицию пузырька
                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                # проверяем, сталкивается ли новый пузырек с другими пузырьками
                if not self.check_collisions(new_bubble, rest_bub):
                    self.bubbles[i, :] = new_bubble
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    # пытаемся переместиться вокруг пузырька, с которым сталкиваемся
                    # находим столкнувшийся пузырек
                    for colliding in self.collides_with(new_bubble, rest_bub):
                        # вычисляем вектор направления
                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        # вычисляем ортогональный вектор
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        # проверяем, в какую сторону идти
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
        Рисует график с пузырьками.

        Параметры
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Метки для пузырьков.
        colors : list
            Цвета для пузырьков.
        """
        for i in range(len(self.bubbles)):
            circ = plt.Circle(
                self.bubbles[i, :2], self.bubbles[i, 2], color=colors[i])
            ax.add_patch(circ)
            ax.text(*self.bubbles[i, :2], labels[i],
                    horizontalalignment='center', verticalalignment='center')
```
