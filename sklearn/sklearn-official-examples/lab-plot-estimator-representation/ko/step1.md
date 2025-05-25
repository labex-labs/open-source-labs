# 압축된 텍스트 표현

추정기를 표시하는 첫 번째 방법은 압축된 텍스트 표현입니다. 추정기는 문자열로 표시될 때 기본값이 아닌 값으로 설정된 매개변수만 표시합니다. 이는 시각적인 노이즈를 줄이고 인스턴스를 비교할 때 차이점을 더 쉽게 파악할 수 있도록 합니다.

```python
from sklearn.linear_model import LogisticRegression

# l1 패널티를 가진 로지스틱 회귀의 인스턴스 생성
lr = LogisticRegression(penalty="l1")

# 추정기 표시
print(lr)
```
