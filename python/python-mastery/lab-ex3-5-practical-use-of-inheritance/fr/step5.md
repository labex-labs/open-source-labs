# Faciliter le choix

Un problème avec l'utilisation de l'héritage est la complexité supplémentaire liée au choix des classes différentes à utiliser (par exemple, se souvenir des noms, utiliser les bonnes instructions `import`, etc.). Une fonction usine peut simplifier cela. Ajoutez une fonction `create_formatter()` à votre fichier `tableformat.py` qui permet à un utilisateur de créer plus facilement un formateur en spécifiant un format tel que `'text'`, `'csv'` ou `'html'`. Par exemple :

```python
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('html')
>>> print_table(portfolio, ['name','shares','price'], formatter)
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
>>>
```

**Discussion**

La classe `TableFormatter` dans cet exercice est un exemple de ce qu'on appelle une "classe de base abstraite". Ce n'est pas quelque chose qui est destiné à être utilisé directement. Au contraire, elle sert comme une sorte de spécification d'interface pour un composant de programme - dans ce cas, les différents formats de sortie. Essentiellement, le code qui produit le tableau sera programmé contre la classe de base abstraite avec l'attente qu'un utilisateur fournisse une implémentation appropriée. Tant que toutes les méthodes requises ont été implémentées, tout devrait simplement "fonctionner" (on peut croiser les doigts).
