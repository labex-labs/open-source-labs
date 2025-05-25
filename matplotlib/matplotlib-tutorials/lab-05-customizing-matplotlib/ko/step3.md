# matplotlibrc 파일 변경하기

`matplotlibrc` 파일은 Matplotlib 에서 모든 종류의 속성을 사용자 정의할 수 있도록 해주는 구성 파일입니다. 그림 크기, 선 너비, 색상, 글꼴 등과 같은 속성의 기본값을 제어합니다. `matplotlibrc` 파일을 수정하여 Matplotlib 을 선호도에 따라 사용자 정의할 수 있습니다. 이 파일은 시스템의 여러 위치에 있을 수 있으며, Matplotlib 은 특정 순서로 파일을 찾습니다. `matplotlibrc` 파일이 발견되면 다른 설정보다 우선합니다. 현재 활성 `matplotlibrc` 파일의 경로를 표시하려면 `matplotlib.matplotlib_fname()` 함수를 사용할 수 있습니다.
