# 가상 환경 (Virtual Environments)

패키지 설치 문제에 대한 일반적인 해결책은 소위 "가상 환경 (virtual environment)"을 직접 만드는 것입니다. 당연히, 이를 수행하는 "단 하나의 방법"은 없으며, 실제로 여러 경쟁 도구와 기술이 있습니다. 그러나 표준 Python 설치를 사용하고 있다면 다음을 입력해 볼 수 있습니다.

```bash
$ sudo apt install python3-venv
$ python -m venv mypython
bash %
```

잠시 기다리면, 자신만의 작은 Python 설치인 새로운 디렉토리 `mypython`이 생성됩니다. 해당 디렉토리 내에서 `bin/` 디렉토리 (Unix) 또는 `Scripts/` 디렉토리 (Windows) 를 찾을 수 있습니다. 거기에서 찾을 수 있는 `activate` 스크립트를 실행하면 이 Python 버전을 "활성화"하여 셸의 기본 `python` 명령으로 만듭니다. 예를 들어:

```bash
$ source mypython/bin/activate
(mypython) bash %
```

여기에서 자신을 위해 Python 패키지 설치를 시작할 수 있습니다. 예를 들어:

    (mypython) $ python -m pip install pandas
    ...

실험하고 다양한 패키지를 시도하는 목적이라면, 가상 환경이 일반적으로 잘 작동합니다. 반면에, 응용 프로그램을 만들고 특정 패키지 종속성 (dependency) 이 있는 경우, 이는 약간 다른 문제입니다.
