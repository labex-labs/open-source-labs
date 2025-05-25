# figure 와 subplot 생성

데이터를 플롯하기 위해 figure 와 subplot 을 생성해야 합니다. 두 개의 subplot 이 있는 플롯을 생성할 것입니다.

```python
fig = plt.figure()

ax = fig.add_subplot(211)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")

ax = fig.add_subplot(223)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")
```
