# Verificação de Tipos (Type Checking)

Como verificar se um objeto é de um tipo específico.

```python
if isinstance(a, list):
    print('a is a list')
```

Verificando um entre muitos tipos possíveis.

```python
if isinstance(a, (list,tuple)):
    print('a is a list or tuple')
```

\*Cuidado: Não exagere na verificação de tipos. Isso pode levar a uma complexidade excessiva no código. Geralmente, você só faria isso se isso impedisse erros comuns cometidos por outras pessoas que usam seu código.
