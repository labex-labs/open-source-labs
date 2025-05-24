# Criando uma Rota Básica

Rotas (Routes) no Flask definem os padrões de URL para sua aplicação. Vamos criar uma rota básica que exibe a mensagem "Hello, World!".

1. Adicione o seguinte código ao seu arquivo `app.py`:

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. Salve o arquivo.
