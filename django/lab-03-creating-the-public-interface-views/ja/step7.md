# URL 名の名前空間化

チュートリアルプロジェクトには `polls` という 1 つのアプリケーションのみがあります。本格的な Django プロジェクトでは、5 つ、10 つ、20 つ以上のアプリケーションがある場合もあります。Django はそれらの間で URL 名をどのように区別するのでしょうか？たとえば、`polls` アプリケーションには `detail` ビューがあり、同じプロジェクト内のブログ用のアプリケーションにもそれがあるかもしれません。`{% url %}` テンプレートタグを使用して URL に対して Django がどのアプリケーションビューを作成するかを知らせるにはどうすればよいでしょうか？

答えは、URLconf に名前空間を追加することです。`polls/urls.py` ファイルで、アプリケーション名前空間を設定するための `app_name` を追加しましょう。

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

次に、`polls/index.html` テンプレートを以下のように変更します。

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

名前空間化された詳細ビューを指すようにします。

```html+django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

![URL 名前空間化の例](../assets/20230908-09-58-22-qkl9l0DT.png)

ビューの作成に慣れたら、**フォーム処理とコードの削減** を読んで、フォーム処理と汎用ビューの基本を学びましょう。
