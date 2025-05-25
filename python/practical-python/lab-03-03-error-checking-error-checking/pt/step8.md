# Maneira Errada de Capturar Erros (Wrong Way to Catch Errors)

Aqui está a maneira errada de usar exceções.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

Isso captura todos os erros possíveis e pode tornar impossível a depuração quando o código falha por alguma razão que você não esperava (por exemplo, módulo Python desinstalado, etc.).
