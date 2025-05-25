# 랜덤 데이터에 대한 퍼뮤테이션 테스트 점수

다음으로, 피처와 레이블 간에 의존성이 없어야 하는 랜덤하게 생성된 피처와 붓꽃 레이블을 사용하여 `permutation_test_score`를 계산합니다.

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
