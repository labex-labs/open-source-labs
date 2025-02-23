# Konfiguriere den Git-Texteditor

Für dieses Lab verwenden wir das Repository von `https://github.com/labex-labs/git-playground`. Sie möchten den von Git verwendeten Texteditor auf Ihren bevorzugten Editor konfigurieren.

1. Klone das `git-playground`-Repository:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Navigiere zum geklonten Repository und konfiguriere die Identität:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Konfiguriere Git, um Ihren bevorzugten Texteditor zu verwenden (in diesem Beispiel verwenden wir vim):

```shell
git config --global core.editor "vim"
```

4. Mache eine Änderung an einer Datei und bereite sie vor, um sie zu committen:

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. Committe die Änderung:

```shell
git commit
```

6. Ihr bevorzugter Texteditor (in diesem Beispiel vim) sollte mit der Commit-Nachricht geöffnet werden. Schreibe Ihre Commit-Nachricht "Update hello.txt" und speichere die Datei.
7. Schließe den Texteditor. Der Commit wird mit der Nachricht durchgeführt, die Sie geschrieben haben.

Dies ist das fertige Ergebnis:

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
