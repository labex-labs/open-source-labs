# Definir Normalizador Numérico

Definiremos uma função `number_normalizer()` para mapear todos os tokens numéricos para um marcador de substituição. Isto é usado para redução de dimensionalidade.

```python
def number_normalizer(tokens):
    """Mapear todos os tokens numéricos para um marcador de substituição.

    Para muitas aplicações, tokens que começam com um número não são diretamente
    úteis, mas o facto de tal token existir pode ser relevante. Aplicando esta forma de redução de dimensionalidade, alguns métodos podem ter um desempenho melhor.
    """
    return ("#NUMBER" if token[0].isdigit() else token for token in tokens)
```
