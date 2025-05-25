# Desenhar a Linha de Conexão

O quinto passo é desenhar uma linha pontilhada conectando os dois subplots. Criamos um objeto `ConnectionPatch` que conecta a origem do subplot da esquerda à borda direita do subplot da direita. Também salvamos o objeto de patch `con`, que atualizaremos mais tarde na animação.

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```
