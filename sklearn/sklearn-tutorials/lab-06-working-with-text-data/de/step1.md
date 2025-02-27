# Laden der Text-Daten

Zunächst müssen wir die Text-Daten laden, mit denen wir arbeiten werden. Wir werden den 20 Newsgroups-Datensatz verwenden, der Nachrichtenartikel zu zwanzig verschiedenen Themen enthält. Um den Datensatz zu laden, können wir die Funktion `fetch_20newsgroups` aus scikit-learn verwenden.

```python
from sklearn.datasets import fetch_20newsgroups

# Lade den Datensatz
categories = ['alt.atheism','soc.religion.christian', 'comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

Jetzt haben wir die Daten geladen, und wir können ihre Struktur und Inhalt untersuchen.
