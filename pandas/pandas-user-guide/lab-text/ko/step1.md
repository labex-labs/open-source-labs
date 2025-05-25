# 텍스트 데이터 저장

pandas 에서는 텍스트 데이터를 두 가지 방법으로 저장할 수 있습니다: `object` dtype NumPy 배열을 사용하거나 `StringDtype` 확장 타입을 사용하는 것입니다. 일반적인 `object` dtype 보다 안전하고 더 구체적이므로 `StringDtype`을 사용하는 것이 좋습니다.

```python
import pandas as pd

# create a series with `object` dtype
s1 = pd.Series(["a", "b", "c"], dtype="object")

# create a series with `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
