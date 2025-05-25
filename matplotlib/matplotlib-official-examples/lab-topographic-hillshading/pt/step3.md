# Especificar o Tamanho da Célula

Se você precisar de uma exageração vertical topograficamente precisa, ou não quiser adivinhar qual deve ser o `vert_exag`, você precisará especificar o tamanho da célula da grade (ou seja, os parâmetros `dx` e `dy`). Caso contrário, qualquer valor de `vert_exag` que você especificar será relativo ao espaçamento da grade dos seus dados de entrada. Nesta etapa, calculamos os valores de `dx` e `dy` em metros.

```python
dy = 111200 * dy
dx = 111200 * dx * np.cos(np.radians(dem['ymin']))
```
