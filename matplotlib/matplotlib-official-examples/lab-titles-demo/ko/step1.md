# 기본 제목 위치를 사용한 기본 플로팅

이 단계에서는 간단한 선 플롯을 생성하고 Matplotlib 의 기본 위치인 가운데 정렬된 제목을 추가합니다.

## Jupyter Notebook 생성

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 Jupyter Notebook 에 액세스합니다.

![click-notebook](https://file.labex.io/images/click-notebook.png)

Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한 사항으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

랩 중에 문제가 발생하면 Labby 에게 도움을 요청하십시오. 세션 후 피드백을 제공하여 문제를 신속하게 해결할 수 있도록 해주세요.

## Matplotlib 가져오기

이제 Matplotlib 라이브러리를 가져오는 것으로 시작해 보겠습니다. 노트북의 첫 번째 셀에 다음 코드를 입력하고 Shift+Enter 를 눌러 실행합니다.

```python
import matplotlib.pyplot as plt
```

이 코드는 Matplotlib 에서 pyplot 모듈을 가져와서 `plt`라는 별칭을 할당합니다. 이는 일반적인 관례입니다.

## 간단한 플롯 생성

다음으로, 기본 선 플롯을 생성해 보겠습니다. 새 셀에 다음 코드를 입력하고 실행합니다.

```python
plt.figure(figsize=(8, 5))  # 특정 크기의 figure 생성
plt.plot(range(10))         # 0 부터 9 까지의 숫자 플롯
plt.grid(True)              # 가독성을 위해 그리드 추가
plt.show()                  # 플롯 표시
```

출력에 0 부터 9 까지의 값이 표시된 간단한 선 플롯이 표시됩니다.

![line-plot](../assets/screenshot-20250306-g5knGobR@2x.png)

## 기본 (가운데 정렬) 제목 추가

이제 플롯에 제목을 추가해 보겠습니다. 제목의 기본 위치는 플롯 상단의 가운데입니다. 새 셀에 다음 코드를 입력합니다.

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('My First Matplotlib Plot')  # 가운데 정렬된 제목 추가
plt.show()
```

![line-plot-with-title](../assets/screenshot-20250306-XMODABB2@2x.png)

셀을 실행하면 상단에 가운데 정렬된 제목이 있는 플롯이 표시됩니다.

추가 매개변수 없이 `title()` 함수를 사용하면 제목이 가운데에 배치됩니다. 이것이 기본 위치입니다.
