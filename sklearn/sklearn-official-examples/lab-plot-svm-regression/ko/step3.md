# 결과 시각화

마지막으로, 샘플 데이터 세트와 비교하여 SVR 모델의 결과를 시각화합니다. 지원 벡터와 다른 학습 데이터도 함께 플롯합니다.

```python
import matplotlib.pyplot as plt

# 결과 확인
lw = 2

kernel_label = ["RBF", "Linear", "Polynomial"]
model_color = ["m", "c", "g"]

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10), sharey=True)

for ix, svr in enumerate(svrs):
    axes[ix].plot(
        X,
        svr.predict(X),
        color=model_color[ix],
        lw=lw,
        label="{} 모델".format(kernel_label[ix]),
    )
    axes[ix].scatter(
        X[svr.support_],
        y[svr.support_],
        facecolor="none",
        edgecolor=model_color[ix],
        s=50,
        label="{} 지원 벡터".format(kernel_label[ix]),
    )
    axes[ix].scatter(
        X[np.setdiff1d(np.arange(len(X)), svr.support_)],
        y[np.setdiff1d(np.arange(len(X)), svr.support_)],
        facecolor="none",
        edgecolor="k",
        s=50,
        label="다른 학습 데이터",
    )
    axes[ix].legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.1),
        ncol=1,
        fancybox=True,
        shadow=True,
    )

fig.text(0.5, 0.04, "데이터", ha="center", va="center")
fig.text(0.06, 0.5, "대상", ha="center", va="center", rotation="vertical")
fig.suptitle("지원 벡터 회귀", fontsize=14)
plt.show()
```
