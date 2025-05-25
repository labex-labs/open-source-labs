# Criar o `GridSpec` Interno

Agora, criaremos o `gridspec` interno. Usaremos o método `GridSpecFromSubplotSpec` para criar um `gridspec` de 3 por 3 que será um subplot do `gridspec` externo.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
