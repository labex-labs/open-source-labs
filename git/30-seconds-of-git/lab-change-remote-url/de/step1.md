# Ändern der Remote-URL

Sie haben ein Repository von GitHub geklont und einige Änderungen daran vorgenommen. Nun stellen Sie jedoch fest, dass Sie die URL des Remote-Repositorys ändern müssen. Dies könnte daran liegen, dass das ursprüngliche Repository an einen anderen Ort verschoben wurde oder weil Sie Ihre Änderungen an ein anderes Remote-Repository pushen möchten. Ihre Aufgabe besteht darin, die Remote-URL des Repositorys mit Git-Befehlen zu ändern.

Sie müssen das Repository `https://github.com/labex-labs/git-playground` auf Ihren lokalen Computer klonen. Um die Remote-URL des Repositorys zu `https://github.com/your-username/git-playground` zu ändern, folgen Sie diesen Schritten:

1. Öffnen Sie ein Terminal oder eine Befehlszeile, klonen Sie das Repository und navigieren Sie zum lokalen Repository.
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. Verwenden Sie den folgenden Befehl, um die aktuelle Remote-URL anzuzeigen:
   ```
   git remote -v
   ```
3. Verwenden Sie den folgenden Befehl, um die Remote-URL auf die neue URL zu ändern:
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. Verwenden Sie den folgenden Befehl, um zu überprüfen, ob die Remote-URL geändert wurde:
   ```
   git remote -v
   ```

Die Ausgabe sollte die neue URL anstelle der alten anzeigen:

![Updated remote URL output](../assets/challenge-change-remote-url-step1-1.png)
