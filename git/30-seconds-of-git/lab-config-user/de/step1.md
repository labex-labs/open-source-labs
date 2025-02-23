# Konfigurieren von Git-Benutzereinformationen

Sie haben gerade begonnen, an einem neuen Projekt zu arbeiten, und möchten Ihre Benutzereinformationen für Git konfigurieren. Sie möchten sicherstellen, dass Ihr Name und Ihre E-Mail-Adresse mit allen Änderungen verbunden sind, die Sie am Repository vornehmen.

Für dieses Lab verwenden wir das Git-Repository mit der URL `https://github.com/labex-labs/git-playground`. Folgen Sie diesen Schritten, um Ihre Benutzereinformationen für dieses Repository zu konfigurieren:

1. Klonen Sie das Repository mit dem folgenden Befehl:

```
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigieren Sie zum geklonten Repository mit dem folgenden Befehl:

```
cd git-playground
```

3. Verwenden Sie den Befehl `git config`, um Ihre Benutzereinformationen für das Repository festzulegen. Beispielsweise würden Sie die folgenden Befehle verwenden, wenn Ihre E-Mail-Adresse `jane.doe@example.com` und Ihr Name `Jane Doe` lautet:

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```

4. Vergewissern Sie sich, dass Ihre Benutzereinformationen korrekt festgelegt wurden, indem Sie folgenden Befehl verwenden: `git config --list`. Unter den Schlüsseln `user.email` und `user.name` sollten Sie Ihre E-Mail-Adresse und Ihren Namen aufgelistet sehen.

Dies ist das Ergebnis nach Abschluss des Labs:

![Git user configuration result](../assets/challenge-config-user-step1-1.png)
