# Einführung in die automatisierte Tests

## Was sind automatisierte Tests?

Tests sind Routinen, die die Funktionsweise Ihres Codes überprüfen.

Das Testen erfolgt auf verschiedenen Ebenen. Einige Tests können sich auf einen winzigen Detailbereich beziehen („gibt eine bestimmte Modellmethode die erwarteten Werte zurück?“), während andere die Gesamtfunktionsweise der Software untersuchen („erzeugt eine Sequenz von Benutzereingaben auf der Website das gewünschte Ergebnis?“). Dies unterscheidet sich nicht von der Art des Tests, die Sie früher in `**Set Up the Database**` durchgeführt haben, indem Sie die `shell` verwendet haben, um das Verhalten einer Methode zu untersuchen, oder indem Sie die Anwendung ausgeführt und Daten eingegeben haben, um zu überprüfen, wie sie sich verhält.

Was bei _automatisierten_ Tests anders ist, ist, dass die Testarbeit vom System für Sie erledigt wird. Sie erstellen einmal eine Reihe von Tests, und wenn Sie Ihre App ändern, können Sie überprüfen, ob Ihr Code weiterhin wie ursprünglich geplant funktioniert, ohne dass Sie zeitaufwendiges manuelles Testen vornehmen müssen.

## Warum Sie Tests erstellen sollten

Warum sollten Sie Tests erstellen und warum gerade jetzt?

Sie mögen sich vielleicht denken, dass Sie schon genug auf dem Teller haben, indem Sie nur noch Python/Django lernen, und dass das Lernen und Tun noch eines weiteren Dings überwältigend und vielleicht sogar unnötig erscheint. Nach allem, was wir wissen, funktioniert unsere Umfrageanwendung derzeit problemlos; das Aufwand der Erstellung automatisierter Tests wird sie nicht funktionieren lassen. Wenn das Erstellen der Umfrageanwendung der letzte Schritt der Django-Programmierung ist, die Sie jemals ausführen werden, dann stimmt es, dass Sie nicht wissen müssen, wie automatisierte Tests erstellt werden. Wenn das jedoch nicht der Fall ist, ist jetzt ein ausgezeichneter Zeitpunkt, um zu lernen.

### Tests sparen Ihnen Zeit

Bis zu einem gewissen Punkt wird das „Überprüfen, ob es funktioniert“ ein zufriedenstellender Test sein. In einer komplexeren Anwendung können Sie zwischen den Komponenten zahlreiche komplexe Interaktionen haben.

Eine Änderung in einer dieser Komponenten kann unerwartete Auswirkungen auf das Verhalten der Anwendung haben. Das Überprüfen, ob es weiterhin „funktioniert“, kann bedeuten, dass Sie durch die Funktionalität Ihres Codes mit zwanzig verschiedenen Variationen Ihrer Testdaten laufen, um sicherzustellen, dass Sie nichts kaputt gemacht haben – kein guter Zeitverbrauch.

Dies trifft besonders zu, wenn automatisierte Tests dies für Sie in wenigen Sekunden erledigen können. Wenn etwas schiefgeht, helfen Ihnen Tests auch bei der Identifizierung des Codes, der das unerwartete Verhalten verursacht.

Manchmal kann es sich anfühlen, als wäre es eine Last, sich von Ihrer produktiven, kreativen Programmierarbeit zu lösen, um der langweiligen und unaufregenden Aufgabe der Schreiben von Tests zu begegnen, insbesondere wenn Sie wissen, dass Ihr Code ordnungsgemäß funktioniert.

Dennoch ist die Aufgabe des Schreibens von Tests viel erfüllender als Stunden am manuellen Testen Ihrer Anwendung oder am Versuch, die Ursache eines neu aufgetretenen Problems zu identifizieren.

### Tests identifizieren nicht nur Probleme, sondern verhindern sie auch

Es ist ein Fehler, Tests lediglich als einen negativen Aspekt der Entwicklung zu betrachten.

Ohne Tests kann der Zweck oder das beabsichtigte Verhalten einer Anwendung ziemlich undurchsichtig sein. Selbst wenn es Ihr eigener Code ist, werden Sie sich manchmal darin herumtappen, um herauszufinden, was er genau macht.

Tests ändern das; sie beleuchten Ihren Code von innen heraus, und wenn etwas schiefgeht, richten sie das Licht auf den Teil, der fehlerhaft ist – _auch wenn Sie nicht einmal bemerkt haben, dass etwas schiefgeht_.

### Tests machen Ihren Code attraktiver

Sie könnten ein brillantes Softwarestück erstellt haben, aber Sie werden feststellen, dass viele andere Entwickler es ablehnen, weil es keine Tests hat; ohne Tests vertrauen sie es nicht. Jacob Kaplan-Moss, einer der ursprünglichen Django-Entwickler, sagt: „Code ohne Tests ist von der Design her fehlerhaft.“

Der Grund, warum andere Entwickler Tests in Ihrer Software sehen möchten, bevor sie es ernst nehmen, ist noch ein weiterer Grund für Sie, anfangen, Tests zu schreiben.

### Tests helfen Teams zusammenzuarbeiten

Die vorherigen Punkte sind aus der Sicht eines einzelnen Entwicklers geschrieben, der eine Anwendung unterhält. Komplexe Anwendungen werden von Teams unterhalten. Tests gewährleisten, dass Kollegen Ihren Code nicht versehentlich kaputt machen (und dass Sie auch nicht den ihren ohne zu wissen). Wenn Sie als Django-Programmierer leben möchten, müssen Sie gut im Schreiben von Tests sein!
