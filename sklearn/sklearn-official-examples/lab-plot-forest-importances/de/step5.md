# Merkmalswichtigkeit basierend auf Merkmalspermutation

Die Merkmalspermutationswichtigkeit überwindet die Einschränkungen der auf Unreinheit basierenden Merkmalswichtigkeit: Sie haben keinen Bias gegenüber Merkmalen mit hoher Kardinalität und können auf einem separat gehaltenen Testset berechnet werden. Wir werden die volle Permutationswichtigkeit berechnen. Die Merkmale werden n-mal durchgemischt und das Modell erneut angepasst, um ihre Wichtigkeit zu schätzen. Wir werden die Wichtigkeitsrangfolge plotten.

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
