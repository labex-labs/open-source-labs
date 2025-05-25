# 플롯 생성

판매 데이터를 나타내기 위해 막대 그래프 (barplot) 시각화를 사용합니다. 다음 단계를 따르세요.

1. `plt.subplots()`를 사용하여 figure 와 axis 객체를 생성합니다.

```python
fig, ax = plt.subplots()
```

2. axis 객체의 `barh()` 메서드를 사용하여 데이터를 플롯합니다.

```python
ax.barh(group_names, group_data)
```
