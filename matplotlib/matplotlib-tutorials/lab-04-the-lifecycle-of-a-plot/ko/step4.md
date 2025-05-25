# 플롯 스타일 사용자 정의

시각적으로 더 매력적인 플롯을 만들기 위해 스타일을 변경할 수 있습니다. 다음 단계를 따르세요.

1. `print(plt.style.available)`를 사용하여 사용 가능한 스타일 목록을 출력합니다.

```python
print(plt.style.available)
```

2. 스타일을 선택하고 `plt.style.use(style_name)`를 사용하여 적용합니다.

```python
plt.style.use('fivethirtyeight')
```

3. 플롯을 다시 표시해 보겠습니다.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```
