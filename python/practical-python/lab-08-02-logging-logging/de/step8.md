# Übung 8.3: Hinzufügen von Protokollierung zu einem Programm

Um der Protokollierung in einer Anwendung hinzuzufügen, müssen Sie ein Mechanismus haben, um das Protokollierungsmodul im Hauptmodul zu initialisieren. Ein Möglichkeit dazu ist, Code für die Einrichtung wie folgt zu verwenden:

    # This file sets up basic configuration of the logging module.
    # Change settings here to adjust logging output as needed.
    import logging
    logging.basicConfig(
        filename = 'app.log',            # Name der Protokolldatei (lassen Sie weg, um stderr zu verwenden)
        filemode = 'w',                  # Dateimodus (verwenden Sie 'a', um anzuhängen)
        level    = logging.WARNING,      # Protokollierungslevel (DEBUG, INFO, WARNING, ERROR oder CRITICAL)
    )

Wiederum müssen Sie diesen Code an einem Ort in den Startschritten Ihres Programms platzieren. Beispielsweise, wo würden Sie diesen Code in Ihrem `report.py`-Programm platzieren?
