# Zusammenfassung

In diesem Lab haben Sie Ihre ersten Ubuntu-, Nginx- und MongoDB-Container erstellt.

Wichtige Erkenntnisse

- Container bestehen aus Linux-Namespaces und Kontrollgruppen, die Isolation von anderen Containern und dem Host gewährleisten.
- Aufgrund der Isolationseigenschaften von Containern können Sie viele Container auf einem einzelnen Host planen, ohne sich um konfligierende Abhängigkeiten zu sorgen. Dies erleichtert es, mehrere Container auf einem einzelnen Host auszuführen: die zu diesem Host zugewiesenen Ressourcen optimal zu nutzen und letztendlich Kosten für Server zu sparen.
- Vermeiden Sie die Verwendung unverifizierten Inhalts aus dem Docker Store, wenn Sie eigene Bilder entwickeln, da diese Bilder möglicherweise Sicherheitslücken oder sogar Schadsoftware enthalten können.
- Container enthalten alles, was sie zur Ausführung der Prozesse innerhalb von ihnen benötigen, sodass es nicht erforderlich ist, zusätzliche Abhängigkeiten direkt auf Ihrem Host zu installieren.
