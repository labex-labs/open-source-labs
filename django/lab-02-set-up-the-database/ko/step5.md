# Django Admin 소개

직원이나 고객이 콘텐츠를 추가, 변경 및 삭제할 수 있도록 관리자 사이트를 생성하는 것은 창의성이 많이 필요하지 않은 지루한 작업입니다. 이러한 이유로 Django 는 모델에 대한 관리자 인터페이스 생성을 완전히 자동화합니다.

Django 는 "콘텐츠 게시자"와 "공개" 사이트 간에 매우 명확한 구분이 있는 뉴스룸 환경에서 작성되었습니다. 사이트 관리자는 시스템을 사용하여 뉴스 기사, 이벤트, 스포츠 점수 등을 추가하고 해당 콘텐츠는 공개 사이트에 표시됩니다. Django 는 사이트 관리자가 콘텐츠를 편집할 수 있는 통합 인터페이스를 만드는 문제를 해결합니다.

관리자는 사이트 방문자가 사용하도록 설계되지 않았습니다. 사이트 관리자를 위한 것입니다.

## 관리자 사용자 생성

먼저 관리자 사이트에 로그인할 수 있는 사용자를 생성해야 합니다. 다음 명령을 실행합니다.

```bash
python manage.py createsuperuser
```

원하는 사용자 이름을 입력하고 Enter 키를 누릅니다.

```plaintext
Username: admin
```

그런 다음 원하는 이메일 주소를 입력하라는 메시지가 표시됩니다.

```plaintext
Email address: admin@example.com
```

마지막 단계는 비밀번호를 입력하는 것입니다. 비밀번호를 두 번 입력하라는 메시지가 표시되며, 두 번째는 첫 번째의 확인입니다.

```plaintext
Password: 12345678
Password (again): 12345678

This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## 개발 서버 시작

Django 관리자 사이트는 기본적으로 활성화되어 있습니다. 개발 서버를 시작하고 탐색해 보겠습니다.

서버가 실행 중이지 않은 경우 다음과 같이 시작합니다.

```bash
python manage.py runserver
```

이제 **VNC** 탭에서 웹 브라우저를 열고 로컬 도메인의 "/admin/"으로 이동합니다. 예를 들어, `http://127.0.0.1:8000/admin/`. 관리자의 로그인 화면이 표시됩니다.

![Django admin login screen](../assets/20230907-14-31-50-SvkJF8K8.png)

`translation </topics/i18n/translation>`이 기본적으로 켜져 있으므로, `LANGUAGE_CODE`를 설정하면 로그인 화면이 지정된 언어로 표시됩니다 (Django 에 적절한 번역이 있는 경우).

## 관리자 사이트 입력

이제 이전 단계에서 생성한 슈퍼유저 계정으로 로그인해 보십시오. Django 관리자 인덱스 페이지가 표시됩니다.

![Django admin index page](../assets/admin02.png)

그룹 및 사용자와 같이 편집 가능한 콘텐츠가 몇 가지 표시됩니다. 이는 Django 에서 제공하는 인증 프레임워크인 `django.contrib.auth`에서 제공합니다.

## 설문 앱을 관리자에서 수정 가능하게 만들기

하지만 설문 앱은 어디에 있습니까? 관리자 인덱스 페이지에 표시되지 않습니다.

해야 할 일이 하나 더 있습니다. 관리자에게 `Question` 객체에 관리자 인터페이스가 있음을 알려야 합니다. 이렇게 하려면 `polls/admin.py` 파일을 열고 다음과 같이 편집합니다.

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

## 무료 관리자 기능 탐색

이제 `Question`을 등록했으므로 Django 는 관리자 인덱스 페이지에 표시해야 함을 알고 있습니다.

![Django admin index page, now with polls displayed](../assets/admin03t.png)

"Questions"를 클릭합니다. 이제 질문에 대한 "변경 목록" 페이지에 있습니다. 이 페이지는 데이터베이스의 모든 질문을 표시하고 변경할 질문을 선택할 수 있도록 합니다. 앞서 생성한 "What's up?" 질문이 있습니다.

![Polls change list page](../assets/admin04t.png)

"What's up?" 질문을 클릭하여 편집합니다.

![Editing a poll question](../assets/20230907-14-33-49-XWeEgAXl.png)

여기서 주목할 사항은 다음과 같습니다.

- 양식은 `Question` 모델에서 자동으로 생성됩니다.
- 서로 다른 모델 필드 유형 (`~django.db.models.DateTimeField`, `~django.db.models.CharField`) 은 적절한 HTML 입력 위젯에 해당합니다. 각 필드 유형은 Django 관리자에서 자체적으로 표시하는 방법을 알고 있습니다.
- 각 `~django.db.models.DateTimeField`은 무료 JavaScript 바로 가기를 얻습니다. 날짜는 "Today" 바로 가기 및 캘린더 팝업을 얻고, 시간은 "Now" 바로 가기 및 일반적으로 입력된 시간을 나열하는 편리한 팝업을 얻습니다.

페이지 하단에는 몇 가지 옵션이 있습니다.

- 저장 - 변경 사항을 저장하고 이 유형의 객체에 대한 변경 목록 페이지로 돌아갑니다.
- 저장 및 계속 편집 - 변경 사항을 저장하고 이 객체에 대한 관리자 페이지를 다시 로드합니다.
- 저장 및 다른 항목 추가 - 변경 사항을 저장하고 이 유형의 객체에 대한 새 빈 양식을 로드합니다.
- 삭제 - 삭제 확인 페이지를 표시합니다.

"게시 날짜"의 값이 **기본 설문 애플리케이션 생성**에서 질문을 생성했을 때의 시간과 일치하지 않으면, `TIME_ZONE` 설정을 올바르게 설정하는 것을 잊었을 가능성이 큽니다. 변경하고 페이지를 다시 로드하여 올바른 값이 나타나는지 확인하십시오.

"Today" 및 "Now" 바로 가기를 클릭하여 "게시 날짜"를 변경합니다. 그런 다음 오른쪽 상단에서 "History"를 클릭합니다. Django 관리자를 통해 이 객체에 대해 수행된 모든 변경 사항을 타임스탬프 및 변경을 수행한 사용자와 함께 나열하는 페이지가 표시됩니다.

![History page for question object](../assets/admin06t.png)

모델 API 에 익숙해지고 관리자 사이트에 익숙해지면, 설문 앱에 더 많은 보기를 추가하는 방법을 배우려면 **공개 인터페이스 보기 생성**을 읽어보십시오.
