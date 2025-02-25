# Zeige fett kursiv

Als Bonus können wir auch Text mit sowohl fettem als auch kursivem Stil anzeigen. Wir werden die `fig.text()`-Methode verwenden, um den Text mit dem entsprechenden Stil, Gewicht und Größe anzuzeigen.

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```
