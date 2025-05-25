# 눈금 레이블 끄기

각 삽입에서 눈금 레이블을 제거하려면 `tick_params()` 메서드를 사용하고 `labelleft` 및 `labelbottom`을 `False`로 설정할 수 있습니다.

```python
# 삽입의 눈금 레이블 끄기
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```
