# Linhas de Fluxo (Streamlines) Contínuas

Nesta etapa, criaremos um streamplot com linhas de fluxo contínuas. O parâmetro `broken_streamlines` controla se as linhas de fluxo devem ser interrompidas quando excedem o limite de linhas dentro de uma única célula da grade.

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
