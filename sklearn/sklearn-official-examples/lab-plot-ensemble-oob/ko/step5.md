# OOB 오류율 시각화

마지막으로, 각 분류기의 OOB 오류율을 추정자 수의 함수로 플롯하여 오류율이 안정되는 추정자 수를 확인합니다. Matplotlib 을 사용하여 플롯을 생성합니다.

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("OOB error rate")
plt.legend(loc="upper right")
plt.show()
```
