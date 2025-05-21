# 소개

데이터 시각화에서 로고, 워터마크 또는 기타 이미지 요소를 플롯에 추가하고 싶을 때가 있습니다. 이 튜토리얼에서는 플롯 콘텐츠 앞에 이미지를 배치하고 반투명하게 만들어 Matplotlib 플롯에 이미지를 오버레이하는 방법을 보여줍니다.

`matplotlib.figure.Figure` 클래스의 `figimage` 메서드를 사용하여 플롯에 이미지를 배치하는 방법과 `matplotlib.image` 모듈의 `imread` 메서드를 사용하여 이미지 데이터를 로드하는 방법을 배우게 됩니다.

이 튜토리얼을 마치면 브랜딩, 워터마킹 또는 데이터 프레젠테이션의 시각적 매력을 향상시키는 데 유용한 사용자 정의 이미지 오버레이를 사용하여 전문적인 모습의 시각화를 만들 수 있습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위한 Jupyter Notebook 에 액세스하십시오.

![click-notebook](https://file.labex.io/images/click-notebook.png)
때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화할 수 없습니다.

학습 중에 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 즉시 해결해 드리겠습니다.
