# 필요한 파일 포함

setuptools 빌드 백엔드는 프로젝트에 비 Python 파일을 포함하기 위해 `MANIFEST.in`이라는 다른 파일이 필요합니다.

다음 내용으로 `MANIFEST.in`을 생성합니다.

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

이것은 빌드에 `static` 및 `templates` 디렉토리의 모든 내용과 `schema.sql` 파일을 복사하도록 지시하는 동시에 모든 바이트코드 파일을 제외합니다.
