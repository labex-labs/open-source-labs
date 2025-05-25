# Criando o Objeto PathPatch

Agora que temos o objeto `Path`, podemos criar o objeto `PathPatch` que será usado para desenhar a Curva de Bézier no gráfico. Definiremos o `facecolor` como `'none'` para que apenas a curva seja desenhada e não preenchida.

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
