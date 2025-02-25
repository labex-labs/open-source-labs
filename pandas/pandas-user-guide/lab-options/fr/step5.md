# Utilisation de option_context

La fonction `option_context` nous permet d'exécuter un bloc de code avec un ensemble d'options qui reviennent aux paramètres précédents après l'exécution.

```python
# Exécutez un bloc de code avec un ensemble d'options
with pd.option_context("display.max_rows", 10):
    # Cela affichera 10 malgré que le paramètre global soit différent
    print(pd.get_option("display.max_rows"))

# Cela affichera le paramètre global car le bloc de contexte est terminé
print(pd.get_option("display.max_rows"))
```
