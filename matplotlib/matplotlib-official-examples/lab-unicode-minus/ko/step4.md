# 눈금 레이블 설정

기본적으로 음수 값의 눈금 레이블은 ASCII 하이픈 대신 유니코드 마이너스를 사용하여 렌더링됩니다. 하지만 `axes.unicode_minus`를 `False`로 설정하여 이 동작을 변경할 수 있습니다.

```python
plt.rcParams['axes.unicode_minus'] = False
```
