# Adicionar linhas verticais ao histograma

Para facilitar a visualização do efeito do thresholding, adicionaremos linhas verticais ao histograma para indicar os valores atuais do limiar. Criaremos duas linhas para os valores de limiar inferior e superior, respectivamente.

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```
