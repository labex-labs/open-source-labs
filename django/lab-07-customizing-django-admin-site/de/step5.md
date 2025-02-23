# Anpassen der Admin-Startseite

In ähnlicher Weise möchten Sie vielleicht das Aussehen und die Bedienbarkeit der Django-Admin-Startseite anpassen.

Standardmäßig werden alle Apps in `INSTALLED_APPS`, die mit der Admin-Anwendung registriert wurden, in alphabetischer Reihenfolge angezeigt. Möglicherweise möchten Sie erhebliche Änderungen am Layout vornehmen. Schließlich ist die Startseite wahrscheinlich die wichtigste Seite der Admin und sollte einfach zu bedienen sein.

Das zu customisierende Template ist `admin/index.html`. (Tun Sie das Gleiche wie mit `admin/base_site.html` im vorherigen Abschnitt - kopieren Sie es aus dem Standardverzeichnis in Ihr benutzerdefiniertes Templateverzeichnis). Bearbeiten Sie die Datei, und Sie werden sehen, dass sie eine Template-Variable namens `app_list` verwendet. Diese Variable enthält jede installierte Django-App. Anstatt dies zu verwenden, können Sie Links zu objekt-spezifischen Admin-Seiten in der Weise hartcodieren, die Ihnen am besten erscheint.
