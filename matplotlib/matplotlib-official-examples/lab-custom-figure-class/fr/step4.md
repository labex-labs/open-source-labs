# Tracez les données à l'aide de la sous-classe de figure personnalisée

Utilisez la fonction `plt.figure()` pour tracer les données à l'aide de la sous-classe de figure personnalisée `WatermarkFigure`. Dans cet exemple, nous allons ajouter le texte de filigrane "projet" au tracé.

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```
