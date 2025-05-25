# Criar uma função de formatação

Criamos uma função de formatação que determina o rótulo da marca de escala (tick label) a partir do valor na marca de escala. Se o valor da marca de escala for um inteiro no intervalo de `xs`, o rótulo correspondente da lista `labels` é retornado. Caso contrário, uma string vazia é retornada.

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
