# ローレンツアトラクターの描画

Matplotlib の mplot3d モジュールを使用してローレンツアトラクターを描画します。

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
```
