# Headers de Segurança

Os navegadores reconhecem vários headers de resposta para controlar a segurança. É recomendado revisar e usar os seguintes headers de segurança em sua aplicação Flask:

- HTTP Strict Transport Security (HSTS): Informa ao navegador para converter todas as requisições HTTP para HTTPS.
- Content Security Policy (CSP): Especifica de onde vários tipos de recursos podem ser carregados.
- X-Content-Type-Options: Força o navegador a honrar o tipo de conteúdo da resposta.
- X-Frame-Options: Impede que sites externos incorporem seu site em um iframe.

Você pode usar a extensão `Flask-Talisman` para gerenciar HTTPS e headers de segurança em sua aplicação Flask.
