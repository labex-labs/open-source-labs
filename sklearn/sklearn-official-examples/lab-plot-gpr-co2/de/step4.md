# Interpretation der Kernel-Hyperparameter

Jetzt können wir uns die Hyperparameter des Kerns ansehen.

```python
gaussian_process.kernel_
```

Somit wird der größte Teil des Zielsignals, mit dem Mittelwert subtrahiert, durch einen langfristigen Anstiegstrend von etwa 45 ppm und eine Längenskala von etwa 52 Jahren erklärt. Die periodische Komponente hat eine Amplitude von etwa 2,6 ppm, eine Abklingzeit von etwa 90 Jahren und eine Längenskala von etwa 1,5. Die lange Abklingzeit zeigt an, dass wir eine Komponente haben, die sehr nahe an einer saisonalen Periodizität ist. Der korrelierte Rauschen hat eine Amplitude von etwa 0,2 ppm mit einer Längenskala von etwa 0,12 Jahren und einen Weißrauschenbeitrag von etwa 0,04 ppm. Somit ist das gesamte Rauschlevel sehr klein, was darauf hindeutet, dass die Daten sehr gut durch das Modell erklärt werden können.
