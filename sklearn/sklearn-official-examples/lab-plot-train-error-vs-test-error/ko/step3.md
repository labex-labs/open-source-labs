# 결과 플롯 함수

`matplotlib` 라이브러리를 사용하여 결과를 플롯합니다. `plt.subplot()` 함수를 사용하여 두 개의 서브플롯을 생성합니다. 첫 번째 서브플롯에서는 정규화 매개변수에 따른 학습 및 테스트 오류를 플롯하고, 최적의 정규화 매개변수에 해당하는 수직선을 표시합니다. 두 번째 서브플롯에서는 실제 계수와 추정된 계수를 플롯합니다.

```python
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.semilogx(alphas, train_errors, label="Train")
plt.semilogx(alphas, test_errors, label="Test")
plt.vlines(
    alpha_optim,
    plt.ylim()[0],
    np.max(test_errors),
    color="k",
    linewidth=3,
    label="Optimum on test",
)
plt.legend(loc="lower right")
plt.ylim([0, 1.2])
plt.xlabel("Regularization parameter")
plt.ylabel("Performance")

# Show estimated coef_ vs true coef
plt.subplot(2, 1, 2)
plt.plot(coef, label="True coef")
plt.plot(coef_, label="Estimated coef")
plt.legend()
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
plt.show()
```
