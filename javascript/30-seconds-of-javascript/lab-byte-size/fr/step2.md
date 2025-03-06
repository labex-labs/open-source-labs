# Utilisation de Blob pour calculer la taille en octets d'une chaîne de caractères (string)

Maintenant que nous comprenons la représentation des chaînes de caractères, apprenons à calculer la taille réelle en octets d'une chaîne de caractères à l'aide de l'objet `Blob`.

Un `Blob` (Binary Large Object) représente un objet semblable à un fichier contenant des données brutes immuables. En convertissant notre chaîne de caractères en un Blob, nous pouvons accéder à sa propriété `size` pour déterminer la taille en octets.

Dans la console Node.js, créons une fonction pour calculer la taille en octets :

```javascript
const byteSize = (str) => new Blob([str]).size;
```

Cette fonction prend une chaîne de caractères en entrée, la convertit en un Blob et renvoie sa taille en octets.

Testons cette fonction avec un exemple simple :

```javascript
byteSize("Hello World");
```

Vous devriez voir le résultat suivant :

```
11
```

Dans ce cas, le nombre de caractères et la taille en octets sont les mêmes car "Hello World" ne contient que des caractères ASCII, chacun représenté par un seul octet.

Essayons maintenant avec un caractère non-ASCII :

```javascript
byteSize("😀");
```

Vous devriez voir le résultat suivant :

```
4
```

Cela montre que bien que l'emoji apparaisse comme un seul caractère, il occupe en réalité 4 octets de stockage.
