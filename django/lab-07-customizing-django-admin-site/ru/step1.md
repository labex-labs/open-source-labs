# Настройка формы административного интерфейса

Регистрируя модель `Question` с помощью `admin.site.register(Question)`, Django смог построить стандартное представление формы. Часто требуется настроить внешний вид и работу формы административного интерфейса. Для этого нужно передать Django параметры при регистрации объекта.

Рассмотрим, как это работает на примере переупорядочивания полей на форме редактирования. Замените строку `admin.site.register(Question)` на:

Откройте файл `~/project/mysite/polls/admin.py` и измените его так, чтобы он выглядел следующим образом:

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

Вы будете следовать этой схеме — создавать класс модели административного интерфейса и передавать его в качестве второго аргумента в `admin.site.register()` — каждый раз, когда нужно изменить параметры административного интерфейса для модели.

Запустите сервер разработки Django:

```bash
cd ~/project/mysite
python manage.py runserver
```

Откройте `http://127.0.0.1:8000/admin/` в Firefox в рабочей среде и нажмите на ссылку "Questions" (Вопросы). Форма должна выглядеть так:

В данном случае порядок следования полей изменился, и поле "Publication date" (Дата публикации) теперь отображается перед полем "Question" (Вопрос):

![Изменение порядка полей в форме административного интерфейса](../assets/20230908-16-06-41-wiBfnHS8.png)

Этот эффект не очень заметен при наличии только двух полей, но для форм с десятками полей выбор интуитивного порядка является важным аспектом удобства использования.

Если же речь идет о формах с большим количеством полей, вы, возможно, захотите разбить форму на группы полей (fieldset):

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

Первый элемент каждого кортежа в `~django.contrib.admin.ModelAdmin.fieldsets` — это заголовок группы полей. Вот, как наша форма выглядит теперь:

![Форма административного интерфейса с группами полей](../assets/20230908-16-08-19-HOzMJWFG.png)
