# figure 및 ImageGrid 객체 생성

다음으로, `plt.figure` 함수를 사용하여 `figure` 객체를 생성하고 `figsize` 인수를 전달하여 figure 의 크기를 설정합니다. 그런 다음 `ImageGrid` 함수를 사용하여 `ImageGrid` 객체를 생성하고, subplot 인수로 `figure`, `111`을 전달하고, 2x2 그리드의 축을 생성하기 위해 `nrows_ncols` 인수로 `(2, 2)`를 전달하며, 축 사이의 패딩을 설정하기 위해 `axes_pad` 인수로 `0.1`을 전달합니다.

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
