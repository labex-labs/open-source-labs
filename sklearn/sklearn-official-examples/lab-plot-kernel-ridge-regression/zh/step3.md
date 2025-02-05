# 比较支持向量回归和核岭回归的时间

我们将使用在步骤2中找到的最佳超参数，比较支持向量回归（SVR）和核岭回归（KRR）模型的拟合时间和预测时间。

```python
import time

# 拟合SVR
t0 = time.time()
svr.fit(X[:train_size], y[:train_size])
svr_fit = time.time() - t0

# 打印SVR模型的最佳参数和得分
print(f"最佳SVR的参数: {svr.best_params_}，R2得分: {svr.best_score_:.3f}")
print("SVR选择了复杂度和带宽并在%.3f秒内拟合了模型" % svr_fit)

# 拟合KRR
t0 = time.time()
kr.fit(X[:train_size], y[:train_size])
kr_fit = time.time() - t0

# 打印KRR模型的最佳参数和得分
print(f"最佳KRR的参数: {kr.best_params_}，R2得分: {kr.best_score_:.3f}")
print("KRR选择了复杂度和带宽并在%.3f秒内拟合了模型" % kr_fit)

# 计算SVR的支持向量比例
sv_ratio = svr.best_estimator_.support_.shape[0] / train_size
print("支持向量比例: %.3f" % sv_ratio)

# 使用SVR进行预测
t0 = time.time()
y_svr = svr.predict(X_plot)
svr_predict = time.time() - t0
print("SVR对%d个输入进行预测耗时%.3f秒" % (X_plot.shape[0], svr_predict))

# 使用KRR进行预测
t0 = time.time()
y_kr = kr.predict(X_plot)
kr_predict = time.time() - t0
print("KRR对%d个输入进行预测耗时%.3f秒" % (X_plot.shape[0], kr_predict))
```
