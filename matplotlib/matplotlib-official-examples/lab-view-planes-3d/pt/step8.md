# Personalizar os rótulos dos ticks e dos eixos para cada plano de visualização 3D primário

Personalizamos os rótulos dos ticks e dos eixos para cada plano de visualização 3D primário para remover quaisquer rótulos desnecessários.

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```
