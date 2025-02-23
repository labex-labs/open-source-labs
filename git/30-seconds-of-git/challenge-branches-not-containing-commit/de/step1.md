# Branches finden, die einen Commit nicht enthalten

Sie arbeiten an einem Projekt mit mehreren Branches und müssen alle Branches finden, die einen bestimmten Commit nicht enthalten. Dies kann nützlich sein, wenn Sie sicherstellen möchten, dass eine bestimmte Änderung auf alle Branches angewendet wurde, oder wenn Sie wissen möchten, welche Branches veraltet sind und aktualisiert werden müssen.

## Aufgaben

Für diese Herausforderung verwenden wir das Git-Repository mit dem Namen `https://github.com/your-username/git-playground`.

1. Klonen Sie dieses Repository auf Ihren lokalen Computer.
2. Navigieren Sie zu dem Verzeichnis, nachdem Sie das Repository geklont haben.
3. Erstellen Sie und wechseln Sie zu einem `new-branch`-Branch und machen Sie einige Codeänderungen auf diesem Branch und committen Sie sie dann, die Commit-Nachricht lautet "Create a new-branch branch".
4. Überprüfen Sie den Hash der Commit-Nachricht "Create a new-branch branch".
5. Finden Sie alle Branches, die keinen Hash mit der Commit-Nachricht "Create a new-branch branch" enthalten.

Dies wird eine Liste aller Branches ausgeben, die den angegebenen Commit nicht enthalten. Im diesem Fall wird die Ausgabe lauten:

```shell
master
```

Dies bedeutet, dass der `master`-Branch den Commit mit dem Hash `31c5ac20129151af1` nicht enthält.
