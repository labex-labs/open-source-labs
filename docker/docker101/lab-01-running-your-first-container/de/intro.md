# Einführung

In diesem Lab werden Sie Ihren ersten Docker-Container ausführen.

Container sind einfach ein Prozess (oder eine Gruppe von Prozessen), der in Isolation läuft. Die Isolation wird über Linux-Namespaces, Control Groups (cgroups), seccomp und SELinux erreicht. Beachten Sie, dass Linux-Namespaces und Control Groups in den Linux-Kernel integriert sind! Abgesehen vom Linux-Kernel selbst ist es ansonsten nichts Besonderes an Containern.

Was Containern nützlich macht, ist die Tooling, die sich um sie herum entwickelt hat. Für diese Labs werden wir Docker verwenden, das ein weit verbreitetes Tool zur Verwendung von Containern zum Erstellen von Anwendungen ist. Docker bietet Entwicklern und Betreibern eine freundliche Schnittstelle, um Container auf jeder Umgebung mit einem Docker-Engine zu erstellen, zu verschiffen und auszuführen. Da der Docker-Client einen Docker-Engine erfordert, ist eine Alternative die Verwendung von [Podman](https://podman.io/), einem daemonlosen Container-Engine, um [OCI](https://opencontainers.org/)-Container zu entwickeln, zu verwalten und auszuführen und um Container als root oder im rootless-Modus auszuführen. Aus diesen Gründen empfehlen wir Podman, aber aufgrund der Verbreitung wird in diesem Lab immer noch Docker verwendet.

Im ersten Teil dieses Labs werden wir unseren ersten Container ausführen und lernen, wie wir ihn untersuchen können. Wir werden die Namespace-Isolation, die wir aus dem Linux-Kernel erhalten, beobachten können.

Nachdem wir unseren ersten Container ausgeführt haben, werden wir uns anderen Anwendungen von Containern widmen. Sie können viele Beispiele davon im Docker Store finden, und wir werden mehrere verschiedene Typen von Containern auf dem gleichen Host ausführen. Dies wird uns die Vorteile der Isolation zeigen - dass wir mehrere Container auf dem gleichen Host ohne Konflikte ausführen können.

Wir werden in diesem Lab einige Docker-Befehle verwenden. Für die vollständige Dokumentation zu den verfügbaren Befehlen schauen Sie sich die [offizielle Dokumentation](https://docs.docker.com/) an.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Dies ist ein Guided Lab, das schrittweise Anweisungen bietet, um Ihnen beim Lernen und Üben zu helfen. Befolgen Sie die Anweisungen sorgfältig, um jeden Schritt abzuschließen und praktische Erfahrungen zu sammeln. Historische Daten zeigen, dass dies ein Labor der Stufe <span class="text-green-600 dark:text-green-400">Anfänger</span> mit einer Abschlussquote von <span class="text-green-600 dark:text-green-400">90%</span> ist. Es hat eine positive Bewertungsrate von <span class="text-primary-600 dark:text-primary-400">92%</span> von den Lernenden erhalten.
</div>
