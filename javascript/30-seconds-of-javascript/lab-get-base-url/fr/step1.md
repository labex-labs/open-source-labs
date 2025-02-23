# Récupération de l'URL de base

Pour récupérer l'URL de base à partir d'une URL donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Utilisez la fonction JavaScript suivante pour obtenir l'URL actuelle sans aucun paramètre ou identifiant de fragment :

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. Remplacez `url` par l'URL à partir de laquelle vous voulez récupérer l'URL de base.
5. La fonction supprimera tout ce qui se trouve après soit `'?'` soit `'#'`, s'il est trouvé, et renverra l'URL de base.
6. Voici un exemple :

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
