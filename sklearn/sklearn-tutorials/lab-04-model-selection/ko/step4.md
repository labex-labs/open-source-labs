# 교차 검증된 추정자

Scikit-learn 의 일부 추정자는 내장된 교차 검증 기능을 가지고 있습니다. 이러한 교차 검증된 추정자는 교차 검증을 통해 자동으로 매개변수를 선택하여 모델 선택 프로세스를 더욱 효율적으로 만듭니다.

```python
from sklearn import linear_model, datasets

# LassoCV 객체 생성
lasso = linear_model.LassoCV()

# 당뇨병 데이터셋 로드
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# 데이터셋에 LassoCV 객체 맞추기
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```
