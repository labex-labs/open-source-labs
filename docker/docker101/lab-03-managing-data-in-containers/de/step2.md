# Bind Mounts

Docker empfiehlt die `mount`-Syntax gegenüber der `volume`-Syntax. Bind Mounts haben im Vergleich zu Volumes eingeschränkte Funktionen. Eine Datei oder ein Verzeichnis wird beim Mounten in einen Container anhand seines vollständigen Pfads auf der Hostmaschine referenziert. Bind Mounts setzen voraus, dass das Dateisystem der Hostmaschine eine bestimmte Verzeichnisstruktur zur Verfügung hat, und Sie können die Docker-Befehlszeilenschnittstelle (CLI) nicht verwenden, um Bind Mounts zu verwalten. Beachten Sie, dass Bind Mounts das Hostdateisystem über Prozesse, die in einem Container laufen, verändern können.

Anstatt die `-v`-Syntax mit drei durch Doppelpunkte getrennten Feldern zu verwenden, ist die `mount`-Syntax ausführlicher und verwendet mehrere `Schlüssel-Wert`-Paare:

- type: bind, volume oder tmpfs,
- source: Pfad zur Datei oder zum Verzeichnis auf der Hostmaschine,
- destination: Pfad im Container,
- readonly,
- bind-propagation: rprivate, private, rshared, shared, rslave, slave,
- consistency: consistent, delegated, cached,
- mount.

```bash
cd /home/labex/project
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
```

Geben Sie den Befehl im Container ein:

```
echo "hello busybox" > /data/hi.txt
exit
```

Überprüfen Sie, ob die Datei auf der Hostmaschine erstellt wurde.

```
cat data/hi.txt
```
