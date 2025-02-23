# Conversion d'un objet en chaîne de requête

Pour convertir un objet en chaîne de requête, utilisez la fonction `objectToQueryString()` qui génère une chaîne de requête à partir des paires clé-valeur de l'objet donné.

La fonction fonctionne comme suit :

- Elle utilise `Array.prototype.reduce()` sur `Object.entries()` pour créer la chaîne de requête à partir de `queryParameters`.
- Elle détermine le `symbole` à utiliser soit `?` soit `&` en fonction de la longueur de `queryString`.
- Elle concatène `val` à `queryString` seulement si c'est une chaîne de caractères.
- Elle renvoie la `queryString` ou une chaîne de caractères vide lorsque les `queryParameters` sont fausses.

Voici le code de la fonction `objectToQueryString()` :

```js
const objectToQueryString = (queryParameters) => {
  return queryParameters
    ? Object.entries(queryParameters).reduce(
        (queryString, [key, val], index) => {
          const symbol = queryString.length === 0 ? "?" : "&";
          queryString +=
            typeof val === "string" ? `${symbol}${key}=${val}` : "";
          return queryString;
        },
        ""
      )
    : "";
};
```

Utilisation de l'exemple de la fonction `objectToQueryString()` :

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // renvoie '?page=1&size=2kg'
```
