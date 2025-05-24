# 애플리케이션 빌드

먼저, 애플리케이션을 위한 휠 (wheel) 파일을 생성해야 합니다. 이를 위해 `build` 도구를 사용할 것입니다. 아직 설치하지 않았다면 pip 를 사용하여 `build` 도구를 설치하십시오:

```bash
# 빌드 도구 설치
pip install build
```

이제 `build` 도구를 사용하여 휠 파일을 생성합니다:

```bash
# 휠 파일 빌드
python -m build --wheel
```

휠 파일은 `dist` 디렉토리에 `flaskr-1.0.0-py3-none-any.whl`과 같은 이름으로 생성됩니다.
