# 데이터셋의 첫 번째 샘플에 대한 클래스 확률 가져오기

데이터셋의 첫 번째 샘플에 대한 클래스 확률을 가져와 class1_1 과 class2_1 에 저장합니다.

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```
