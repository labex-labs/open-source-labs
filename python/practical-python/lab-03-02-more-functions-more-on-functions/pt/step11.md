# Passagem de Argumentos (Argument Passing)

Quando você chama uma função, as variáveis de argumento são nomes que se referem aos valores passados. Esses valores NÃO são cópias. Se tipos de dados mutáveis são passados (por exemplo, listas, dicionários), eles podem ser modificados _in-place_ (no local).

```python
def foo(items):
    items.append(42)    # Modifica o objeto de entrada

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Ponto chave: Funções não recebem uma cópia dos argumentos de entrada.**
