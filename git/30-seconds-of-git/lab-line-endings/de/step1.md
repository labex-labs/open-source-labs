# Zeilenenden konfigurieren

Sie arbeiten an einem Projekt mit einem Team von Entwicklern und stellen fest, dass einige Teammitglieder andere Zeilenenden als andere verwenden. Dies kann Probleme bei der Zusammenführung von Code verursachen und zu Konflikten führen. Sie müssen die Zeilenenden für das Repository konfigurieren, um Konsistenz zu gewährleisten und Konflikte zu vermeiden.

Auf Unix- oder Unix-ähnlichen Systemen endet jede Zeile von Text mit dem Zeilenende `LF` (Line Feed). Wenn Sie die `cat`-Befehl verwenden, um eine Datei anzuzeigen, werden Zeilenenden normalerweise nicht auf dem Bildschirm angezeigt, da sie als das Ende der Zeile, nicht als Teil der Zeile betrachtet werden.

Wenn Sie eine Datei mit dem Befehl `cat -vet` anzeigen, zeigt die Option `-v` nicht-druckbare Zeichen als sichtbare Zeichendarstellungen an, wie das `$`-Symbol. Daher bedeutet es, wenn Sie das `$`-Symbol in einer Datei sehen, dass jede Zeile in der Datei mit dem Zeilenende `LF` endet. `LF` und `\n` sind das gleiche Konzept und bezeichnen ein Zeilenende.

Um die Zeilenenden für das Repository `git-playground` zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Öffnen Sie die Befehlszeile oder das Terminal auf Ihrem Computer.
2. Navigieren Sie zum Verzeichnis, in dem das Repository `git-playground` im Verzeichnis `~/project` gespeichert ist.
3. Führen Sie den folgenden Befehl aus, um die Zeilenenden so zu konfigurieren, dass UNIX-Zeilenenden verwendet werden:

   ```shell
   git config core.eol lf
   ```

   Dies konfiguriert die Zeilenenden, um das UNIX-Zeilenende (`\n`) zu verwenden.

4. Führen Sie den folgenden Befehl aus, um zu überprüfen, ob die Zeilenenden korrekt konfiguriert wurden:

   ```shell
   git config core.eol
   ```

   Dies zeigt die aktuelle Zeilenendkonfiguration an.

Dies ist das Ergebnis von `cat -vet file2.txt`:

```shell
This is file2.$
```
