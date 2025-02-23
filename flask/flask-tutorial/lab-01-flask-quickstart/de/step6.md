# Hinzufügen von dynamischem Inhalt

Flask ermöglicht es uns, dynamischen Inhalt an unsere Vorlagen zu übergeben. Lassen Sie uns unseren Route ändern, um einen Namenparameter zu übergeben und einen persönlichen Gruß anzuzeigen.

1. Ändern Sie Ihre `app.py`-Datei, um einen Namenparameter im Route zu akzeptieren:

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. Öffnen Sie die Datei `index.html` und ändern Sie das `<h1>`-Tag, um den persönlichen Gruß anzuzeigen:

   ```html
   <h1>Hello, {{ name }}!</h1>
   ```
