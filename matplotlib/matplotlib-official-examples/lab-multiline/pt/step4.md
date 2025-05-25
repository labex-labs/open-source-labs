# Personalizando os Rótulos dos Eixos

Para personalizar os rótulos dos eixos, podemos usar as funções `set_xlabel` e `set_ylabel`. Também podemos adicionar quebras de linha usando o caractere "\n".

```python
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
```
