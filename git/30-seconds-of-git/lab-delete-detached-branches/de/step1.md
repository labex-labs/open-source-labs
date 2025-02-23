# Entfernen von detached branches

Sie haben ein Git-Repository mit mehreren detached branches, die Sie nicht mehr benötigen. Diese Branches verschmutzen Ihr Repository und erschweren die Verwaltung. Sie möchten alle detached branches löschen, um Ihr Repository aufzuräumen.

Um dieses Lab zu absolvieren, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Konto, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Aktivieren Sie nicht das Kontrollkästchen "Kopiere nur die master-Branch".

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Da es in dem Remote-Repository eine `feature-branch`-Branch gibt, wechseln Sie zu `feature-branch`, was dazu führt, dass die lokale `feature-branch` die `feature-branch`-Branch des Remote-Repositories verfolgt, und löschen Sie die `feature-branch`-Branch im Remote-Repository:

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. Zeigen Sie die Verfolgungsbeziehung zwischen lokalen Branches und den Remote-Branches, die sie verfolgen:

```shell
git branch -vv
```

4. Wechseln Sie zurück zur `master`-Branch:

```shell
git checkout master
```

5. Entfernen Sie alle detached branches aus Ihrem lokalen Repository:

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. Vergewissern Sie sich, dass die detached branches gelöscht wurden:

```shell
git branch
```

Die Ausgabe sollte nur die Branches anzeigen, die mit einer bestimmten Branch assoziiert sind:

```shell
* master d22f46b [origin/master] Added file2.txt
```
