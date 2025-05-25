# 여러 시각화 결합

시각화에 추가적인 플롯 요소를 추가할 수 있습니다. 다음 단계를 따르세요.

1. 판매 데이터의 평균을 나타내는 수직선을 추가합니다.

```python
ax.axvline(group_mean, ls='--', color='r')
```

2. 플롯에 새로운 회사를 주석 처리합니다.

```python
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")
```

3. 플롯 제목의 위치를 조정합니다.

```python
ax.title.set(y=1.05)
```

4. 전체 코드는 아래에 나와 있습니다.

```python
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')

plt.show()
```
