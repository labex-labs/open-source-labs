# Figure 및 외부 그리드 생성

다음으로, `add_gridspec` 함수를 사용하여 figure 와 외부 그리드를 생성합니다. 서브플롯 간 간격 없이 4x4 그리드를 생성합니다.

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
