# 결과 플롯

마지막으로, 다양한 반복 횟수에 대한 모델 성능을 시각화하기 위해 결과를 플롯할 수 있습니다. y 축에는 음수 로그 손실을, x 축에는 반복 횟수를 표시합니다.

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('반복 횟수')
plt.ylabel('음수 로그 손실')
plt.legend()
plt.show()
```
