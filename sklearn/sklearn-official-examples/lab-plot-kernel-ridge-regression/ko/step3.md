# SVR 및 커널 릿지 회귀 시간 비교

2 단계에서 찾은 최적의 하이퍼파라미터를 사용하여 SVR 및 KRR 모델의 학습 및 예측 시간을 비교합니다.

```python
import time

# SVR 학습
t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

# SVR 모델의 최적 파라미터 및 점수 출력
print(f"최적 SVR 파라미터: {svr.best_params_} 및 R2 점수: {svr.best_score_:.3f}")
print("SVR 복잡도 및 밴드폭 선택 및 모델 학습 시간: %.3f 초" % svr_fit)

# KRR 학습
t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

# KRR 모델의 최적 파라미터 및 점수 출력
print(f"최적 KRR 파라미터: {kr.best_params_} 및 R2 점수: {kr.best_score_:.3f}")
print("KRR 복잡도 및 밴드폭 선택 및 모델 학습 시간: %.3f 초" % kr_fit)

# SVR 의 지원 벡터 비율 계산
sv_ratio = svr.best_estimator_.support_.shape[0] / train_size
print("지원 벡터 비율: %.3f" % sv_ratio)

# SVR 예측
t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0
print("%d개 입력에 대한 SVR 예측 시간: %.3f 초" % (X_plot.shape[0], svr_predict))

# KRR 예측
t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0
print("%d개 입력에 대한 KRR 예측 시간: %.3f 초" % (X_plot.shape[0], kr_predict))
```
