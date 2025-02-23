# Einführung

Standardmäßig werden alle in einem Container erstellten Dateien auf einer beschreibbaren Container-Schicht gespeichert. Das bedeutet, dass:

- Wenn der Container nicht mehr existiert, gehen die Daten verloren,
- Die beschreibbare Schicht des Containers ist eng mit dem Hostcomputer verknüpft, und
- Um das Dateisystem zu verwalten, benötigen Sie einen Speicherdreiber, der ein Union-Dateisystem bereitstellt, indem er den Linux-Kernel verwendet. Dieser zusätzliche Abstraktionsschritt reduziert die Leistung im Vergleich zu `Data Volumes`, die direkt auf das Dateisystem schreiben.

Docker bietet zwei Optionen, um Dateien auf dem Hostcomputer zu speichern: `Volumes` und `Bind Mounts`. Wenn Sie Docker auf Linux ausführen, können Sie auch eine `tmpfs Mount` verwenden, und mit Docker auf Windows können Sie auch eine `benannte Pipe` verwenden.

![Types of Mounts](../assets/types-of-mounts.png)

- `Volumes` werden im von Docker verwalteten Hostdateisystem gespeichert.
- `Bind Mounts` können an beliebiger Stelle des Hostsystems gespeichert werden.
- `tmpfs Mounts` werden ausschließlich im Hostspeicher gespeichert.

Ursprünglich wurde das Flag `--mount` für Docker Swarm-Dienste verwendet, und das Flag `--volume` für einzelne Container. Ab Docker 17.06 und höher können Sie auch `--mount` für einzelne Container verwenden, und es ist im Allgemeinen expliziter und ausführlicher als `--volume`.
