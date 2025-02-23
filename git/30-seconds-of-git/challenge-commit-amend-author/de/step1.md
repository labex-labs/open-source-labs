# Ändern des Autors des letzten Commits

Du hast gerade einen Commit in dein Git-Repository gemacht, stellst aber fest, dass der Name und die E-Mail-Adresse des Autors falsch sind. Du möchtest die Autorinformationen aktualisieren, ohne den Inhalt des Commits zu ändern. Wie kannst du dies mit Git erreichen?

## Aufgaben

Um den Autor des letzten Commits zu ändern, kannst du einen Befehl verwenden. Dieser Befehl ermöglicht es dir, den letzten Commit in deinem Git-Repository zu modifizieren.

1. Navigiere zum Repository und konfiguriere Git's Identitätsinformationen mit deinem GitHub-Konto.
2. Ändere den Autor des letzten Commits zu `Duck Quackers`, dessen E-Mail-Adresse `cool.duck@qua.ck` ist, und speichere die Inhalte.
3. Verifiziere, dass die Autorinformationen aktualisiert wurden.

Du solltest sehen, dass der Autor des letzten Commits jetzt `Duck Quackers` ist:

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
