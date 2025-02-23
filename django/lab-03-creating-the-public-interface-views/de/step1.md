# Überblick

Eine Ansicht ist eine "Art" von Webseite in Ihrer Django-Anwendung, die im Allgemeinen eine bestimmte Funktion erfüllt und eine bestimmte Vorlage hat. Beispielsweise könnte eine Blog-Anwendung die folgenden Ansichten haben:

- Blog-Hauptseite - zeigt die neuesten Einträge an.
- Eintrags-"Detail"-Seite - Permalink-Seite für einen einzelnen Eintrag.
- Jahresarchivseite - zeigt alle Monate mit Einträgen im angegebenen Jahr an.
- Monatsarchivseite - zeigt alle Tage mit Einträgen im angegebenen Monat an.
- Tagesarchivseite - zeigt alle Einträge am angegebenen Tag an.
- Kommentaraktion - behandelt das Absenden von Kommentaren zu einem angegebenen Eintrag.

In unserer Umfrageanwendung werden wir die folgenden vier Ansichten haben:

- Frage-"Index"-Seite - zeigt die neuesten Fragen an.
- Frage-"Detail"-Seite - zeigt den Frage-Text an, ohne Ergebnisse, aber mit einem Formular zum Abstimmen.
- Frage-"Ergebnisse"-Seite - zeigt die Ergebnisse für eine bestimmte Frage an.
- Abstimmungsaktion - behandelt das Abstimmen für eine bestimmte Wahl in einer bestimmten Frage.

In Django werden Webseiten und anderer Inhalt durch Ansichten bereitgestellt. Jede Ansicht wird durch eine Python-Funktion (oder Methode, im Falle von klassenbasierten Ansichten) repräsentiert. Django wird eine Ansicht auswählen, indem es die angeforderte URL untersucht (genauer gesagt den Teil der URL nach dem Domainnamen).

In Ihrer Zeit im Internet haben Sie möglicherweise solche Schönheiten wie `ME2/Sites/dirmod.htm?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B` kennen gelernt. Sie werden sich freuen zu hören, dass Django uns viel elegantere _URL-Muster_ als das erlaubt.

Ein URL-Muster ist die allgemeine Form einer URL - beispielsweise: `/newsarchive/<year>/<month>/.`

Um von einer URL zu einer Ansicht zu gelangen, verwendet Django sogenannte 'URL-Konfigurationen'. Eine URL-Konfiguration bildet URL-Muster auf Ansichten ab.

Dieser Tutorial bietet grundlegende Anweisungen zur Verwendung von URL-Konfigurationen, und Sie können sich auf `/topics/http/urls` für weitere Informationen beziehen.
