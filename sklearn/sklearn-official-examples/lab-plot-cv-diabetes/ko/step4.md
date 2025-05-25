# alpha 선택 확인을 위한 LassoCV 사용

마지막으로, alpha 선택에 얼마나 신뢰할 수 있는지 확인하기 위해 LassoCV 를 사용합니다. 3 개의 폴드를 가진 KFold 를 사용합니다.

```python
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold

lasso_cv = LassoCV(alphas=alphas, random_state=0, max_iter=10000)
k_fold = KFold(3)

print("보너스 질문에 대한 답변:", "alpha 선택에 얼마나 신뢰할 수 있나요?")
print()
print("데이터의 서로 다른 하위 집합에서 일반화 점수를 극대화하는 alpha 매개변수:")
for k, (train, test) in enumerate(k_fold.split(X, y)):
    lasso_cv.fit(X[train], y[train])
    print(
        "[폴드 {0}] alpha: {1:.5f}, 점수: {2:.5f}".format(
            k, lasso_cv.alpha_, lasso_cv.score(X[test], y[test])
        )
    )

print()
print("답변: 서로 다른 데이터 하위 집합에 대해 다른 alpha 값을 얻었고, 게다가 이러한 alpha 값에 대한 점수가 상당히 다르기 때문에 매우 신뢰할 수 없습니다.")
```
