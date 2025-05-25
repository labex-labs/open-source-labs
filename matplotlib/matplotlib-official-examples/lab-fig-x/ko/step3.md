# Figure 에 선 추가

`fig.add_artist()` 메서드를 사용하여 Figure 에 선을 추가할 수 있습니다. (0,0) 에서 (1,1) 까지, 그리고 (0,1) 에서 (1,0) 까지 두 개의 선을 생성합니다.

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```
