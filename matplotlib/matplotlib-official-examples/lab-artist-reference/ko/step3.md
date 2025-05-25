# 도형 그리기

이제 `shapes` 리스트를 반복하고 플롯에 추가하여 Matplotlib 를 사용하여 도형을 그립니다.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
