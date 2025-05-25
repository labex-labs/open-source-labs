# Definir a regra de recorrência

Você definirá marcas de data personalizadas a cada 5ª Páscoa. Para fazer isso, você precisa definir a regra de recorrência usando a função `rrulewrapper`.

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```
