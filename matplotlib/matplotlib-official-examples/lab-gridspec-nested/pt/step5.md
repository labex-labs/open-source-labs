# Criar Outro `GridSpec` Interno

Agora criaremos outro `gridspec` interno. Desta vez, usaremos o método `subgridspec` para criar um `gridspec` de 3 por 3 que será um subplot da segunda coluna do `gridspec` externo.

```python
gs01 = gs0[1].subgridspec(3, 3)
```
