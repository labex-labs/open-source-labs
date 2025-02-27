# Testorganisation

Wie am Anfang des Kapitels erwähnt, ist das Testen eine komplexe Disziplin, und verschiedene Menschen verwenden unterschiedliche Terminologien und Organisationen. Die Rust-Community denkt sich Tests in zwei Hauptkategorien: Einheitstests und Integrations-Tests. _Einheitstests_ sind klein und fokussierter, testen jeweils ein Modul isoliert und können private Schnittstellen testen. _Integrations-Tests_ sind vollständig extern zu Ihrer Bibliothek und verwenden Ihren Code auf die gleiche Weise wie jeder andere externe Code, indem sie nur die öffentliche Schnittstelle verwenden und möglicherweise mehrere Module pro Test durchlaufen.

Es ist wichtig, beide Arten von Tests zu schreiben, um sicherzustellen, dass die Teile Ihrer Bibliothek das tun, was Sie von ihnen erwarten, separat und zusammen.
