# Text-Daten speichern

In pandas können Sie Text-Daten auf zwei Arten speichern: indem Sie ein NumPy-Array vom Typ `object` oder einen Erweiterungstyp `StringDtype` verwenden. Wir empfehlen die Verwendung von `StringDtype`, da er sicherer und spezifischer als der generische `object`-DatenTyp ist.

```python
import pandas as pd

# erstelle eine Serie mit dem `object`-DatenTyp
s1 = pd.Series(["a", "b", "c"], dtype="object")

# erstelle eine Serie mit dem `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
