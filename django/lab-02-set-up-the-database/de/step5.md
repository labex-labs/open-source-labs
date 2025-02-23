# Einführung in die Django-Admin

Das Erstellen von Administrationsseiten für Ihr Personal oder Kunden, um Inhalte hinzuzufügen, zu ändern und zu löschen, ist mühsame Arbeit, die nicht viel Kreativität erfordert. Aus diesem Grund automatisieren Django die Erstellung von Administrationsschnittstellen für Modelle vollständig.

Django wurde in einem Redaktionsumfeld geschrieben, mit einer sehr klaren Trennung zwischen "Inhaltspublizisten" und der "öffentlichen" Website. Die Site-Manager verwenden das System, um Nachrichten, Veranstaltungen, Sportergebnisse usw. hinzuzufügen, und dieser Inhalt wird auf der öffentlichen Website angezeigt. Django löst das Problem der Erstellung einer einheitlichen Schnittstelle für die Site-Administratoren, um Inhalte zu bearbeiten.

Die Admin-Site ist nicht für die Besucher der Website gedacht. Sie ist für die Site-Manager.

## Erstellen eines Admin-Benutzers

Zunächst müssen wir einen Benutzer erstellen, der sich in die Admin-Site einloggen kann. Führen Sie folgenden Befehl aus:

```bash
python manage.py createsuperuser
```

Geben Sie Ihren gewünschten Benutzernamen ein und drücken Sie die Eingabetaste.

```plaintext
Username: admin
```

Anschließend werden Sie aufgefordert, Ihre gewünschte E-Mail-Adresse einzugeben:

```plaintext
Email address: admin@example.com
```

Der letzte Schritt ist, Ihr Passwort einzugeben. Sie werden dazu aufgefordert, Ihr Passwort zweimal einzugeben, das zweite Mal als Bestätigung des ersten.

```plaintext
Password: 12345678
Password (again): 12345678

This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Starten des Entwicklungsservers

Die Django-Admin-Site ist standardmäßig aktiviert. Lassen Sie uns den Entwicklungsserver starten und ihn erkunden.

Wenn der Server nicht läuft, starten Sie ihn wie folgt:

```bash
python manage.py runserver
```

Öffnen Sie jetzt einen Webbrowser im **VNC**-Tab und gehen Sie auf Ihrer lokalen Domain zu "/admin/" - z.B. `http://127.0.0.1:8000/admin/`. Sie sollten das Login-Screen der Admin-Site sehen:

![Django admin login screen](../assets/20230907-14-31-50-SvkJF8K8.png)

Da `translation </topics/i18n/translation>` standardmäßig eingeschaltet ist, wird der Login-Screen in der angegebenen Sprache angezeigt (wenn Django passende Übersetzungen hat).

## Eintreten in die Admin-Site

Versuchen Sie jetzt, sich mit dem Superuser-Konto einzuloggen, das Sie im vorherigen Schritt erstellt haben. Sie sollten die Django-Admin-Indexseite sehen:

![Django admin index page](../assets/admin02.png)

Sie sollten einige Arten von bearbeitbarem Inhalt sehen: Gruppen und Benutzer. Sie werden von `django.contrib.auth`, dem Authentifizierungsframework, das von Django mitgeliefert wird, bereitgestellt.

## Machen Sie die Umfrage-App im Admin veränderbar

Aber wo ist unsere Umfrage-App? Sie wird nicht auf der Admin-Indexseite angezeigt.

Es bleibt nur noch ein weiterer Schritt: Wir müssen der Admin mitteilen, dass `Question`-Objekte eine Admin-Schnittstelle haben. Um dies zu tun, öffnen Sie die Datei `polls/admin.py` und bearbeiten Sie sie, so dass sie wie folgt aussieht:

```python
from django.contrib import admin

from.models import Question

admin.site.register(Question)
```

## Erkunden Sie die kostenlosen Admin-Funktionalitäten

Jetzt, da wir `Question` registriert haben, weiß Django, dass es auf der Admin-Indexseite angezeigt werden sollte:

![Django admin index page, now with polls displayed](../assets/admin03t.png)

Klicken Sie auf "Fragen". Jetzt befinden Sie sich auf der "Änderungsliste"-Seite für Fragen. Diese Seite zeigt alle Fragen in der Datenbank an und ermöglicht es Ihnen, eine auszuwählen, um sie zu ändern. Da ist die Frage "What's up?", die wir zuvor erstellt haben:

![Polls change list page](../assets/admin04t.png)

Klicken Sie auf die Frage "What's up?", um sie zu bearbeiten:

![Editing a poll question](../assets/20230907-14-33-49-XWeEgAXl.png)

Dinge, die hier zu beachten sind:

- Das Formular wird automatisch aus dem `Question`-Modell generiert.
- Die verschiedenen Modellfeldtypen (`~django.db.models.DateTimeField`, `~django.db.models.CharField`) entsprechen dem passenden HTML-Eingabefeld. Jeder Feldtyp weiß, wie er sich in der Django-Admin anzeigt.
- Jeder `~django.db.models.DateTimeField` erhält kostenlose JavaScript-Kurzschlüsse. Datumseingaben erhalten einen "Heute"-Kurzschluss und einen Kalender-Popup, und Zeitangaben erhalten einen "Jetzt"-Kurzschluss und ein bequemes Popup, das häufig eingegebene Zeiten auflistet.

Der untere Teil der Seite bietet Ihnen einige Optionen:

- Speichern - Speichert die Änderungen und kehrt zur Änderungsliste-Seite für diesen Objekttyp zurück.
- Speichern und fortfahren mit der Bearbeitung - Speichert die Änderungen und lädt die Admin-Seite für dieses Objekt neu.
- Speichern und einen anderen hinzufügen - Speichert die Änderungen und lädt ein neues, leeres Formular für diesen Objekttyp.
- Löschen - Zeigt eine Löschbestätigungsseite an.

Wenn der Wert von "Veröffentlicht am" nicht mit der Zeit übereinstimmt, zu der Sie die Frage im **Erstellen einer einfachen Umfrageanwendung** erstellt haben, bedeutet dies wahrscheinlich, dass Sie vergessen haben, den richtigen Wert für die `TIME_ZONE`-Einstellung festzulegen. Ändern Sie es, laden Sie die Seite neu und überprüfen Sie, ob der richtige Wert erscheint.

Ändern Sie das "Veröffentlicht am", indem Sie die "Heute"- und "Jetzt"-Kurzschlüsse klicken. Klicken Sie dann auf "Speichern und fortfahren mit der Bearbeitung". Klicken Sie anschließend auf "Verlauf" in der oberen rechten Ecke. Sie werden eine Seite sehen, die alle Änderungen an diesem Objekt via der Django-Admin auflistet, mit dem Zeitstempel und dem Benutzernamen der Person, die die Änderung vorgenommen hat:

![History page for question object](../assets/admin06t.png)

Wenn Sie sich mit der Models-API vertraut machen und sich mit der Admin-Site vertraut gemacht haben, lesen Sie **Erstellen der öffentlichen Schnittstellensichten**, um zu erfahren, wie Sie unserer Umfrage-App weitere Sichten hinzufügen.
