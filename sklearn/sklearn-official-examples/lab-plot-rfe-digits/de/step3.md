# Bewerte die Features

Nachdem die Daten an das RFE-Objekt angepasst wurden, können wir die Features nach ihrer Wichtigkeit bewerten. Wir werden das Attribut `ranking_` des RFE-Objekts verwenden, um die Feature-Bewertungen zu erhalten. Wir werden auch die Bewertungen umformen, um der Form der ursprünglichen Bilder zu entsprechen.

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```
