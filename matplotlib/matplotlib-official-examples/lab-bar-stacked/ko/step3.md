# 누적 막대 차트 생성

`matplotlib.pyplot.bar`를 사용하여 누적 막대 차트를 만들고 각 체중 범주를 반복하여 막대를 쌓습니다.

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")
```
