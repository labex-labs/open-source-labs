# Erstellen von benutzerdefinierten Violinplots

Wir werden benutzerdefinierte Violinplots erstellen, indem wir verschiedene Parameter ändern. Wir werden 5 benutzerdefinierte Violinplots mit unterschiedlichen Parametern erstellen.

```python
fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(10, 6))

# Benutzerdefinierter Violinplot 1
axs[0, 0].violinplot(data, pos, points=20, widths=0.3,
                     showmeans=True, showextrema=True, showmedians=True)
axs[0, 0].set_title('Benutzerdefinierter Violinplot 1', fontsize=fs)

# Benutzerdefinierter Violinplot 2
axs[0, 1].violinplot(data, pos, points=40, widths=0.5,
                     showmeans=True, showextrema=True, showmedians=True,
                     bw_method='silverman')
axs[0, 1].set_title('Benutzerdefinierter Violinplot 2', fontsize=fs)

# Benutzerdefinierter Violinplot 3
axs[0, 2].violinplot(data, pos, points=60, widths=0.7, showmeans=True,
                     showextrema=True, showmedians=True, bw_method=0.5)
axs[0, 2].set_title('Benutzerdefinierter Violinplot 3', fontsize=fs)

# Benutzerdefinierter Violinplot 4
axs[0, 3].violinplot(data, pos, points=60, widths=0.7, showmeans=True,
                     showextrema=True, showmedians=True, bw_method=0.5,
                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]])
axs[0, 3].set_title('Benutzerdefinierter Violinplot 4', fontsize=fs)

# Benutzerdefinierter Violinplot 5
axs[0, 4].violinplot(data[-1:], pos[-1:], points=60, widths=0.7,
                     showmeans=True, showextrema=True, showmedians=True,
                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
axs[0, 4].set_title('Benutzerdefinierter Violinplot 5', fontsize=fs)
```
