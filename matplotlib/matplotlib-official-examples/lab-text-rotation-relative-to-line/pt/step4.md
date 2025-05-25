# Plotar texto sem rotação correta

Agora, plotaremos o texto nas localizações especificadas sem levar em consideração a rotação da linha. Isso resultará no texto sendo rotacionado em um ângulo de 45 graus, que não é o que queremos.

```python
# Plot text
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
