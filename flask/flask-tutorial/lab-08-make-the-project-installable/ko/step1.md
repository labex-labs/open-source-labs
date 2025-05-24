# 프로젝트 설명

먼저, 프로젝트를 설명하고 빌드하는 방법을 정의하기 위해 `pyproject.toml` 파일을 생성해야 합니다.

`pyproject.toml` 파일은 다음과 같아야 합니다.

```toml
# pyproject.toml

[project]
name = "flaskr" # 프로젝트 이름
version = "1.0.0" # 프로젝트 버전
dependencies = [
    "flask", # 프로젝트 종속성
]

[build-system]
requires = ["setuptools"] # 필요한 빌드 시스템
build-backend = "setuptools.build_meta" # 백엔드 빌드 시스템
```
