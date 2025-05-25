# 주기적 스플라인

`SplineTransformer`를 사용하고 노드를 수동으로 지정하여 주기적 스플라인의 사용을 보여줍니다. 릿지 회귀 모델을 학습 데이터에 맞추고 주기적 스플라인을 사용하여 함수, 학습 점 및 보간 결과를 플롯합니다.

```python
def g(x):
    """주기적 스플라인 보간으로 근사할 함수."""
    return np.sin(x) - 0.7 * np.cos(x * 3)


y_train = g(x_train)

# 테스트 데이터를 미래로 확장:
x_plot_ext = np.linspace(-1, 21, 200)
X_plot_ext = x_plot_ext[:, np.newaxis]

lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(color=["black", "tomato", "teal"])
ax.plot(x_plot_ext, g(x_plot_ext), linewidth=lw, label="실제 값")
ax.scatter(x_train, y_train, label="학습 점")

for transformer, label in [
    (SplineTransformer(degree=3, n_knots=10), "스플라인"),
    (
        SplineTransformer(
            degree=3,
            knots=np.linspace(0, 2 * np.pi, 10)[:, None],
            extrapolation="periodic",
        ),
        "주기적 스플라인",
    ),
]:
    model = make_pipeline(transformer, Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot_ext = model.predict(X_plot_ext)
    ax.plot(x_plot_ext, y_plot_ext, label=label)

ax.legend()
fig.show()
```
