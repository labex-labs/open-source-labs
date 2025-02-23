# Utiliser le système de gabarits

Revenons à la vue `detail()` de notre application de sondage. Étant donné la variable de contexte `question`, voici à quoi pourrait ressembler le gabarit `polls/detail.html` :

```html+django
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

Le système de gabarits utilise une syntaxe de recherche par point pour accéder aux attributs des variables. Dans l'exemple de `{{ question.question_text }}`, d'abord Django effectue une recherche dans un dictionnaire sur l'objet `question`. Si cela échoue, il essaie une recherche d'attribut - ce qui fonctionne, dans ce cas. Si la recherche d'attribut avait échoué, il aurait essayé une recherche par indice de liste.

L'appel de méthode se produit dans la boucle `{% for %}<for>` : `question.choice_set.all` est interprété comme le code Python `question.choice_set.all()`, qui renvoie un itérable d'objets `Choice` et est approprié pour être utilisé dans la balise `{% for %}<for>`.
