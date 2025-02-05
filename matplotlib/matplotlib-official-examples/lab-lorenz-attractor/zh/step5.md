# 绘制洛伦兹吸引子

我们使用Matplotlib的mplot3d模块来绘制洛伦兹吸引子。

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X轴")
ax.set_ylabel("Y轴")
ax.set_zlabel("Z轴")
ax.set_title("洛伦兹吸引子")

plt.show()
```
