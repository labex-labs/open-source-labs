# 플롯에 범례 추가

이제 플롯에 범례를 추가하겠습니다. Matplotlib 에서 범례를 추가하는 두 가지 방법이 있습니다. 이 예제에서는 두 가지 방법을 모두 사용합니다.

```python
# Method 1: Place a legend above the subplot
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Method 2: Place a legend to the right of the subplot
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
