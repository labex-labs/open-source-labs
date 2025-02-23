# Zeigen Sie einen visuellen Graphen des Repositorys an

Als Entwickler müssen Sie möglicherweise die Geschichte eines Repositorys ansehen, um zu verstehen, wie sich der Code im Laufe der Zeit verändert hat. Ein einfaches Auflisten der Commits kann jedoch überwältigend und schwer zu verstehen sein. Hier kommt der Git-Graph ins Spiel. Indem Sie die Geschichte eines Repositorys visualisieren, können Sie schnell sehen, wie sich der Code entwickelt hat und eventuelle Probleme oder Fehler identifizieren, die möglicherweise eingeführt wurden.

Um einen visuellen Graphen eines Git-Repositorys anzuzeigen, können Sie den Befehl `git log` mit der Option `--graph` verwenden. Nehmen wir an, Sie möchten die Geschichte des `git-playground`-Repositorys auf GitHub ansehen.

Nachdem Sie das Repository geklont haben, können Sie in das Verzeichnis navigieren und den Befehl `git log` verwenden, um den Graphen anzuzeigen:

```shell
cd git-playground
git log --pretty=oneline --graph --decorate --all
```

Dies wird einen visuellen Graphen aller Commits und Branches im Repository anzeigen und Ihnen ermöglichen, zu sehen, wie sich der Code im Laufe der Zeit entwickelt hat.

Dies ist das Endresultat:

```
* d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
* cf80005e40a3c661eb212fcea5fad06f8283f08f Added file1.txt
* b00b9374a7c549d1af111aa777fdcc868d8a2a01 Initial commit
```
