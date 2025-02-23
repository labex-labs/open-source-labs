# Non, N'est-pas-égal

Cela renvoie la valeur logiquement opposée de ce qui le précède. Il transforme un `true` en un `false`, etc. Lorsqu'il est utilisé avec l'opérateur d'égalité, l'opérateur de négation teste si deux valeurs ne sont pas égales.

Pour "Non", l'expression de base est true, mais la comparaison renvoie `false` car nous la nigeons :

```js
// Non(!)
let myVariable = 3;
!(myVariable === 3);
```

"N'est-pas-égal" donne essentiellement le même résultat avec une syntaxe différente. Ici, nous testons "`myVariable` est-il DIFFERENT de 3". Cela renvoie `false` car `myVariable` EST égal à 3 :

```js
// N'est-pas-égal(!==)
let myVariable = 3;
myVariable !== 3;
```

Il y a beaucoup plus d'opérateurs à explorer, mais c'est suffisant pour le moment. Consultez [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators) pour une liste complète.

> **Note** : Le mélange de types de données peut entraîner des résultats étranges lors des calculs. Faites attention à vous référer correctement à vos variables et à obtenir les résultats que vous attendez. Par exemple, entrez `'35' + '25'` dans votre console. Pourquoi n'obtenez-vous pas le résultat que vous attendiez? Parce que les guillemets transforment les nombres en chaînes de caractères, donc vous avez fini par concaténer des chaînes de caractères plutôt qu'en additionnant des nombres. Si vous entrez `35 + 25`, vous obtiendrez la somme des deux nombres.
