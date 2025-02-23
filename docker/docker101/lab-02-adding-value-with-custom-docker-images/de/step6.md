# Understanding Image Layers

Eine der wichtigsten Designmerkmale von Docker ist die Verwendung des Union-Dateisystems.

Betrachten Sie die `Dockerfile`, die wir zuvor erstellt haben:

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
```

Jede dieser Zeilen ist eine Schicht. Jede Schicht enthält nur die Änderungen, Differenzen oder Änderungen gegenüber den vorherigen Schichten. Um diese Schichten zu einem einzelnen laufenden Container zusammenzufügen, verwendet Docker das `Union-Dateisystem`, um die Schichten transparent zu überlagern und in einer einzigen Ansicht zu kombinieren.

Jede Schicht des Images ist `schreibgeschützt`, mit Ausnahme der obersten Schicht, die für den laufenden Container erstellt wird. Die schreibende Container-Schicht implementiert das "Copy-on-Write"-Verfahren, was bedeutet, dass Dateien, die in den unteren Image-Schichten gespeichert sind, nur dann in die schreibende Container-Schicht kopiert werden, wenn Änderungen an diesen Dateien vorgenommen werden. Die Änderungen werden dann in der laufenden Container-Schicht gespeichert. Die "Copy-on-Write"-Funktion ist sehr schnell und hat in fast allen Fällen keinen merklichen Effekt auf die Leistung. Sie können überprüfen, welche Dateien in die Containerebene kopiert wurden, mit dem Befehl `docker diff`. Weitere Informationen über die Verwendung von `docker diff` finden Sie [hier](https://docs.docker.com/engine/reference/commandline/diff/).

![understanding image layers](../assets/lab2_understanding_image_layers_1.png)

Da die Image-Schichten `schreibgeschützt` sind, können sie von Images und laufenden Containern geteilt werden. Beispielsweise würde das Erstellen einer neuen Python-App mit ihrer eigenen Dockerfile mit ähnlichen Basis-Schichten alle gemeinsamen Schichten mit der ersten Python-App teilen.

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app2.py"]
COPY app2.py /app2.py
```

![understanding image layers](../assets/lab2_understanding_image_layers_2.png)

Sie können auch die Teilung von Schichten erleben, wenn Sie mehrere Container aus dem gleichen Image starten. Da die Container die gleichen schreibgeschützten Schichten verwenden, können Sie sich vorstellen, dass das Starten von Containern sehr schnell ist und einen sehr geringen Speicherbedarf auf dem Host hat.

Sie werden möglicherweise bemerken, dass es doppelte Zeilen in dieser Dockerfile und der Dockerfile gibt, die Sie zu Beginn dieses Labs erstellt haben. Obwohl dies ein sehr einfaches Beispiel ist, können Sie die gemeinsamen Zeilen beider Dockerfiles in eine "Basis"-Dockerfile ziehen, auf die Sie dann in jeder Ihrer Kind-Dockerfiles mit dem `FROM`-Befehl verweisen können.

Die Image-Schichtung ermöglicht den Docker-Caching-Mechanismus für Builds und Pushes. Beispielsweise zeigt die Ausgabe Ihres letzten `docker push` an, dass einige der Schichten Ihres Images bereits auf dem Docker Hub existieren.

```bash
$ docker push $DOCKERHUB_USERNAME/python-hello-world
```

Um genauer auf die Schichten zu schauen, können Sie den Befehl `docker image history` des Python-Images verwenden, das wir erstellt haben.

```bash
$ docker image history python-hello-world
```

Jede Zeile stellt eine Schicht des Images dar. Sie werden feststellen, dass die obersten Zeilen mit Ihrer erstellten Dockerfile übereinstimmen und die Zeilen darunter aus dem übergeordneten Python-Image stammen. Machen Sie sich keine Sorgen um die "\<missing\>"-Tags. Dies sind immer noch normale Schichten; sie haben nur keine ID von dem Docker-System erhalten.
