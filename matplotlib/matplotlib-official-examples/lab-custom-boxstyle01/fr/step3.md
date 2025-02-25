# Enregistrer le style de boîte personnalisé avec Matplotlib

Une fois que vous avez implémenté un style de boîte personnalisé sous forme de classe, vous pouvez l'enregistrer avec Matplotlib. Cela vous permet de spécifier le style de boîte sous forme de chaîne de caractères, `bbox=dict(boxstyle="nom_enregistré,param=valeur,...",...)`.

```python
BoxStyle._style_list["angled"] = MyStyle  # Enregistre le style personnalisé.
```
