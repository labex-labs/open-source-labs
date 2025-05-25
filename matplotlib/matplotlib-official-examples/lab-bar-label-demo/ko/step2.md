# 수직 막대 차트 레이블 지정

`bar_label` 함수를 사용하여 수직 막대 차트를 만들고 레이블을 지정하는 것으로 시작합니다. 사용할 데이터는 https://allisonhorst.github.io/palmerpenguins/에서 가져온 성별에 따른 펭귄의 수입니다.

```python
species = ('Adelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()
```
