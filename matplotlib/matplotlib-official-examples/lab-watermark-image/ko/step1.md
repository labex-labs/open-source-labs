# Jupyter Notebook 생성 및 필수 라이브러리 가져오기

노트북의 첫 번째 셀에 다음 코드를 입력하여 필요한 라이브러리를 가져옵니다.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
```

각 라이브러리가 수행하는 작업을 이해해 보겠습니다.

- `matplotlib.pyplot` (별칭 `plt`): matplotlib 을 MATLAB 처럼 작동하게 해주는 함수의 모음으로, 플롯을 생성하기 위한 편리한 인터페이스를 제공합니다.
- `numpy` (별칭 `np`): Python 에서 과학적 계산을 위한 기본 패키지로, 데이터 조작에 사용합니다.
- `matplotlib.cbook`: 샘플 데이터를 가져오는 함수를 포함하여 matplotlib 에 대한 유틸리티 함수의 모음입니다.
- `matplotlib.image`: matplotlib 에서 이미지 관련 기능을 위한 모듈로, 이미지를 읽고 표시하는 데 사용합니다.

노트북 상단의 "Run" 버튼을 클릭하거나 Shift+Enter 를 눌러 셀을 실행합니다.

![libraries-imported](../assets/screenshot-20250306-18gJ6FRZ@2x.png)

이 셀 실행은 모든 라이브러리가 성공적으로 가져와졌음을 나타내며, 어떤 출력도 없이 완료되어야 합니다.
