# figure 및 플롯 생성

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

두 개의 서브플롯이 있는 figure 를 생성하고, 두 세트의 데이터를 플롯합니다. 또한 플롯에 범례 (legend) 를 추가합니다.
