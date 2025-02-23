# Erstellen eines neuen Branches

Für dieses Lab forken Sie das Git-Repository mit dem Namen `https://github.com/labex-labs/git-playground` in Ihr GitHub-Konto. Sie arbeiten an einem Projekt in einem Git-Repository mit dem Namen `https://github.com/your-username/git-playground`. Sie müssen einen neuen Branch mit dem Namen `feature-1` erstellen, um an einer neuen Funktion zu arbeiten.

1. Klonen Sie das Repository, navigieren Sie zum Verzeichnis und konfigurieren Sie die Identität:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Überprüfen Sie den aktuellen Branch:

```shell
git branch
```

3. Erstellen Sie einen neuen Branch mit dem Namen `feature-1`:

```shell
git checkout -b feature-1
```

4. Vergewissern Sie sich, dass Sie jetzt auf dem Branch `feature-1` sind:

```shell
git branch
```

5. Stellen Sie die Änderungen auf das Remote-Repository dar:

```shell
git push -u origin feature-1
```

Dies ist das, was passiert, wenn Sie den Befehl `git branch -r` ausführen:

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
