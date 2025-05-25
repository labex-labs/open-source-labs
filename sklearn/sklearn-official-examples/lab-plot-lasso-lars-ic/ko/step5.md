# AIC 및 BIC 기준 플롯

AIC 및 BIC 기준과 이후 선택된 정규화 매개변수를 플롯합니다.

```python
plt.plot(aic_criterion, color="tab:blue", marker="o", label="AIC 기준")
plt.plot(bic_criterion, color="tab:orange", marker="o", label="BIC 기준")
plt.vlines(
    index_alpha_path_bic,
    aic_criterion.min(),
    aic_criterion.max(),
    color="black",
    linestyle="--",
    label="선택된 alpha",
)
plt.legend()
plt.ylabel("정보 기준")
plt.xlabel("Lasso 모델 시퀀스")
_ = plt.title("AIC 및 BIC 를 통한 Lasso 모델 선택")
```
