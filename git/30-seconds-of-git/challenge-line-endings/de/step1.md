# Zeilenenden konfigurieren

Sie arbeiten an einem Projekt mit einem Team von Entwicklern und stellen fest, dass einige Teammitglieder andere Zeilenenden als andere verwenden. Dies kann Probleme bei der Zusammenführung von Code verursachen und zu Konflikten führen. Sie müssen die Zeilenenden für das Repository konfigurieren, um Konsistenz zu gewährleisten und Konflikte zu vermeiden.

## Aufgaben

Um die Zeilenenden für das Repository `git-playground` zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Navigieren Sie zum Verzeichnis, in dem das Repository `git-playground` gespeichert ist (`~/project/git-playground`).
2. Konfigurieren Sie die Zeilenenden, um UNIX-Zeilenenden (`\n`) zu verwenden.
3. Vergewissern Sie sich, dass die Zeilenenden korrekt konfiguriert wurden.

## Beispiel

Um zu überprüfen, ob die Zeilenenden korrekt konfiguriert wurden, können Sie den folgenden Befehl verwenden:

```bash
git config --get core.eol
```

Wenn die Zeilenenden korrekt konfiguriert wurden, wird der Befehl `lf` zurückgeben.

![Git line endings configuration](../assets/20240702-15-01-34-S4a8vHzh@2x.png)
