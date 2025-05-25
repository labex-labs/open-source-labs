# 차트 사용자 정의

x 축과 y 축에 레이블을 추가하고 y 축의 스케일을 로그 스케일로 설정하여 차트의 모양을 사용자 정의할 수 있습니다.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
