# Anpassen des Aussehens Ihrer _App_

Erstellen Sie zunächst ein Verzeichnis namens `static` im Verzeichnis `polls`. Django wird dort nach statischen Dateien suchen, ähnlich wie es Templates in `polls/templates/` findet.

Die Django-Einstellung `STATICFILES_FINDERS` enthält eine Liste von Findern, die wissen, wie statische Dateien aus verschiedenen Quellen entdeckt werden können. Einer der Standardfinder ist `AppDirectoriesFinder`, der nach einem Unterverzeichnis namens "static" in jeder der `INSTALLED_APPS` sucht, wie das in `polls`, das wir gerade erstellt haben. Die Administrationswebsite verwendet dieselbe Verzeichnisstruktur für ihre statischen Dateien.

Innerhalb des gerade erstellten `static`-Verzeichnisses erstellen Sie ein weiteres Verzeichnis namens `polls` und darin eine Datei namens `style.css`. Mit anderen Worten, Ihre Stylesheet-Datei sollte sich unter `polls/static/polls/style.css` befinden. Aufgrund der Arbeitsweise des `AppDirectoriesFinder`-Statikdateienfinders können Sie diese statische Datei in Django als `polls/style.css` referenzieren, ähnlich wie Sie den Pfad zu Templates referenzieren.

## Namensraum für statische Dateien

Genau wie bei Templates könnten wir möglicherweise statische Dateien direkt in `polls/static` ablegen (anstatt ein weiteres `polls`-Unterverzeichnis zu erstellen), aber das wäre tatsächlich eine schlechte Idee. Django wird die erste statische Datei auswählen, deren Name übereinstimmt, und wenn Sie eine statische Datei mit demselben Namen in einer _anderen_ Anwendung hätten, wäre Django nicht in der Lage, zwischen ihnen zu unterscheiden. Wir müssen Django die richtige Datei anzeigen können, und der beste Weg, dies sicherzustellen, ist, indem wir sie _namespacing_. Das heißt, indem wir diese statischen Dateien in einem weiteren Verzeichnis ablegen, das nach der Anwendung selbst benannt ist.

Fügen Sie folgenden Code in diese Stylesheet-Datei (`polls/static/polls/style.css`) ein:

```css
li a {
  color: green;
}
```

Fügen Sie anschließend Folgendes am Anfang von `polls/templates/polls/index.html` hinzu:

```html+django
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

Das `{% static %}`-Template-Tag generiert die absolute URL von statischen Dateien.

Das ist alles, was Sie für die Entwicklung tun müssen.

Starten Sie den Server (oder starten Sie ihn neu, wenn er bereits läuft):

```bash
python manage.py runserver 0.0.0.0:8080
```

Neuladen Sie die Registerkarte **Web 8080** und Sie sollten sehen, dass die Frage-Links grün sind (Django-Style!), was bedeutet, dass Ihr Stylesheet richtig geladen wurde.

![Beispiel für grüne Frage-Links](../assets/20230908-15-29-11-ztyI1umP.png)
