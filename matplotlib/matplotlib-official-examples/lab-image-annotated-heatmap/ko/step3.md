# 함수 적용

이제 함수가 있으므로 이를 사용하여 주석이 있는 히트맵을 생성할 수 있습니다. 새로운 데이터 세트를 생성하고, `imshow`에 추가 인수를 제공하고, 주석에 정수 형식을 사용하고, 몇 가지 색상을 제공합니다. 또한 `matplotlib.ticker.FuncFormatter`를 사용하여 대각선 요소 (모두 1) 를 숨깁니다.

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Book {i}" for i in range(1, 8)]
x = [f"Store {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="weekly sold copies")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("red", "white"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```
