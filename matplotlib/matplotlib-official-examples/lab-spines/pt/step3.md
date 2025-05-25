# Criar Subplots

Criaremos três subplots para demonstrar diferentes customizações de spines. Usaremos o layout constrito (constrained layout) para garantir que os rótulos não se sobreponham aos eixos.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```
