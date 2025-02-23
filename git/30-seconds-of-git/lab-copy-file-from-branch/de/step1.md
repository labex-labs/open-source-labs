# Kopiere eine Datei von einem anderen Branch

Sie arbeiten an einem Projekt in einem Git-Repository namens `https://github.com/labex-labs/git-playground.git`. Sie haben zwei Branches namens `feature-1` und `feature-2`. Sie müssen die Datei `hello.txt` vom Branch `feature-1` in den Branch `feature-2` kopieren.

1. Klone das Repository:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigiere zum Verzeichnis und konfiguriere die Identität:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Erstelle und wechsle zum Branch `feature-1` und erstelle eine Textdatei namens `hello.txt` und schreibe die Zeichenfolge "hello,world" hinein und commite die Datei mit der Nachricht "add hello.txt":

```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

4. Erstelle und wechsle zum Branch `feature-2` nachdem du zum Branch `master` gewechselt bist:

```shell
git checkout master
git checkout -b feature-2
```

5. Kopiere die Datei `hello.txt` vom Branch `feature-1` in den Branch `feature-2` und commite sie mit der Commit-Nachricht "copy hello.txt":

```shell
git checkout feature-1 hello.txt
git commit -am "copy hello.txt"
```

6. Verifiziere, dass die Datei `hello.txt` in den Branch `feature-2` kopiert wurde:

```shell
ll
```

Du solltest die Datei `hello.txt` in der Liste der Dateien im Branch `feature-2` sehen:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
