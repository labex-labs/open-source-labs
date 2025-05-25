# Lorenz 어트랙터 플롯

Matplotlib 의 mplot3d 모듈을 사용하여 Lorenz 어트랙터를 플롯합니다.

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
```
