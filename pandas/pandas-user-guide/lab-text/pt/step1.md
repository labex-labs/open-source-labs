# Armazenando Dados Textuais

No pandas, você pode armazenar dados textuais de duas maneiras: usando um array NumPy com `object` dtype ou um tipo de extensão `StringDtype`. Recomendamos o uso de `StringDtype` porque é mais seguro e específico do que o genérico `object` dtype.

```python
import pandas as pd

# create a series with `object` dtype
s1 = pd.Series(["a", "b", "c"], dtype="object")

# create a series with `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
