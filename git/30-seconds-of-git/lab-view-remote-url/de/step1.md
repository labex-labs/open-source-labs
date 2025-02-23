# Zeige die Remote-URL an

Als Entwickler benötigen Sie möglicherweise aus verschiedenen Gründen die URL eines Remote-Repositorys, beispielsweise, um Probleme mit Ihrer Git-Konfiguration zu beheben oder zu überprüfen, dass Sie mit dem richtigen Repository arbeiten. Wenn Sie jedoch nicht mit Git-Befehlen vertraut sind, kann es herausfordernd sein, zu wissen, wie Sie die Remote-URL anzeigen.

Für dieses Lab verwenden wir das Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground`. Um die Remote-URL dieses Repositorys anzuzeigen, führen Sie die folgenden Schritte aus:

1. Öffnen Sie Ihr Terminal oder die Befehlszeile.
2. Navigieren Sie zum Verzeichnis, in dem Sie das `git-playground`-Repository geklont haben:

```shell
cd git-playground
```

3. Führen Sie den folgenden Befehl aus, um die Remote-URL anzuzeigen:

```shell
git config --get remote.origin.url
```

Die Ausgabe sollte die URL des Remote-Repositorys anzeigen, was in diesem Fall `https://github.com/labex-labs/git-playground.git` ist.
