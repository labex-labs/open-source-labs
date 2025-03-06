# Utilisation des expressions régulières pour la correspondance de motifs

Pour convertir des chaînes de caractères en snake case, nous allons utiliser des expressions régulières (regex) pour identifier les limites des mots. Le module `re` en Python offre des capacités puissantes de correspondance de motifs que nous pouvons utiliser pour cette tâche.

Mettons à jour notre fonction pour gérer les chaînes au format camelCase :

1. Tout d'abord, nous devons identifier le motif où une lettre minuscule est suivie d'une lettre majuscule (comme dans "camelCase").
2. Ensuite, nous allons insérer un espace entre elles.
3. Enfin, nous allons convertir tout en minuscules et remplacer les espaces par des underscores (tirets bas).

Mettez à jour votre fichier `snake_case.py` avec cette fonction améliorée :

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Analysons ce que fait cette fonction :

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)` recherche les motifs où une lettre minuscule `([a-z])` est suivie d'une lettre majuscule `([A-Z])`. Ensuite, il remplace ce motif par les mêmes lettres mais ajoute un espace entre elles en utilisant `\1` et `\2` qui font référence aux groupes capturés.
- Ensuite, nous convertissons tout en minuscules avec `lower()` et remplaçons les espaces par des underscores.

Exécutez votre script à nouveau pour voir si cela fonctionne pour les chaînes au format camelCase :

```bash
python3 ~/project/snake_case.py
```

La sortie devrait maintenant être :

```
Original: helloWorld
Snake case: hello_world
```

Génial ! Notre fonction peut maintenant gérer les chaînes au format camelCase. À l'étape suivante, nous allons la améliorer pour gérer des cas plus complexes.
