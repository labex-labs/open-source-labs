# scatter_hist 함수 정의

x 와 y 데이터, 그리고 산점도용 메인 축과 두 개의 주변 축, 총 세 개의 축을 입력으로 받는 `scatter_hist` 함수를 정의해야 합니다. 이 함수는 제공된 축 내에서 산점도와 히스토그램을 생성합니다.

```python
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # Remove labels from the histograms
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # Create the scatter plot
    ax.scatter(x, y)

    # Determine nice limits by hand
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')
```
