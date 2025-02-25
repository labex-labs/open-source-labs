# Daten definieren

Als nächstes müssen wir die Daten definieren, die geplottet werden sollen. In diesem Beispiel haben wir einen Satz von Beobachtungen mit vier Variablen: Name, Winkelrichtbewegung, Fehler der Winkelrichtbewegung und Entfernung. Wir werden die Winkelrichtbewegung in lineare Geschwindigkeit umrechnen und sie gegen die FWHM (vollweite bei halber Höhe) der Beobachtungen aufzeichnen.

```python
obs = [["01_S1", 3.88, 0.14, 1970, 63],
       ["01_S4", 5.6, 0.82, 1622, 150],
       ["02_S1", 2.4, 0.54, 1570, 40],
       ["03_S1", 4.1, 0.62, 2380, 170]]

# Umrechnungsfaktor von Winkelrichtbewegung in lineare Geschwindigkeit
pm_to_kms = 1./206265.*2300*3.085e18/3.15e7/1.e5
```
