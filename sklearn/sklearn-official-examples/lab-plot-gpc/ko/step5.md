# LML 지형도 플롯

다양한 하이퍼파라미터 선택을 사용하여 GPC 모델의 로그 - 주변 - 가능도 지형도를 플롯합니다. 이전 플롯에서 사용된 하이퍼파라미터를 강조 표시합니다. 또한 플롯에 레이블을 지정합니다.

```python
# LML 지형도 플롯
plt.figure()
theta0 = np.logspace(0, 8, 30)
theta1 = np.logspace(-1, 1, 29)
Theta0, Theta1 = np.meshgrid(theta0, theta1)
LML = [[gp_opt.log_marginal_likelihood(np.log([Theta0[i, j], Theta1[i, j]])) for i in range(Theta0.shape[0])] for j in range(Theta0.shape[1])]
LML = np.array(LML).T
plt.plot(np.exp(gp_fix.kernel_.theta)[0], np.exp(gp_fix.kernel_.theta)[1], "ko", zorder=10)
plt.plot(np.exp(gp_opt.kernel_.theta)[0], np.exp(gp_opt.kernel_.theta)[1], "ko", zorder=10)
plt.pcolor(Theta0, Theta1, LML)
plt.xscale("log")
plt.yscale("log")
plt.colorbar()
plt.xlabel("크기")
plt.ylabel("길이 스케일")
plt.title("로그 - 주변 - 가능도")
```
