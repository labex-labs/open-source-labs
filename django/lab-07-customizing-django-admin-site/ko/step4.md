# 관리자 모양 및 느낌 커스터마이징

분명히, 각 관리자 페이지 상단에 "Django administration"이 있는 것은 터무니없습니다. 이는 단지 자리 표시자 텍스트일 뿐입니다.

하지만 Django 의 템플릿 시스템을 사용하여 변경할 수 있습니다. Django 관리자는 Django 자체에서 제공되며, 해당 인터페이스는 Django 자체의 템플릿 시스템을 사용합니다.

## _프로젝트_ 템플릿 커스터마이징

프로젝트 디렉토리 ( `manage.py`가 포함된 디렉토리) 에 `templates` 디렉토리를 만듭니다. 템플릿은 Django 가 액세스할 수 있는 파일 시스템의 어느 곳에나 있을 수 있습니다. (Django 는 서버가 실행되는 사용자로 실행됩니다.) 그러나 프로젝트 내에 템플릿을 유지하는 것이 좋은 관례입니다.

설정 파일 ( `mysite/settings.py` 기억하세요) 을 열고 `TEMPLATES` 설정에 `DIRS <TEMPLATES-DIRS>` 옵션을 추가합니다.

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

`DIRS <TEMPLATES-DIRS>`는 Django 템플릿을 로드할 때 확인할 파일 시스템 디렉토리 목록입니다. 즉, 검색 경로입니다.

## 템플릿 구성

정적 파일과 마찬가지로 모든 템플릿을 하나의 큰 템플릿 디렉토리에 함께 넣을 수 있으며, 완벽하게 작동합니다. 그러나 특정 애플리케이션에 속하는 템플릿은 프로젝트의 템플릿 ( `templates`) 이 아닌 해당 애플리케이션의 템플릿 디렉토리 (예: `polls/templates`) 에 배치해야 합니다. `reusable apps tutorial </intro/reusable-apps>`에서 이렇게 하는 *이유*에 대해 자세히 설명합니다.

이제 `templates` 내에 `admin`이라는 디렉토리를 만들고 Django 자체의 소스 코드 ( `django/contrib/admin/templates`) 의 기본 Django 관리자 템플릿 디렉토리 내에서 `admin/base_site.html` 템플릿을 해당 디렉토리로 복사합니다.

## Django 소스 파일은 어디에 있습니까?

시스템에서 Django 소스 파일의 위치를 찾는 데 어려움이 있는 경우 다음 명령을 실행합니다.

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

그런 다음 파일을 편집하고 `{{ site_header|default:_('Django administration') }}`(중괄호 포함) 을 원하는 대로 사이트 이름으로 바꿉니다. 다음과 같은 코드 섹션이 생성되어야 합니다.

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a><div>
{% endblock %}
```

이 접근 방식을 사용하여 템플릿을 재정의하는 방법을 가르칩니다. 실제 프로젝트에서는 이 특정 사용자 지정을 더 쉽게 수행하기 위해 `django.contrib.admin.AdminSite.site_header` 속성을 사용할 것입니다.

이 템플릿 파일에는 `{% block branding %}` 및 `{{ title }}`와 같은 많은 텍스트가 포함되어 있습니다. `{%` 및 `{{` 태그는 Django 의 템플릿 언어의 일부입니다. Django 가 `admin/base_site.html`을 렌더링하면 이 템플릿 언어가 `**Creating the Public Interface Views**`에서 본 것처럼 최종 HTML 페이지를 생성하기 위해 평가됩니다.

Django 의 기본 관리자 템플릿은 재정의할 수 있습니다. 템플릿을 재정의하려면 `base_site.html`과 동일한 작업을 수행합니다. 즉, 기본 디렉토리에서 사용자 지정 디렉토리로 복사하고 변경합니다.

## _애플리케이션_ 템플릿 커스터마이징

예리한 독자들은 질문할 것입니다. 하지만 `DIRS <TEMPLATES-DIRS>`가 기본적으로 비어 있었다면 Django 는 어떻게 기본 관리자 템플릿을 찾았습니까? 대답은 `APP_DIRS <TEMPLATES-APP_DIRS>`가 `True`로 설정되어 있으므로 Django 는 대체로 사용할 각 애플리케이션 패키지 내에서 `templates/` 하위 디렉토리를 자동으로 찾습니다 ( `django.contrib.admin`이 애플리케이션이라는 것을 잊지 마세요).

Poll 애플리케이션은 그다지 복잡하지 않으며 사용자 지정 관리자 템플릿이 필요하지 않습니다. 그러나 더 정교해지고 일부 기능에 대해 Django 의 표준 관리자 템플릿을 수정해야 하는 경우 *프로젝트*의 템플릿이 아닌 *애플리케이션*의 템플릿을 수정하는 것이 더 합리적입니다. 그렇게 하면 모든 새 프로젝트에 Poll 애플리케이션을 포함하고 필요한 사용자 지정 템플릿을 찾을 수 있습니다.

Django 가 템플릿을 찾는 방법에 대한 자세한 내용은 `template loading documentation <template-loading>`을 참조하십시오.
