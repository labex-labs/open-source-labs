# Ein Submodul löschen

Sie haben ein Git-Repository, das ein Submodul namens `sha1collisiondetection` enthält. Sie möchten dieses Submodul aus Ihrem Repository löschen.

Für dieses Lab verwenden wir das Git-Repository namens `https://github.com/git/git`. Dieses Repository enthält ein Submodul namens `sha1collisiondetection`.

Um das Submodul `sha1collisiondetection` aus dem Repository zu löschen, führen Sie die folgenden Schritte aus:

1. Öffnen Sie Ihr Terminal und navigieren Sie zum Stammverzeichnis Ihres Git-Repositorys:
   ```
   cd git
   ```
2. Führen Sie den folgenden Befehl aus, um das Submodul `sha1collisiondetection` abzumelden:
   ```
   git submodule deinit -f -- sha1collisiondetection
   ```
3. Führen Sie den folgenden Befehl aus, um das Verzeichnis des Submoduls `sha1collisiondetection` zu entfernen:
   ```
   rm -rf.git/modules/sha1collisiondetection
   ```
4. Führen Sie den folgenden Befehl aus, um den Arbeitsbaum des Submoduls `sha1collisiondetection` zu entfernen:
   ```
   git rm -f sha1collisiondetection
   ```

Nach diesen Schritten wird das Submodul `sha1collisiondetection` aus Ihrem Git-Repository entfernt. Wenn Sie den Befehl `git submodule status` ausführen, erhalten Sie keine Informationen über das Submodul.
