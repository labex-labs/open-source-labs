# 플롯 모양 사용자 정의

플롯의 모양을 더 사용자 정의할 수 있습니다. 다음 단계를 따르세요.

1. x 축 레이블을 회전하여 가독성을 높입니다.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. x 축 및 y 축의 limits, labels, title 을 설정합니다.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. 플롯을 다시 표시합니다.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
