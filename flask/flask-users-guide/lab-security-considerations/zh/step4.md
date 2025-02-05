# 安全标头

浏览器通过识别各种响应标头来控制安全性。建议你在Flask应用程序中检查并使用以下安全标头：

- HTTP严格传输安全（HSTS）：告知浏览器将所有HTTP请求转换为HTTPS。
- 内容安全策略（CSP）：指定各种类型的资源可以从何处加载。
- X-Content-Type-Options：强制浏览器遵守响应内容类型。
- X-Frame-Options：防止外部网站将你的网站嵌入到iframe中。

你可以使用 `Flask-Talisman` 扩展来管理Flask应用程序中的HTTPS和安全标头。
