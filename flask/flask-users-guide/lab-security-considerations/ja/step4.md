# セキュリティヘッダー

ブラウザは、セキュリティを制御するためにさまざまな応答ヘッダーを認識します。Flask アプリケーションでは、次のセキュリティヘッダーを見直して使用することをお勧めします。

- HTTP Strict Transport Security (HSTS)：ブラウザに対してすべての HTTP 要求を HTTPS に変換するように指示します。
- Content Security Policy (CSP)：さまざまな種類のリソースをどこから読み込むことができるかを指定します。
- X-Content-Type-Options：ブラウザに応答コンテンツタイプを尊重するように強制します。
- X-Frame-Options：外部サイトが iframe であなたのサイトを埋め込むのを防ぎます。

Flask アプリケーションで HTTPS とセキュリティヘッダーを管理するには、`Flask-Talisman` 拡張機能を使用できます。
