# 눈금 레이블 제거

`ax.get_xticklabels()` 메서드를 사용하여 레이블의 가시성을 변경하여 특정 서브플롯에서 눈금 레이블을 제거할 수 있습니다. 이 예제에서는 두 번째 서브플롯의 x 축 눈금 레이블을 제거합니다.

```python
plt.tick_params('x', labelbottom=False)
```
