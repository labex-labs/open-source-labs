# Einen Commit von einem anderen Autor erstellen

Angenommen, Sie arbeiten an einem Projekt mit einem Team von Entwicklern, und ein Teammitglied hat einige Änderungen am Code vorgenommen. Sie sind jedoch nicht verfügbar, um die Änderungen selbst zu committen, und Sie müssen dies im Namen des anderen Teammitglieds tun. In diesem Szenario können Sie die Option `--author` verwenden, um den Namen und die E-Mail-Adresse des Commit-Autors zu ändern. Diese Option ist nützlich, wenn Sie einem Commit einen anderen Autor zuweisen müssen, z. B. wenn Sie Code im Namen eines Kollegen committen, der im Urlaub oder krank ist.

Um einen Commit von einem anderen Autor zu erstellen, können Sie den folgenden Befehl verwenden:

```shell
git commit -m < message > --author="<name> <email>"
```

Angenommen, Sie arbeiten an einem Projekt, das auf dem Repository `https://github.com/labex-labs/git-playground` gehostet ist. Sie haben einige Änderungen am Code vorgenommen und müssen einen Commit im Namen Ihres Kollegen John Doe erstellen, der nicht verfügbar ist, um die Änderungen selbst zu committen. Dazu können Sie den folgenden Befehl verwenden:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.email "your email"
git config --global user.name "your username"
echo "Fix the network bug" > README.md
git add.
git commit -m "Fix the bug" --author="John Doe <john.doe@example.com>"
```

Dieser Befehl erstellt einen neuen Commit mit der Nachricht "Fix the bug" und weist ihn John Doe zu.

Dies ist das fertige Ergebnis:

![Git commit author change result](../assets/challenge-commit-set-author-step1-1.png)
