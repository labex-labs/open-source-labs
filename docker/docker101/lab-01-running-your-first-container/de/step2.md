# Führen Sie Ihren ersten Container aus

Wir werden die Docker-Befehlszeilenschnittstelle (CLI) verwenden, um unseren ersten Container auszuführen.

Öffnen Sie ein Terminal auf der LabEx VM.

Führen Sie den Befehl aus.

```bash
docker container run -t ubuntu top
```

Verwenden Sie den Befehl `docker container run`, um einen Container mit dem `ubuntu`-Bild mithilfe des `top`-Befehls auszuführen. Das Flag `-t` weist einen Pseudo-TTY zu, den wir für die korrekte Funktion von `top` benötigen.

```bash
$ docker container run -it ubuntu top
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
aafe6b5e13de: Pull complete
0a2b43a72660: Pull complete
18bdd1e546d2: Pull complete
8198342c3e05: Pull complete
f56970a44fd4: Pull complete
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Status: Downloaded newer image for ubuntu:latest
```

Der Befehl `docker run` führt zunächst einen `docker pull` aus, um das `ubuntu`-Bild auf Ihren Host herunterzuladen. Nachdem es heruntergeladen ist, startet es den Container. Die Ausgabe für den laufenden Container sollte so aussehen:

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top` ist ein Linux-Werkzeug, das die Prozesse auf einem System ausgibt und sie nach der Ressourcenverbrauch sortiert. Beachten Sie, dass in dieser Ausgabe nur ein einziger Prozess ist: es ist der `top`-Prozess selbst. Wir sehen in dieser Liste keine anderen Prozesse von unserem Host, da aufgrund der PID-Namespace-Isolation.

Container verwenden Linux-Namespaces, um die Isolation von Systemressourcen von anderen Containern oder dem Host zu gewährleisten. Der PID-Namespace bietet Isolation für Prozess-IDs. Wenn Sie `top` innerhalb des Containers ausführen, werden Sie feststellen, dass es die Prozesse innerhalb des PID-Namespace des Containers zeigt, was sich stark unterscheidet von dem, was Sie sehen würden, wenn Sie `top` auf dem Host ausgeführt hätten.

Auch wenn wir das `ubuntu`-Bild verwenden, ist es wichtig zu beachten, dass unser Container keinen eigenen Kernel hat. Er verwendet den Kernel des Hosts, und das `ubuntu`-Bild wird nur verwendet, um das Dateisystem und die Tools zur Verfügung zu stellen, die auf einem Ubuntu-System verfügbar sind.

Untersuchen Sie den Container mit `docker container exec`

Der Befehl `docker container exec` ist eine Möglichkeit, mit einem neuen Prozess in die Namespaces eines laufenden Containers einzutauchen.

Öffnen Sie ein neues Terminal. Wählen Sie `Terminal` > `New Terminal`.

Im neuen Terminal verwenden Sie den Befehl `docker container ls`, um die ID des gerade erstellten laufenden Containers zu erhalten.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

Verwenden Sie dann diese ID, um `bash` innerhalb dieses Containers mithilfe des Befehls `docker container exec` auszuführen. Da wir `bash` verwenden und mit diesem Container von unserem Terminal interagieren möchten, verwenden wir die Flags `-it`, um im interaktiven Modus auszuführen, während ein Pseudo-Terminal zugewiesen wird.

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

Und voilà! Wir haben gerade den Befehl `docker container exec` verwendet, um mit unserem `bash`-Prozess in die Namespaces unseres Containers einzutauchen. Das Verwenden von `docker container exec` mit `bash` ist ein häufiges Muster, um einen Docker-Container zu untersuchen.

Beachten Sie die Änderung am Präfix Ihres Terminals. z.B. `root@b3ad2a23fab3:/`. Dies ist ein Hinweis darauf, dass wir `bash` "innerhalb" unseres Containers ausführen.

**Hinweis**: Dies ist nicht dasselbe wie das SSH in einen separaten Host oder eine VM. Wir brauchen keinen SSH-Server, um mit einem `bash`-Prozess zu verbinden. Denken Sie daran, dass Container kernelbasierte Funktionen verwenden, um Isolation zu erreichen, und dass Container auf dem Kernel laufen. Unser Container ist einfach eine Gruppe von Prozessen, die in Isolation auf dem gleichen Host laufen, und wir können `docker container exec` verwenden, um mit dem `bash`-Prozess in diese Isolation einzutauchen. Nachdem `docker container exec` ausgeführt wurde, umfasst die Gruppe von Prozessen, die in Isolation laufen (d.h. unser Container), `top` und `bash`.

Im selben Terminal führen Sie `ps -ef` aus, um die laufenden Prozesse zu untersuchen.

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34? 00:00:00 top
root 17 0 0 21:06? 00:00:00 bash
root 27 17 0 21:14? 00:00:00 ps -ef
```

