# 결정 경계 시각화

이 단계에서는 이전 단계에서 생성된 결정 경계를 시각화합니다. SVM 모델의 `coef_`와 `intercept_` 속성을 사용하여 결정 경계를 플롯합니다.

```python
    for coef, intercept, col in zip(svm.coef_, svm.intercept_, classes):
        line2 = -(line * coef[1] + intercept) / coef[0]
        ax.plot(line2, line, "-", c=colors[col[0]])
        ax.plot(line2, line, "--", c=colors[col[1]])
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title)
    ax.set_aspect("equal")
```
