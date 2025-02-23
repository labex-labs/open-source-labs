# Añadir anotación con forma

Las formas se pueden utilizar para llamar la atención sobre regiones específicas de un gráfico. En este paso, agregaremos un rectángulo para resaltar el área entre x = 1 y x = 3.

```python
# Add shape annotation
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
