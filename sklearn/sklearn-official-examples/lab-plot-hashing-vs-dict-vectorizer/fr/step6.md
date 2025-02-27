# Tracer les résultats

Nous allons tracer la vitesse des méthodes ci-dessus pour la vectorisation.

```python
import matplotlib.pyplot as plt

dict_count_vectorizers = {
    "vectorizer": [
        "DictVectorizer\nsur des dictionnaires non fréquences",
        "FeatureHasher\nsur des dictionnaires non fréquences",
        "FeatureHasher\nsur des jetons bruts",
        "CountVectorizer",
        "HashingVectorizer",
        "TfidfVectorizer"
    ],
    "speed": [
        2.4, 4.4, 7.2, 5.1, 11.7, 2.9
    ]
}

fig, ax = plt.subplots(figsize=(12, 6))

y_pos = np.arange(len(dict_count_vectorizers["vectorizer"]))
ax.barh(y_pos, dict_count_vectorizers["speed"], align="center")
ax.set_yticks(y_pos)
ax.set_yticklabels(dict_count_vectorizers["vectorizer"])
ax.invert_yaxis()
_ = ax.set_xlabel("vitesse (MB/s)")
```
