# Grad in Radiant Herausforderung

## Problem

Schreiben Sie eine Funktion `grad_in_rad(grad)`, die einen Winkel in Grad als Argument nimmt und den Winkel in Radiant zurückgibt. Ihre Funktion sollte die folgende Formel verwenden, um Grad in Radiant umzurechnen:

```
radiant = (grad * pi) / 180.0
```

wobei `pi` ein konstanter Wert ist, der das Verhältnis der Kreisumfangs zu seinem Durchmesser darstellt (ungefähr 3,14159).

Ihre Funktion sollte den Winkel in Radiant auf 4 Nachkommastellen gerundet zurückgeben.

## Beispiel

```python
grad_in_rad(180) # gibt 3,1416 zurück
grad_in_rad(90) # gibt 1,5708 zurück
grad_in_rad(45) # gibt 0,7854 zurück
```
