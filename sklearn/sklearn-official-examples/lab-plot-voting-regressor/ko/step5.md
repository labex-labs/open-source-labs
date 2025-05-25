# 결과 시각화

마지막으로, 20 개 예측값을 시각화합니다. 빨간색 별표는 투표 회귀 모델 (Voting Regressor) 이 생성한 평균 예측값을 나타냅니다.

```python
# 결과 시각화
plt.figure()
plt.plot(pred1, "gd", label="GradientBoostingRegressor")
plt.plot(pred2, "b^", label="RandomForestRegressor")
plt.plot(pred3, "ys", label="LinearRegression")
plt.plot(pred4, "r*", ms=10, label="VotingRegressor")

plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.ylabel("예측값")
plt.xlabel("학습 샘플")
plt.legend(loc="best")
plt.title("회귀 모델 예측값 및 평균")

plt.show()
```
