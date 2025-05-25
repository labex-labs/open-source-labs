# Definir o localizador e formatador de marcas

Você usará a função `RRuleLocator` para definir o localizador de marcas com base na regra de recorrência que você definiu na etapa anterior. Você também usará a função `DateFormatter` para definir o formatador de marcas.

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```
