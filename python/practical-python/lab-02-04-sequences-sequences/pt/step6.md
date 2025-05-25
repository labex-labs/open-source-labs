# Declaração break (break statement)

Você pode usar a declaração `break` para sair de um laço antecipadamente.

```python
for name in namelist:
    if name == 'Jake':
        break
    ...
    ...
statements
```

Quando a declaração `break` é executada, ela sai do laço e passa para as próximas `statements`. A declaração `break` se aplica apenas ao laço mais interno. Se este laço estiver dentro de outro laço, ele não interromperá o laço externo.
