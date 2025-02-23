# Entfernen von hartcodierten URLs in Templates

Denken Sie daran, als wir den Link zu einer Frage im `polls/index.html`-Template geschrieben haben, war der Link teilweise wie folgt hartcodiert:

```html+django
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

Das Problem mit diesem hartcodierten, eng gekoppelten Ansatz ist, dass es schwierig wird, URLs in Projekten mit vielen Templates zu ändern. Da Sie jedoch das `name`-Argument in den `~django.urls.path`-Funktionen im `polls.urls`-Modul definiert haben, können Sie die Abhängigkeit von bestimmten in Ihren URL-Konfigurationen definierten URL-Pfaden entfernen, indem Sie das `{% url %}`-Template-Tag verwenden:

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

Wie dies funktioniert, besteht darin, die in der `polls.urls`-Datei definierte URL-Definition aufzurufen. Sie können genau sehen, wo der URL-Name 'detail' definiert ist, wie hier unten:

```python
# der 'name'-Wert, wie er vom {% url %} Template-Tag aufgerufen wird
path("<int:question_id>/", views.detail, name="detail"),
```

Wenn Sie die URL der Umfrage-Detail-Ansicht auf etwas anderes ändern möchten, vielleicht auf etwas wie `polls/specifics/12/` anstatt es im Template (oder Templates) zu tun, würden Sie es in `polls/urls.py` ändern:

> Sie müssen das Template überhaupt nicht ändern.

```python
# das Wort'specifics' hinzugefügt
path("specifics/<int:question_id>/", views.detail, name="detail"),
```
