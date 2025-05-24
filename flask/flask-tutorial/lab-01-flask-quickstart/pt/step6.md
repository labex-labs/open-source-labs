# Adicionando Conteúdo Dinâmico

Flask nos permite passar conteúdo dinâmico para nossos templates. Vamos modificar nossa rota para passar um parâmetro nome (name) e exibir uma saudação personalizada.

1. Modifique seu arquivo `app.py` para aceitar um parâmetro nome na rota:

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. Abra o arquivo `index.html` e modifique a tag `<h1>` para exibir a saudação personalizada:

   ```html
   <h1>Hello, {{ name }}!</h1>
   ```
