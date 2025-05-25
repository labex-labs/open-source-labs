# Abordagem um Pouco Melhor (Somewhat Better Approach)

Se você vai capturar todos os erros, esta é uma abordagem mais sensata.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
```

Ele relata uma razão específica para a falha. É quase sempre uma boa ideia ter algum mecanismo para visualizar/relatar erros quando você escreve código que captura todas as exceções possíveis.

Em geral, no entanto, é melhor capturar o erro da forma mais restrita possível. Capture apenas os erros que você realmente pode tratar. Deixe outros erros passarem – talvez algum outro código possa tratá-los.
