# Anpassen der Strichmarkenbeschriftungen und Achsenbeschriftungen für jede primäre 3D-Ansichtsebene

Wir passen die Strichmarkenbeschriftungen und Achsenbeschriftungen für jede primäre 3D-Ansichtsebene an, um unnötige Beschriftungen zu entfernen.

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```
