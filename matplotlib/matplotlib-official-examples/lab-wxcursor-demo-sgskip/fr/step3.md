# Mettre à jour la barre de statut

Enfin, nous allons définir une méthode pour mettre à jour la barre de statut avec l'emplacement du curseur chaque fois que la souris se déplace sur le tracé.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
