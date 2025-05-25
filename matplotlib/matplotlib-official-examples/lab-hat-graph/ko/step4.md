# Hat 그래프 생성

이 단계에서는 이전 단계에서 준비한 데이터와 `hat_graph` 함수를 사용하여 Hat 그래프를 생성합니다.

```python
fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Games')
ax.set_ylabel('Score')
ax.set_ylim(0, 60)
ax.set_title('Scores by number of game and players')
ax.legend()

fig.tight_layout()
plt.show()
```
