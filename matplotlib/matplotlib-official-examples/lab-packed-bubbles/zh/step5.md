# 定义气泡碰撞方法

`BubbleChart` 类还包含一个用于检查气泡碰撞并移动碰撞气泡周围其他气泡的方法。`collides_with` 方法计算新气泡位置与其他气泡位置之间的距离。如果距离小于零，则表示发生了碰撞，该方法返回碰撞气泡的索引。`collapse` 方法将气泡移向质心并在碰撞气泡周围移动，`plot` 方法在图表上绘制气泡。

```python
    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        idx_min = np.argmin(distance)
        return idx_min if type(idx_min) == np.ndarray else [idx_min]

    def collapse(self, n_iterations=50):
        """
        将气泡移向质心。

        参数
        ----------
        n_iterations : 整数，默认值：50
            要执行的移动次数。
        """
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bubbles)):
                rest_bub = np.delete(self.bubbles, i, 0)
                # 尝试直接移向质心
                # 从气泡到质心的方向向量
                dir_vec = self.com - self.bubbles[i, :2]

                # 缩短方向向量使其长度为 1
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                # 计算新的气泡位置
                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                # 检查新气泡是否与其他气泡碰撞
                if not self.check_collisions(new_bubble, rest_bub):
                    self.bubbles[i, :] = new_bubble
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    # 尝试在与你碰撞的气泡周围移动
                    # 找到碰撞气泡
                    for colliding in self.collides_with(new_bubble, rest_bub):
                        # 计算方向向量
                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        # 计算正交向量
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        # 测试向哪个方向移动
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
        绘制气泡图。

        参数
        ----------
        ax : matplotlib.axes.Axes
        labels : 列表
            气泡的标签。
        colors : 列表
            气泡的颜色。
        """
        for i in range(len(self.bubbles)):
            circ = plt.Circle(
                self.bubbles[i, :2], self.bubbles[i, 2], color=colors[i])
            ax.add_patch(circ)
            ax.text(*self.bubbles[i, :2], labels[i],
                    horizontalalignment='center', verticalalignment='center')
```
