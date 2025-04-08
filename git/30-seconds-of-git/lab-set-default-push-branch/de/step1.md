# Standard-Push-Branch-Namen festlegen

Wenn Sie Änderungen in ein Remote-Repository pushen, verwendet Git den Namen des aktuellen lokalen Branches als Standardnamen für den Remote-Branch. Manchmal möchten Sie jedoch Ihre Änderungen in einen anderen Branch pushen. In diesem Fall müssten Sie den Namen des Remote-Branches jedes Mal explizit angeben, wenn Sie Ihre Änderungen pushen. Dies kann mühsam und fehleranfällig sein, insbesondere wenn Sie mit mehreren Branches arbeiten.

Um dieses Lab zu absolvieren, verwenden Sie das Git-Repository `git-playground` aus Ihrem GitHub-Account, das von einem Fork von `https://github.com/labex-labs/git-playground.git` stammt. Folgen Sie den Schritten unten, um den Standard-Push-Branch-Namen festzulegen:

1. Klonen Sie das Repository mit dem folgenden Befehl:
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. Wechseln Sie in das Repository-Verzeichnis:
   ```
   cd git-playground
   ```
3. Legen Sie den Standard-Push-Branch-Namen auf den Namen des aktuellen lokalen Branches fest:
   ```
   git config push.default current
   ```
4. Erstellen Sie einen neuen Branch und wechseln Sie zu ihm:
   ```
   git checkout -b my-branch
   ```
5. Machen Sie einige Änderungen am Repository und committen Sie sie:
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. Pushen Sie Ihre Änderungen in das Remote-Repository:
   ```
   git push -u
   ```
   Git wird Ihre Änderungen in einen Branch namens `my-branch` im Remote-Repository pushen.

Dies ist das Ergebnis von `git log`:

```shell

ADD hello.txt
```
