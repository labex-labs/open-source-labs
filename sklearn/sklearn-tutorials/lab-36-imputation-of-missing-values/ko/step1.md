# 필요한 모듈 가져오기

먼저, scikit-learn 라이브러리에서 필요한 모듈을 가져와야 합니다. 단변량 특징 임퓨테이션에는 `SimpleImputer` 클래스를, 다변량 특징 임퓨테이션에는 `IterativeImputer` 클래스를 사용할 것입니다.

```python
import numpy as np
from sklearn.impute import SimpleImputer, IterativeImputer
```
