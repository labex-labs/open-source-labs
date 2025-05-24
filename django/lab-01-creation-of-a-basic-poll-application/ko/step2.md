# 프로젝트 생성

Django 를 처음 사용하는 경우, 몇 가지 초기 설정을 처리해야 합니다. 즉, Django `project` (Django 인스턴스에 대한 설정 모음, 데이터베이스 구성, Django 관련 옵션 및 애플리케이션별 설정을 포함) 을 설정하는 일부 코드를 자동 생성해야 합니다.

명령줄에서 코드를 저장할 디렉토리로 `cd`한 다음 다음 명령을 실행합니다.

```bash
cd ~/project
django-admin startproject mysite
```

이렇게 하면 현재 디렉토리에 `mysite` 디렉토리가 생성됩니다.

`startproject`가 생성한 내용을 살펴보겠습니다.

```plaintext
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

이 파일들은 다음과 같습니다.

- 외부 `mysite/` 루트 디렉토리는 프로젝트의 컨테이너입니다. 이름은 Django 에 중요하지 않으며 원하는 대로 이름을 변경할 수 있습니다.
- `manage.py`: 이 Django 프로젝트와 다양한 방식으로 상호 작용할 수 있는 명령줄 유틸리티입니다.
- 내부 `mysite/` 디렉토리는 프로젝트의 실제 Python 패키지입니다. 이 이름은 내부의 모든 것을 가져오는 데 사용해야 하는 Python 패키지 이름입니다 (예: `mysite.urls`).
- `mysite/__init__.py`: 이 디렉토리를 Python 패키지로 간주해야 함을 Python 에 알리는 빈 파일입니다.
- `mysite/settings.py`: 이 Django 프로젝트의 설정/구성입니다.
- `mysite/urls.py`: 이 Django 프로젝트의 URL 선언; Django 기반 사이트의 "목차"입니다.
- `mysite/asgi.py`: ASGI 호환 웹 서버가 프로젝트를 제공하기 위한 진입점입니다.
- `mysite/wsgi.py`: WSGI 호환 웹 서버가 프로젝트를 제공하기 위한 진입점입니다.
