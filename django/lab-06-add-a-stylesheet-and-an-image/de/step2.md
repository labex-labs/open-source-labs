# Hinzufügen eines Hintergrundbilds

Als nächstes erstellen wir ein Unterverzeichnis für Bilder. Erstellen Sie ein Unterverzeichnis `images` im Verzeichnis `polls/static/polls/`. Fügen Sie in diesem Verzeichnis jede Bilddatei hinzu, die Sie als Hintergrund verwenden möchten. Im Rahmen dieses Tutorials verwenden wir eine Datei namens `background.png`, die Sie im Verzeichnis `/tmp/background.png` in der VM finden können.

Sie müssen die Datei `/tmp/background.png` in `polls/static/polls/images/background.png` kopieren.

Fügen Sie anschließend einen Verweis auf Ihr Bild in Ihrem Stylesheet (`polls/static/polls/style.css`) hinzu:

```css
body {
  background: white url("images/background.png") no-repeat;
}
```

Neuladen Sie die Registerkarte **Web 8080** und Sie sollten sehen, dass das Hintergrundbild in der oberen linken Ecke des Bildschirms geladen wird.

![Beispiel für Hintergrundbild](../assets/20230908-15-39-41-8dGms0NM.png)

> Das `{% static %}`-Template-Tag ist nicht in statischen Dateien verfügbar, die nicht von Django generiert werden, wie Ihr Stylesheet. Sie sollten immer **relative Pfade** verwenden, um Ihre statischen Dateien miteinander zu verknüpfen, da Sie dann `STATIC_URL` (das vom `static`-Template-Tag verwendet wird, um seine URLs zu generieren) ändern können, ohne dass Sie auch eine Reihe von Pfaden in Ihren statischen Dateien ändern müssen.

Dies sind die **Grundlagen**. Weitere Details zu Einstellungen und anderen Teilen des Frameworks finden Sie unter `the static files howto </howto/static-files/index>` und `the staticfiles reference </ref/contrib/staticfiles>`. `Deploying static files </howto/static-files/deployment>` behandelt die Verwendung von statischen Dateien auf einem realen Server.

Wenn Sie sich mit den statischen Dateien vertraut machen, lesen Sie **Customizing Django's Admin Site**, um zu lernen, wie Sie die automatisch generierte Django-Administrationswebsite anpassen.
