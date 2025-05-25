# Plotar texto com rotação correta

Finalmente, plotaremos o texto nas localizações especificadas, levando em consideração a rotação da linha. Isso resultará no texto sendo rotacionado no ângulo correto em relação à linha.

```python
# Plot text
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
