# Nullable 정수 배열 구성

Pandas 는 nullable 정수 배열을 생성하기 위해 `IntegerArray` 클래스를 제공합니다. `IntegerArray`를 생성하는 것부터 시작해 보겠습니다.

```python
# Import necessary libraries
import pandas as pd
import numpy as np

# Create an IntegerArray with missing values
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```

배열을 생성할 때 문자열 별칭 "Int64"를 사용하여 데이터 유형을 지정할 수도 있습니다. 모든 NA 와 유사한 값은 `pandas.NA`로 대체됩니다.

```python
# Create an IntegerArray using the "Int64" string alias
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```
