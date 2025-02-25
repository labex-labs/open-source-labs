# Exercice 1.18 : Expressions régulières

Une limitation des opérations de base sur les chaînes de caractères est qu'elles ne prennent pas en charge aucun type de correspondance de motif avancée. Pour cela, vous devez utiliser le module `re` de Python et les expressions régulières. La manipulation des expressions régulières est un sujet vaste, mais voici un exemple court :

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Trouvez toutes les occurrences d'une date
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Remplacez toutes les occurrences d'une date par du texte de remplacement
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

Pour plus d'informations sur le module `re`, consultez la documentation officielle à [https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).
