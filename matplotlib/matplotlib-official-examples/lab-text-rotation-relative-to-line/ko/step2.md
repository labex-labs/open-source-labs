# 플롯의 제한 조정

다음으로, 화면에서 볼 때 대각선이 더 이상 45 도 각도가 아니도록 플롯의 제한을 조정합니다. 이렇게 하면 화면 좌표계가 아닌 선을 기준으로 텍스트를 회전해야 하는 시나리오가 생성됩니다.

```python
# set limits so that it no longer looks on screen to be 45 degrees
ax.set_xlim([-10, 20])
```
