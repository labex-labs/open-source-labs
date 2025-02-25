# Weitere benutzerdefinierte Violinplots erstellen

Wir werden weitere benutzerdefinierte Violinplots mit unterschiedlichen Parametern erstellen.

```python
# Benutzerdefinierter Violinplot 6
axs[1, 0].violinplot(data, pos, points=80, vert=False, widths=0.7,
                     showmeans=True, showextrema=True, showmedians=True)
axs[1, 0].set_title('Benutzerdefinierter Violinplot 6', fontsize=fs)

# Benutzerdefinierter Violinplot 7
axs[1, 1].violinplot(data, pos, points=100, vert=False, widths=0.9,
                     showmeans=True, showextrema=True, showmedians=True,
                     bw_method='silverman')
axs[1, 1].set_title('Benutzerdefinierter Violinplot 7', fontsize=fs)

# Benutzerdefinierter Violinplot 8
axs[1, 2].violinplot(data, pos, points=200, vert=False, widths=1.1,
                     showmeans=True, showextrema=True, showmedians=True,
                     bw_method=0.5)
axs[1, 2].set_title('Benutzerdefinierter Violinplot 8', fontsize=fs)

# Benutzerdefinierter Violinplot 9
axs[1, 3].violinplot(data, pos, points=200, vert=False, widths=1.1,
                     showmeans=True, showextrema=True, showmedians=True,
                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]],
                     bw_method=0.5)
axs[1, 3].set_title('Benutzerdefinierter Violinplot 9', fontsize=fs)

# Benutzerdefinierter Violinplot 10
axs[1, 4].violinplot(data[-1:], pos[-1:], points=200, vert=False, widths=1.1,
                     showmeans=True, showextrema=True, showmedians=True,
                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
axs[1, 4].set_title('Benutzerdefinierter Violinplot 10', fontsize=fs)
```
