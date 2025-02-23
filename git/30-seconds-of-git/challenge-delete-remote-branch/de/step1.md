# Entfernen eines Remote-Branches

Manchmal müssen Sie einen Remote-Branch entfernen, den Sie nicht mehr benötigen. Wenn beispielsweise ein Feature-Branch in den Haupt-Branch zusammengeführt wurde, möchten Sie möglicherweise den Remote-Feature-Branch löschen, um das Repository sauber zu halten.

## Aufgaben

Angenommen, ein GitHub-Repository namens `git-playground` wurde von Ihrem GitHub-Konto geklont, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Sie möchten den Remote-Branch namens `feature-branch` entfernen, den Sie nicht mehr benötigen.

1. Öffnen Sie das Terminal und navigieren Sie zum Verzeichnis des lokalen Repositorys.
2. Fügen Sie den `feature-branch`-Branch zum `origin`-Remote-Repository hinzu.
3. Listen Sie alle Remote-Branches auf.
4. Löschen Sie den `feature-branch`-Remote-Branch auf dem `origin`-Remote-Repository.
5. Vergewissern Sie sich, dass der Remote-Branch gelöscht wurde.

Die Ausgabe sollte nicht den `feature-branch`-Remote-Branch enthalten:

```
origin/HEAD -> origin/master
origin/master
```
