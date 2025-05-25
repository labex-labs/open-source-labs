# Figure 및 Subplot 생성

데이터를 표시하기 위해 figure 와 subplot 을 생성해야 합니다. 이 랩에서는 두 개의 subplot 을 나란히 생성합니다.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
