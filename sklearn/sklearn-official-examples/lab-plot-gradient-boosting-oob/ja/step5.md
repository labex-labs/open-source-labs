# 結果をプロットする

最後に、異なる反復回数に対するモデルの性能を視覚化するために結果をプロットすることができます。y 軸に負のログ損失を、x 軸に反復回数をプロットします。

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('Number of iterations')
plt.ylabel('Negative log-loss')
plt.legend()
plt.show()
```
