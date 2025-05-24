# *app*의 모양과 느낌 사용자 정의하기

먼저, `polls` 디렉토리 안에 `static`이라는 디렉토리를 생성합니다. Django 는 `polls/templates/` 내에서 템플릿을 찾는 방식과 유사하게, 거기에서 정적 파일 (static files) 을 찾습니다.

Django 의 `STATICFILES_FINDERS` 설정에는 다양한 소스에서 정적 파일을 찾는 방법을 아는 파인더 (finder) 목록이 포함되어 있습니다. 기본값 중 하나는 `AppDirectoriesFinder`로, 방금 생성한 `polls`와 같이 각 `INSTALLED_APPS`에서 "static" 하위 디렉토리를 찾습니다. 관리자 사이트 (admin site) 는 정적 파일에 대해 동일한 디렉토리 구조를 사용합니다.

방금 생성한 `static` 디렉토리 내에 `polls`라는 다른 디렉토리를 생성하고, 그 안에 `style.css`라는 파일을 생성합니다. 즉, 스타일시트는 `polls/static/polls/style.css`에 있어야 합니다. `AppDirectoriesFinder` 정적 파일 파인더가 작동하는 방식 때문에, Django 에서 이 정적 파일을 템플릿 경로를 참조하는 방식과 유사하게 `polls/style.css`로 참조할 수 있습니다.

## 정적 파일 네임스페이싱 (Static file namespacing)

템플릿과 마찬가지로, 정적 파일을 `polls/static`에 직접 넣을 수도 있지만 (다른 `polls` 하위 디렉토리를 생성하는 대신), 실제로 좋지 않은 생각입니다. Django 는 이름이 일치하는 첫 번째 정적 파일을 선택하며, _다른_ 애플리케이션에 동일한 이름의 정적 파일이 있는 경우 Django 는 이를 구별할 수 없습니다. 우리는 Django 가 올바른 파일을 가리키도록 해야 하며, 이를 보장하는 가장 좋은 방법은 *네임스페이싱 (namespacing)*하는 것입니다. 즉, 해당 정적 파일을 애플리케이션 자체의 이름을 딴 _다른_ 디렉토리 안에 넣는 것입니다.

다음 코드를 해당 스타일시트 (`polls/static/polls/style.css`) 에 넣습니다.

```css
li a {
  color: green;
}
```

다음으로, `polls/templates/polls/index.html`의 맨 위에 다음을 추가합니다.

```html+django
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

`{% static %}` 템플릿 태그는 정적 파일의 절대 URL 을 생성합니다.

개발을 위해 해야 할 일은 이게 전부입니다.

서버를 시작하거나 (이미 실행 중인 경우 다시 시작):

```bash
python manage.py runserver 0.0.0.0:8080
```

**Web 8080** 탭을 다시 로드하면 질문 링크가 녹색으로 표시되어 (Django 스타일!) 스타일시트가 제대로 로드되었음을 의미합니다.

![green question links example](../assets/20230908-15-29-11-ztyI1umP.png)
