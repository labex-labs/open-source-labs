# Figure 와 Axes 생성

`plt.subplots()`를 사용하여 figure 와 axes 객체를 생성합니다. `imshow()` 함수는 임의의 데이터를 이미지로 표시하는 데 사용됩니다.

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```
