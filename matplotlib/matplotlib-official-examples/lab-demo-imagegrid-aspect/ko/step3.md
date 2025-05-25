# ImageGrid 생성

이미지를 표시하기 위해 두 개의 ImageGrid 를 생성합니다. 첫 번째 ImageGrid 는 2 개의 행과 2 개의 열을 가지며, 두 번째 ImageGrid 도 2 개의 행과 2 개의 열을 가집니다.

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
