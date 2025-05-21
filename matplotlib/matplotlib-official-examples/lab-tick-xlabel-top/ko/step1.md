# Matplotlib 이해 및 Notebook 생성

이 첫 번째 단계에서는 Matplotlib 에 대해 배우고 시각화 작업을 위한 새로운 Jupyter Notebook 을 생성합니다.

## Matplotlib 란 무엇인가요?

Matplotlib 는 Python 에서 정적, 애니메이션 및 대화형 시각화를 생성하기 위한 포괄적인 라이브러리입니다. 응용 프로그램에 플롯을 포함하기 위한 객체 지향 API 를 제공하며 과학자, 엔지니어 및 데이터 분석가들이 데이터 시각화에 널리 사용합니다.

## 새로운 Notebook 생성

Notebook 의 첫 번째 셀에서 Matplotlib 라이브러리를 가져오겠습니다. 다음 코드를 입력하고 Shift+Enter 를 눌러 셀을 실행합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Check the Matplotlib version
print(f"NumPy version: {np.__version__}")
```

![libraries-imported](../assets/screenshot-20250306-K6iIFfj1@2x.png)

이 코드를 실행하면 다음과 유사한 출력이 표시됩니다.

```
NumPy version: 2.0.0
```

정확한 버전 번호는 환경에 따라 다를 수 있습니다.

이제 Matplotlib 를 가져와 사용할 준비가 되었습니다. `plt`는 플롯을 생성하기 위한 MATLAB 과 유사한 인터페이스를 제공하는 pyplot 모듈에 사용되는 일반적인 별칭입니다.
