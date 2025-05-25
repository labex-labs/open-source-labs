# Importância das Características baseada na Diminuição Média da Impureza

As importâncias das características são fornecidas pelo atributo ajustado `feature_importances_` e são calculadas como a média e o desvio padrão da acumulação da diminuição da impureza em cada árvore. Vamos plotar a importância baseada na impureza.

```python
start_time = time.time()
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Importâncias das características usando MDI")
ax.set_ylabel("Diminuição média da impureza")
fig.tight_layout()
```
