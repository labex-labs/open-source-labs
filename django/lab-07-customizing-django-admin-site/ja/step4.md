# 管理画面の見た目をカスタマイズする

明らかに、各管理画面の上部に「Django administration」があるのは不合理です。これはただの置き換えテキストにすぎません。

ただし、Django のテンプレートシステムを使用して変更することができます。Django 管理画面は Django 自身によって動作し、そのインターフェイスは Django 自身のテンプレートシステムを使用しています。

## プロジェクトのテンプレートをカスタマイズする

プロジェクトディレクトリ（`manage.py` が含まれているディレクトリ）に `templates` ディレクトリを作成します。テンプレートは、Django がアクセスできるファイルシステムのどこにでも置くことができます。（Django はサーバーが実行するユーザーとして実行されます。）ただし、プロジェクト内にテンプレートを置くことは、従うべき良い慣例です。

設定ファイル（`mysite/settings.py`、覚えていますか？）を開き、`TEMPLATES` 設定に `DIRS <TEMPLATES-DIRS>` オプションを追加します。

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

`DIRS <TEMPLATES-DIRS>` は、Django テンプレートを読み込む際にチェックするファイルシステムディレクトリのリストです。これは検索パスです。

## テンプレートの整理

静的ファイルと同じように、すべてのテンプレートを 1 つの大きな `templates` ディレクトリにまとめておけば、完全に機能します。ただし、特定のアプリケーションに属するテンプレートは、そのアプリケーションのテンプレートディレクトリ（たとえば `polls/templates`）に配置する方が良いでしょう。これについては、`再利用可能なアプリケーションのチュートリアル </intro/reusable-apps>` で詳細に説明します。

次に、`templates` 内に `admin` というディレクトリを作成し、Django 自体のソースコード内のデフォルトの Django 管理テンプレートディレクトリ（`django/contrib/admin/templates`）からテンプレート `admin/base_site.html` をコピーしてそのディレクトリに貼り付けます。

## Django のソースファイルはどこにあるのか？

システム上の Django のソースファイルがどこにあるかを見つけるのが難しい場合は、次のコマンドを実行します。

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

そして、ファイルを編集して、`{{ site_header|default:_('Django administration') }}`（波括弧も含めて）を適切なサイト名に置き換えます。最終的には次のようなコードセクションになるはずです。

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a><div>
{% endblock %}
```

このアプローチを使用して、テンプレートをオーバーライドする方法を学びます。実際のプロジェクトでは、この特定のカスタマイズをより簡単に行うために、`django.contrib.admin.AdminSite.site_header` 属性を使用する場合が多いでしょう。

このテンプレートファイルには、`{% block branding %}` や `{{ title }}` のようなテキストがたくさん含まれています。`{%` と `{{` タグは Django のテンプレート言語の一部です。Django が `admin/base_site.html` をレンダリングするとき、このテンプレート言語が評価されて最終的な HTML ページが生成されます。これは、`**パブリックインターフェイスビューの作成**` で見たのと同じです。

Django のデフォルトの管理テンプレートのいずれもオーバーライドできることに注意してください。テンプレートをオーバーライドするには、`base_site.html` と同じことを行います。デフォルトのディレクトリからコピーしてカスタムディレクトリに貼り付け、変更を加えます。

## アプリケーションのテンプレートをカスタマイズする

鋭い読者は次のように尋ねるかもしれません。では、`DIRS <TEMPLATES-DIRS>` がデフォルトで空だった場合、Django はどのようにしてデフォルトの管理テンプレートを見つけたのでしょうか？答えは、`APP_DIRS <TEMPLATES-APP_DIRS>` が `True` に設定されているため、Django は各アプリケーションパッケージ内の `templates/` サブディレクトリを自動的に探し、フォールバックとして使用します（忘れないでください。`django.contrib.admin` はアプリケーションです）。

私たちの投票アプリケーションはあまり複雑ではなく、カスタム管理テンプレートが必要ありません。ただし、もっと洗練され、一部の機能に対して Django の標準的な管理テンプレートを変更する必要がある場合、プロジェクトのテンプレートではなく、アプリケーションのテンプレートを変更する方が賢明です。そうすることで、投票アプリケーションを新しいプロジェクトに含めることができ、必要なカスタムテンプレートを見つけることができます。

Django がテンプレートを見つける方法に関する詳細は、`テンプレートの読み込みドキュメント <template-loading>` を参照してください。
