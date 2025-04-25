# 绘制洛伦兹吸引子

我们使用 Matplotlib 的 mplot3d 模块来绘制洛伦兹吸引子。

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X 轴")
ax.set_ylabel("Y 轴")
ax.set_zlabel("Z 轴")
ax.set_title("洛伦兹吸引子")

plt.show()
```
