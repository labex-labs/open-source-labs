# Adicionando Templates HTML

Flask usa templates Jinja2 para gerar conteúdo HTML. Vamos criar um arquivo de template e renderizá-lo em nossa rota.

1. Crie um novo diretório em seu projeto chamado `templates`.

2. Dentro do diretório `templates`, crie um novo arquivo chamado `index.html`.

3. Abra o arquivo `index.html` e adicione o seguinte código HTML:

   ```html
   <!doctype html>
   <html>
     <head>
       <title>Flask Quickstart</title>
     </head>
     <body>
       <h1>Hello, Flask!</h1>
     </body>
   </html>
   ```

4. Modifique seu arquivo `app.py` para renderizar o template `index.html`:

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
