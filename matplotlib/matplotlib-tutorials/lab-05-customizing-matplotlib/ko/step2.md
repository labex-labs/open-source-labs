# 스타일 시트 사용하기

플롯의 시각적 모양을 변경하는 또 다른 방법은 스타일 시트에서 rcParams 를 설정하고 `matplotlib.style.use`를 사용하여 해당 스타일 시트를 가져오는 것입니다. 스타일 시트는 플롯의 스타일에 관련된 rcParams 집합을 포함하는 파일입니다. Matplotlib 은 사용할 수 있는 여러 사전 정의된 스타일을 제공합니다. 예를 들어, "ggplot" 스타일은 R 의 ggplot 라이브러리의 미학을 에뮬레이션합니다. 다음과 같이 스타일 시트를 적용할 수 있습니다.

```python
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')
```

또한 사용자 정의 스타일을 정의하고 스타일 시트의 경로 또는 URL 로 `.style.use`를 호출하여 사용할 수도 있습니다.
