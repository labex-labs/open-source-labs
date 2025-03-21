# Security Headers

Браузеры распознают различные заголовки ответов для управления безопасностью. Рекомендуется проверить и использовать следующие заголовки безопасности в вашем приложении Flask:

- HTTP Strict Transport Security (HSTS): сообщает браузеру преобразовывать все HTTP-запросы в HTTPS.
- Content Security Policy (CSP): задает, откуда можно загружать различные типы ресурсов.
- X-Content-Type-Options: заставляет браузер учитывать тип содержимого ответа.
- X-Frame-Options: предотвращает встраивание вашего сайта на внешние сайты в iframe.

Вы можете использовать расширение `Flask-Talisman` для управления HTTPS и заголовками безопасности в вашем приложении Flask.
