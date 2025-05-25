# 특징 이름을 사용하여 단조 제약 조건 지정

훈련 데이터에 특징 이름이 있는 경우 사전을 전달하여 단조 제약 조건을 지정할 수 있습니다. 이제 동일한 데이터를 사용하여 특징 이름을 사용하여 제약 조건을 지정하는 방법을 보여줍니다.

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
