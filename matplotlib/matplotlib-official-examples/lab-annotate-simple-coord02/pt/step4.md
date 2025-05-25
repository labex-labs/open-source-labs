# Adicionar Anotação de Forma

Formas podem ser usadas para chamar a atenção para regiões específicas de um gráfico. Nesta etapa, adicionaremos um retângulo para destacar a área entre x=1 e x=3.

```python
# Add shape annotation
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
