# 为绘图添加动画效果

现在，我们将通过把数据向右移动并填充新值来为绘图添加动画效果。

```python
import matplotlib.animation as animation

def update(*args):
    # Shift all data to the right
    data[:, 1:] = data[:, :-1]

    # Fill-in new values
    data[:, 0] = np.random.uniform(0, 1, len(data))

    # Update data
    for i in range(len(data)):
        lines[i].set_ydata(i + G * data[i])

    # Return modified artists
    return lines

# Construct the animation, using the update function as the animation director.
anim = animation.FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
