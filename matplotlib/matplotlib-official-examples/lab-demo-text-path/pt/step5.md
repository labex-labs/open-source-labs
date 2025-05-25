# Criar uma Caixa de Deslocamento Ancorada (Anchored Offset Box)

Crie uma caixa de deslocamento ancorada (anchored offset box) usando AnnotationBbox para adicionar a caixa de deslocamento e definir sua posição. Use o seguinte código para criar a caixa de deslocamento ancorada:

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
