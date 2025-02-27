# Einführung

In diesem Lab werden wir das Konzept von RAII (Resource Acquisition Is Initialization) in Rust erkunden, das die Initialisierung von Ressourcen erzwingt. Dies bedeutet, dass wenn Objekte außerhalb ihres Gültigkeitsbereichs gelangen, ihre Destruktoren aufgerufen werden und die von ihnen besitzten Ressourcen freigegeben werden, wodurch die Notwendigkeit der manuellen Arbeitsspeicherverwaltung eliminiert und Schutz vor Ressourcenleckfehlern gewährleistet wird. Wir werden auch über das `Drop`-Attribut in Rust lernen, das es ermöglicht, benutzerdefiniertes Destruktorkonzept für Typen zu implementieren, die dies erfordern.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
