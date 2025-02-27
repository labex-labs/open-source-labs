# 特徴量の置換に基づく特徴量の重要度

置換特徴量重要度は、不純度に基づく特徴量重要度の制限を克服します。高基数の特徴量に対するバイアスがなく、留出テストセットで計算できます。完全な置換重要度を計算します。特徴量をn回シャッフルし、モデルを再適合させてその重要度を推定します。重要度のランキングをプロットします。

```python
start_time = time.time()
result = permutation_importance(
    forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(result.importances_mean, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Feature importances using permutation on full model")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
plt.show()
```
