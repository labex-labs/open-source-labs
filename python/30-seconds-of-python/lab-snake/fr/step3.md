# Gestion de motifs plus complexes

Notre fonction actuelle fonctionne pour le camelCase, mais nous devons l'améliorer pour gérer des motifs supplémentaires tels que :

1. Le PascalCase (par exemple, `HelloWorld`)
2. Les chaînes avec des tirets (par exemple, `hello-world`)
3. Les chaînes qui ont déjà des underscores (par exemple, `hello_world`)

Mettons à jour notre fonction pour gérer ces cas :

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

Les améliorations que nous avons apportées :

1. Tout d'abord, nous remplaçons tous les tirets par des espaces.
2. La nouvelle expression régulière `re.sub('([A-Z]+)', r' \1', s)` ajoute un espace avant toute séquence de lettres majuscules, ce qui aide pour le PascalCase.
3. Nous conservons notre expression régulière de gestion du camelCase.
4. Enfin, nous divisons la chaîne par les espaces, la rejoignons avec des underscores et la convertissons en minuscules, ce qui gère tous les espaces restants et assure une sortie cohérente.

Exécutez votre script pour tester avec différents formats d'entrée :

```bash
python3 ~/project/snake_case.py
```

Vous devriez voir une sortie comme celle-ci :

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

Notre fonction est maintenant plus robuste et peut gérer différents formats d'entrée. À l'étape suivante, nous ferons nos derniers ajustements et testerons avec la suite de tests complète.
