# Ändern des Autors des letzten Commits

Du hast gerade einen Commit an dein Git-Repository gemacht, stellst aber fest, dass der Name und die E-Mail-Adresse des Autors falsch sind. Du möchtest die Informationen des Autors aktualisieren, ohne den Inhalt des Commits zu ändern. Wie kannst du dies mit Git erreichen?

Um den Autor des letzten Commits zu ändern, kannst du den Befehl `git commit --amend` verwenden. Dieser Befehl ermöglicht es dir, den letzten Commit in deinem Git-Repository zu modifizieren. Hier ist ein Beispiel, wie du den Namen und die E-Mail-Adresse des Autors ändern kannst:

1. Klone das Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground` auf deinen lokalen Computer:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Konfiguriere die Identitätsinformationen von Git mit deinem GitHub-Konto:

```shell
cd git-playground
git config user.email "deine E-Mail"
git config user.name "dein Benutzername"
```

3. Verwende den Befehl `git commit --amend`, um den Autor des letzten Commits zu modifizieren und die Inhalte zu speichern:

```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```

4. Verifiziere, dass die Informationen des Autors aktualisiert wurden:

```shell
git log
```

Du solltest sehen, dass der Autor des letzten Commits jetzt `Duck Quackers` ist:

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
