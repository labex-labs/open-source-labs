# Declaração continue (continue statement)

Para pular um elemento e passar para o próximo, use a declaração `continue`.

```python
for line in lines:
    if line == '\n':    # Skip blank lines
        continue
    # More statements
    ...
```

Isso é útil quando o item atual não é de interesse ou precisa ser ignorado no processamento.
