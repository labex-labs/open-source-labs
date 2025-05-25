# Figure 및 ImageGrid 생성

다음으로, 그리드의 행과 열의 수를 정의하기 위해 `nrows_ncols` 매개변수를 사용하여 figure 와 ImageGrid 를 생성합니다.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
