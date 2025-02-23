# Summary

In diesem Lab haben Sie begonnen, Wert zu schaffen, indem Sie Ihre eigenen benutzerdefinierten Docker-Container erstellt haben.

Wichtige Erkenntnisse:

- Die Dockerfile ist die Methode, um reproduzierbare Builds für Ihre Anwendung zu erstellen und um Ihre Anwendung mit Docker in die CI/CD-Pipeline zu integrieren.
- Docker-Images können in allen Ihren Umgebungen über einen zentralen Registrierungsdienst zur Verfügung gestellt werden. Der Docker Hub ist ein Beispiel für einen Registrierungsdienst, aber Sie können auch Ihren eigenen Registrierungsdienst auf Servern, die Sie steuern, bereitstellen.
- Docker-Images enthalten alle Abhängigkeiten, die erforderlich sind, um eine Anwendung innerhalb des Images auszuführen. Dies ist nützlich, da wir keine Umgebungsabweichungen (Versionsunterschiede) mehr berücksichtigen müssen, wenn wir von Abhängigkeiten abhängen, die auf jeder Umgebung installiert sind, auf die wir bereitstellen.
- Docker nutzt das Union-Dateisystem und "Copy on Write", um Schichten von Images zu wiederverwenden. Dies verringert den Speicherbedarf für Images und erhöht die Leistung beim Start von Containern erheblich.
- Image-Schichten werden vom Docker-Build- und -Push-System zwischengespeichert. Es ist nicht erforderlich, Image-Schichten neu zu bauen oder erneut zu pushen, die bereits auf dem gewünschten System vorhanden sind.
- Jede Zeile in einer Dockerfile erstellt eine neue Schicht, und aufgrund des Schichtcaches sollten die Zeilen, die häufiger geändert werden (z.B. Hinzufügen von Quellcode zu einem Image), am Ende der Datei aufgelistet werden.