Sie sollten nur den `top`-Prozess, den `bash`-Prozess und unseren `ps`-Prozess sehen.

Zum Vergleich verlassen Sie den Container und führen Sie `ps -ef` oder `top` auf dem Host aus. Diese Befehle funktionieren auf Linux oder Mac. Für Windows können Sie die laufenden Prozesse mit `tasklist` untersuchen.

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# Lots of processes!
```

_Technischer Tieftauchen_
PID ist nur einer der Linux-Namespaces, der Containern die Isolation von Systemressourcen bietet. Andere Linux-Namespaces umfassen:

- MNT - Mounten und Entfernen von Verzeichnissen ohne die anderen Namespaces zu beeinflussen
- NET - Container haben ihren eigenen Netzwerkstack
- IPC - Isolierte interprozessuale Kommunikationsmechanismen wie Nachrichtenwarteschlangen.
- User - Isolierter Ansicht der Benutzer auf dem System
- UTC - Setzen Sie den Hostnamen und die Domäne pro Container

Diese Namespaces bieten zusammen die Isolation für Container, die es ihnen ermöglichen, gemeinsam sicher zu laufen und ohne Konflikt mit anderen Containern, die auf dem gleichen System laufen. Als Nächstes werden wir verschiedene Anwendungen von Containern demonstrieren und den Vorteil der Isolation, wenn wir mehrere Container auf dem gleichen Host ausführen.

**Hinweis**: Namespaces sind eine Funktion des **Linux**-Kernels. Aber Docker ermöglicht es Ihnen, Container auf Windows und Mac auszuführen... wie funktioniert das? Das Geheimnis ist, dass in das Docker-Produkt oder den Docker-Engine ein Linux-Subsystem eingebettet ist. Docker hat dieses Linux-Subsystem in ein neues Projekt open-sourced: [LinuxKit](https://github.com/linuxkit/linuxkit). Ein Vorteil der Verwendung der Docker-Tooling mit Containern ist, dass Sie Container auf vielen verschiedenen Plattformen ausführen können.

Zusätzlich zu der Ausführung von Linux-Containern auf Windows mithilfe eines Linux-Subsystems sind native Windows-Container jetzt möglich, dank der Erstellung von Container-Primitiven auf dem Windows-OS. Native Windows-Container können auf Windows 10 oder Windows Server 2016 oder neuer ausgeführt werden.

**Hinweis**: Wenn Sie diese Übung in einem containerisierten Terminal ausführen und den Befehl `ps -ef` im Terminal ausführen, werden Sie nach dem Beenden des `exec`-Befehls immer noch eine begrenzte Anzahl von Prozessen sehen. Sie können versuchen, den Befehl `ps -ef` in einem Terminal auf Ihrem lokalen Computer auszuführen, um alle Prozesse zu sehen.

Bereinigen Sie den Container, der die `top`-Prozesse ausführt, indem Sie `<ctrl>-c` drücken, listen Sie alle Container auf und entfernen Sie die Container anhand ihrer ID.

```bash
docker ps -a

docker rm <CONTAINER ID>
```
