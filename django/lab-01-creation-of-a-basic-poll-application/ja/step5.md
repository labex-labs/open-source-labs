# 最初のビューを書く

最初のビューを書いてみましょう。`polls/views.py` ファイルを開き、次のPythonコードを入力します。

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

これはDjangoで可能な最もシンプルなビューです。ビューを呼び出すには、それをURLにマッピングする必要があります。このためにはURLconfが必要です。

投票アプリケーションのディレクトリにURLconfを作成するには、`urls.py` という名前のファイルを作成します。アプリケーションのディレクトリは次のようになります。

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

`polls/urls.py` ファイルに次のコードを記述します。

```python
from django.urls import path

from. import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

次のステップは、ルートURLconfを `polls.urls` モジュールに向けることです。`mysite/urls.py` で、`django.urls.include` のインポートを追加し、`urlpatterns` リストに `~django.urls.include` を挿入します。このようになります。

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

`~django.urls.include` 関数は、他のURLconfを参照するために使用します。Djangoが `~django.urls.include` に遭遇すると、その時点までに一致したURLの部分を切り捨て、残りの文字列を含まれるURLconfに送り、さらなる処理を行います。

`~django.urls.include` の背後にある考え方は、URLを簡単にプラグアンドプレイできるようにすることです。投票アプリケーションは独自のURLconf（`polls/urls.py`）にあるため、`/polls/` の下、`/fun_polls/` の下、`/content/polls/` の下、またはその他の任意のパスルートの下に配置でき、アプリケーションは依然として機能します。

> `~django.urls.include()` を使用するタイミング
> 他のURLパターンを含める場合、常に `include()` を使用する必要があります。このルールの唯一の例外は `admin.site.urls` です。

これで、`index` ビューがURLconfに接続されました。次のコマンドでそれが正常に動作することを確認します。

```bash
python manage.py runserver 0.0.0.0:8080
```

ブラウザで <http://<url>/polls/> にアクセスすると、`index` ビューで定義した "_Hello, world. You're at the polls index._" というテキストが表示されるはずです。

![Django URLconf structure](../assets/20230907-13-51-48-aOKKfCBX.png)

`~django.urls.path` 関数には4つの引数が渡されます。必須の引数は2つで、`route` と `view` です。オプションの引数も2つで、`kwargs` と `name` です。この時点で、これらの引数が何のためのものかを見直しておく価値があります。

## `~django.urls.path` 引数: `route`

`route` はURLパターンを含む文字列です。リクエストを処理する際、Djangoは `urlpatterns` の最初のパターンから始まり、リストを下に向かって進み、要求されたURLと各パターンを比較して、一致するものが見つかるまで続けます。

パターンはGETやPOSTパラメータ、ドメイン名を検索しません。たとえば、`https://www.example.com/myapp/` へのリクエストでは、URLconfは `myapp/` を探します。`https://www.example.com/myapp/?page=3` へのリクエストでも、URLconfは `myapp/` を探します。

## `~django.urls.path` 引数: `view`

Djangoが一致するパターンを見つけると、指定されたビュー関数に `~django.http.HttpRequest` オブジェクトを第1引数として、ルートからの任意の「キャプチャされた」値をキーワード引数として渡して呼び出します。この例については少し後で説明します。

## `~django.urls.path` 引数: `kwargs`

任意のキーワード引数を辞書形式で対象のビューに渡すことができます。このチュートリアルではDjangoのこの機能を使用しません。

## `~django.urls.path` 引数: `name`

URLに名前を付けることで、Django内の他の場所、特にテンプレート内から明確に参照できるようになります。この強力な機能により、プロジェクトのURLパターンをグローバルに変更する際に、単一のファイルのみを編集すれば済むようになります。
