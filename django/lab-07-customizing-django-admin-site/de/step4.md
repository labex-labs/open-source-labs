# Anpassen des Admin-Aussehens und der Bedienbarkeit

Offensichtlich ist es lächerlich, "Django-Verwaltung" oben auf jeder Admin-Seite zu haben. Es ist nur Platzhaltertext.

Sie können es jedoch ändern, indem Sie das Django-Templatesystem verwenden. Die Django-Admin wird von Django selbst betrieben, und ihre Schnittstellen verwenden das eigene Templatesystem von Django.

## Anpassen der _Projekt_ -Templates

Erstellen Sie ein Verzeichnis `templates` im Projektverzeichnis (dem Verzeichnis, das `manage.py` enthält). Templates können an jedem Ort auf der Dateisystemebene gespeichert werden, auf den Django zugreifen kann. (Django läuft als der Benutzer, unter dem auch der Server läuft.) Es ist jedoch eine gute Konvention, die Templates innerhalb des Projekts zu halten.

Öffnen Sie Ihre Einstellungsdatei (`mysite/settings.py`, denken Sie daran) und fügen Sie eine `DIRS <TEMPLATES-DIRS>` -Option in die `TEMPLATES` -Einstellung hinzu:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

`DIRS <TEMPLATES-DIRS>` ist eine Liste von Dateisystemverzeichnissen, die überprüft werden, wenn Django-Templates geladen werden; es ist ein Suchpfad.

## Organisieren von Templates

Genau wie die statischen Dateien _könnten_ wir alle unsere Templates zusammen in einem großen `templates` -Verzeichnis haben, und es würde perfekt funktionieren. Allerdings sollten Templates, die zu einer bestimmten Anwendung gehören, in das Templateverzeichnis dieser Anwendung (z.B. `polls/templates`) statt im Projektverzeichnis (`templates`) platziert werden. Wir werden im `reusable apps tutorial </intro/reusable-apps>` im Detail diskutieren, _warum_ wir dies tun.

Erstellen Sie nun ein Verzeichnis namens `admin` innerhalb von `templates`, und kopieren Sie die Vorlage `admin/base_site.html` aus dem Standard-Django-Admin-Templateverzeichnis im Quellcode von Django selbst (`django/contrib/admin/templates`) in dieses Verzeichnis.

## Wo befinden sich die Django-Quelldateien?

Wenn Sie Schwierigkeiten haben, zu finden, wo sich die Django-Quelldateien auf Ihrem System befinden, führen Sie den folgenden Befehl aus:

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

Anschließend bearbeiten Sie die Datei und ersetzen Sie `{{ site_header|default:_('Django administration') }}` (einschließlich der geschweiften Klammern) durch den Namen Ihrer eigenen Website, wie Ihnen am besten passt. Sie sollten am Ende mit einem Codeabschnitt wie diesem übrigbleiben:

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a><div>
{% endblock %}
```

Wir verwenden diese Methode, um Ihnen zu zeigen, wie Sie Templates überschreiben. In einem tatsächlichen Projekt würden Sie wahrscheinlich das Attribut `django.contrib.admin.AdminSite.site_header` verwenden, um diese spezifische Anpassung einfacher vorzunehmen.

Diese Template-Datei enthält viel Text wie `{% block branding %}` und `{{ title }}`. Die Tags `{%` und `{{` sind Teil der Django-Templatelanguage. Wenn Django `admin/base_site.html` rendert, wird diese Templatelanguage ausgewertet, um die endgültige HTML-Seite zu erzeugen, genauso wie wir es in `**Creating the Public Interface Views**` gesehen haben.

Beachten Sie, dass jeder der Standard-Django-Admin-Templates überschrieben werden kann. Um ein Template zu überschreiben, tun Sie das Gleiche wie mit `base_site.html` - kopieren Sie es aus dem Standardverzeichnis in Ihr benutzerdefiniertes Verzeichnis und machen Sie Änderungen.

## Anpassen der _Anwendung_ -Templates

Genau beobachtende Leser werden fragen: Aber wenn `DIRS <TEMPLATES-DIRS>` standardmäßig leer war, wie hat Django die Standard-Admin-Templates gefunden? Die Antwort ist, dass, da `APP_DIRS <TEMPLATES-APP_DIRS>` auf `True` gesetzt ist, Django automatisch nach einem `templates/` -Unterverzeichnis innerhalb jedes Anwendungs-Pakets sucht, um es als Rückfall zu verwenden (vergessen Sie nicht, dass `django.contrib.admin` eine Anwendung ist).

Unsere Umfrageanwendung ist nicht sehr komplex und benötigt keine benutzerdefinierten Admin-Templates. Wenn sie jedoch komplexer würde und Änderungen an den Standard-Django-Admin-Templates für einige ihrer Funktionen erforderte, wäre es vernünftiger, die _Anwendung_ -Templates zu modifizieren, anstatt die im _Projekt_. Auf diese Weise könnten Sie die Umfrageanwendung in jedes neue Projekt einbetten und sicherstellen, dass sie die benötigten benutzerdefinierten Templates finden würde.

Siehe die `template loading documentation <template-loading>` für weitere Informationen darüber, wie Django seine Templates findet.
