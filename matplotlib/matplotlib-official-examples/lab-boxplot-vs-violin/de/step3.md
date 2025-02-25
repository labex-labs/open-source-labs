# Violinplot erstellen

Wir werden einen Violinplot mit der Methode `violinplot()` erstellen. Diese Methode nimmt mehrere Argumente wie Daten, showmeans, showmedians usw. entgegen.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
