# Branches finden, die einen Commit nicht enthalten

Sie arbeiten an einem Projekt mit mehreren Branches und müssen alle Branches finden, die einen bestimmten Commit nicht enthalten. Dies kann nützlich sein, wenn Sie sicherstellen möchten, dass eine bestimmte Änderung auf alle Branches angewendet wurde, oder wenn Sie wissen möchten, welche Branches veraltet sind und aktualisiert werden müssen.

Für dieses Lab verwenden wir das Git-Repository mit dem Namen `https://github.com/your-username/git-playground`.

1. Klonen Sie dieses Repository auf Ihren lokalen Computer mit dem folgenden Befehl:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Nachdem das Repository geklont wurde, verwenden Sie die folgenden Befehle, um in das Verzeichnis zu navigieren und die Identität zu konfigurieren:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Erstellen Sie und wechseln Sie zu einem `new-branch`-Branch und machen Sie einige Codeänderungen auf diesem Branch und committen Sie sie dann, die Commit-Nachricht lautet "Create a new-branch branch":

```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
```

4. Überprüfen Sie den Hash der Commit-Nachricht "Create a new-branch branch":

```shell
git log
```

5. Finden Sie alle Branches, die keinen Hash mit der Commit-Nachricht "Create a new-branch branch" enthalten. Dazu können wir den folgenden Befehl verwenden:

```shell
git branch --no-contains 31c5ac20129151af1
```

Dies wird eine Liste aller Branches ausgeben, die den angegebenen Commit nicht enthalten. In diesem Fall wird die Ausgabe wie folgt sein:

```shell
master
```

Dies bedeutet, dass der `master`-Branch den Commit mit dem Hash `31c5ac20129151af1` nicht enthält.
