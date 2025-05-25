# 결과 플롯

축소 매개변수의 값이 다른 경우 미확인 데이터의 가능도를 플롯하고, 교차 검증, LedoitWolf, 및 OAS 추정값에 의한 선택 사항을 표시합니다.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.title("정규화된 공분산: 가능도 및 축소 계수")
plt.xlabel("정규화 매개변수: 축소 계수")
plt.ylabel("오류: 테스트 데이터에서 음의 로그 가능도")

plt.loglog(shrinkages, negative_logliks, label="음의 로그 가능도")

plt.plot(plt.xlim(), 2 * [loglik_real], "--r", label="실제 공분산 가능도")

lik_max = np.amax(negative_logliks)
lik_min = np.amin(negative_logliks)
ymin = lik_min - 6.0 * np.log((plt.ylim()[1] - plt.ylim()[0]))
ymax = lik_max + 10.0 * np.log(lik_max - lik_min)
xmin = shrinkages[0]
xmax = shrinkages[-1]

plt.vlines(
    lw.shrinkage_,
    ymin,
    -loglik_lw,
    color="magenta",
    linewidth=3,
    label="Ledoit-Wolf 추정값",
)

plt.vlines(
    oa.shrinkage_, ymin, -loglik_oa, color="purple", linewidth=3, label="OAS 추정값"
)

plt.vlines(
    cv.best_estimator_.shrinkage,
    ymin,
    -cv.best_estimator_.score(X_test),
    color="cyan",
    linewidth=3,
    label="교차 검증 최적 추정값",
)

plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.legend()

plt.show()
```
