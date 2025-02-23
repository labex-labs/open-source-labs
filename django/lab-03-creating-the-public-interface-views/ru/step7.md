# Именование URL-адресов с учетом пространства имен

Проект-туториал имеет только одно приложение, `polls`. В реальных проектах на Django может быть пять, десять, двадцать приложений или больше. Как Django различает имена URL-адресов между ними? Например, приложение `polls` имеет представление `detail`, и такое же представление может быть в приложении на том же проекте, которое посвящено блогу. Как заставить Django знать, какое представление приложения создать для URL-адреса при использовании тега шаблона `{% url %}`?

Ответ - добавить пространства имен в конфигурацию URL. В файле `polls/urls.py` добавьте `app_name`, чтобы установить пространство имен приложения:

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    # пример: /polls/
    path("", views.index, name="index"),
    # пример: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # пример: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # пример: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Теперь измените шаблон `polls/index.html` из:

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

на ссылку на представление с учетом пространства имен:

```html+django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

![Пример именования URL-адресов с учетом пространства имен](../assets/20230908-09-58-22-qkl9l0DT.png)

Когда вы будете уверены в написании представлений, прочитайте раздел **Обработка форм и сокращение нашего кода**, чтобы узнать основы обработки форм и обобщенных представлений.
