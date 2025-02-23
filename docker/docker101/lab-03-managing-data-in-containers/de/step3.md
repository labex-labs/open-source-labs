# [Optional] OverlayFS

OverlayFS ist eine Implementierung eines `Union Mount Dateisystems` für Linux. Um zu verstehen, was ein Docker-Volume ist, hilft es, zu verstehen, wie Layer und das Dateisystem in Docker funktionieren.

Um einen Container zu starten, nimmt Docker das schreibgeschützte Image und erstellt eine neue schreibende Schicht darüber. Um die Layer als eine Einheit zu betrachten, verwendet Docker ein Union File System oder OverlayFS (Overlay File System), speziell den Speicherdreiber `overlay2`.

Um die von Docker auf dem Host verwalteten Dateien zu sehen, müssen Sie Zugang zum Docker-Prozessdateisystem haben. Mit den Flags `--privileged` und `--pid=host` können Sie vom Inneren eines Containers wie `busybox` aus auf den Prozess-ID-Namespace des Hosts zugreifen. Anschließend können Sie zu dem Verzeichnis `/var/lib/docker/overlay2` von Docker navigieren, um die heruntergeladenen Layer zu sehen, die von Docker verwaltet werden.

Um die aktuelle Liste der Layer in Docker anzuzeigen:

```bash
$ docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2
total 16
drwx------ 3 root root 4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------ 5 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------ 4 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------ 2 root root 4096 Sep 25 19:44 l

/ # exit
```

Ziehen Sie das `ubuntu`-Image herunter und überprüfen Sie es erneut:

```bash
docker pull ubuntu
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
```

Geben Sie den Befehl ein, um die Liste der Layer erneut anzuzeigen:

```
ls -l /var/lib/docker/overlay2/ & exit
```

Sie sehen, dass beim Herunterladen des `ubuntu`-Images implizit 4 neue Layer heruntergeladen wurden:

- a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
- d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
- dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
- f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709

Der Speicherdreiber `overlay2` legt im Wesentlichen verschiedene Verzeichnisse auf dem Host übereinander und stellt sie als ein einzelnes Verzeichnis dar.

- Basisschicht oder lowerdir,
- `diff`-Schicht oder upperdir,
- Overlay-Schicht (Benutzeransicht) und
- `work`-Verzeichnis.

OverlayFS bezieht sich auf die unteren Verzeichnisse als `lowerdir`, das die Basisimage und die schreibgeschützten (R/O) Layer enthält, die heruntergeladen werden.

Das obere Verzeichnis wird `upperdir` genannt und ist die schreibende (R/W) Container-Schicht.

Die vereinigte Ansicht oder die `overlay`-Schicht wird `merged` genannt.

Schließlich ist ein `workdir` erforderlich, das ein leeres Verzeichnis ist, das von overlay für interne Zwecke verwendet wird.

Der `overlay2`-Treiber unterstützt bis zu 128 untere OverlayFS-Layer. Das `l`-Verzeichnis enthält verkürzte Layer-Identifikatoren als symbolische Links.

![Overlay2 Storage Driver](../assets/overlay2-driver.png)

Bereinigen:

```bash
docker system prune -a
clear
```
