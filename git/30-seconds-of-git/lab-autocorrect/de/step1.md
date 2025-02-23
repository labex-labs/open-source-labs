# Autokorrektur von Git-Befehlen

Das Problem ist, dass Entwickler oft Git-Befehle falsch tippen, was zu Fehlern führen und ihren Workflow verlangsamen kann. Beispielsweise könnte ein Entwickler versehentlich `git sttaus` statt `git status` tippen, was zu einer Fehlermeldung führt. Dies kann frustrierend und zeitaufwendig sein, insbesondere wenn an großen Projekten mit vielen Dateien und Mitwirkenden gearbeitet wird.

Um zu demonstrieren, wie die Autokorrekturfunktion von Git verwendet wird, verwenden wir das Git-Repository im Verzeichnis `https://github.com/labex-labs/git-playground`.

1. Öffnen Sie Ihren Terminal und navigieren Sie zum Verzeichnis, in dem Sie das Repository klonen möchten.
2. Klonen Sie das Repository mit dem folgenden Befehl:

```
git clone https://github.com/labex-labs/git-playground.git
```

3. Navigieren Sie zum geklonten Repository mit dem folgenden Befehl:

```
cd git-playground
```

4. Aktivieren Sie die Autokorrekturfunktion von Git mit dem folgenden Befehl:

```
git config --global help.autocorrect 1
```

5. Versuchen Sie, einen Git-Befehl falsch zu tippen, wie z. B. `git sttaus`. Git wird den Befehl automatisch korrigieren und `git status` statt dessen ausführen.

Dies ist das Ergebnis nach Abschluss des Labs:

![Git autocorrect command result](../assets/challenge-autocorrect-step1-1.jpg)
