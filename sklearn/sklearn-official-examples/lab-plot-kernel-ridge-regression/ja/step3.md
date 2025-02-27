# SVR と Kernel Ridge Regression の時間を比較する

我々は、ステップ 2 で見つけた最適なハイパーパラメータを使って、SVR と KRR モデルのフィッティングと予測の時間を比較します。

```python
import time

# SVR をフィッティングする
t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

# SVR モデルの最適なパラメータとスコアを表示する
print(f"Best SVR with params: {svr.best_params_} and R2 score: {svr.best_score_:.3f}")
print("SVR complexity and bandwidth selected and model fitted in %.3f s" % svr_fit)

# KRR をフィッティングする
t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

# KRR モデルの最適なパラメータとスコアを表示する
print(f"Best KRR with params: {kr.best_params_} and R2 score: {kr.best_score_:.3f}")
print("KRR complexity and bandwidth selected and model fitted in %.3f s" % kr_fit)

# SVR のサポートベクトル比を計算する
sv_ratio = svr.best_estimator_.support_.shape[0] / train_size
print("Support vector ratio: %.3f" % sv_ratio)

# SVR を使って予測する
t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0
print("SVR prediction for %d inputs in %.3f s" % (X_plot.shape[0], svr_predict))

# KRR を使って予測する
t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0
print("KRR prediction for %d inputs in %.3f s" % (X_plot.shape[0], kr_predict))
```
