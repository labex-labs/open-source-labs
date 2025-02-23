# HTML で CSS ファイルをリンクする

次に、HTML テンプレートで CSS ファイルをリンクする必要があります。Flask は自動的に静的ファイルを提供する `static` ビューを追加します。`base.html` テンプレートで `url_for` 関数を使用して CSS ファイルをリンクできます。

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```
