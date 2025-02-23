# Afficher et cacher du contenu

> Le fichier `index.html` a déjà été fourni dans la machine virtuelle.

jQuery peut afficher ou cacher du contenu instantanément avec `.show()` ou `.hide()` :

```js
// Cacher instantanément tous les paragraphes
$("p").hide();

// Afficher instantanément tous les divs ayant la classe de style caché
$("div.hidden").show();
```

Lorsque jQuery cache un élément, il définit sa propriété CSS `display` sur `none`. Cela signifie que le contenu aura une largeur et une hauteur de zéro ; cela ne signifie pas que le contenu deviendra simplement transparent et laissera une zone vide sur la page.

jQuery peut également afficher ou cacher du contenu au moyen d'effets d'animation. Vous pouvez demander à `.show()` et `.hide()` d'utiliser l'animation de plusieurs manières. L'une est de passer un argument de `'slow'`, `'normal'` ou `'fast'` :

```js
// Cacher lentement tous les paragraphes
$("p").hide("slow");

// Afficher rapidement tous les divs ayant la classe de style caché
$("div.hidden").show("fast");
```

Si vous préférez avoir un contrôle plus direct sur la durée de l'effet d'animation, vous pouvez passer la durée souhaitée en millisecondes à `.show()` et `.hide()` :

```js
// Cacher tous les paragraphes en demi-seconde
$("p").hide(2000);

// Afficher tous les divs ayant la classe de style caché en 1,25 secondes
$("div.hidden").show(1250);
```

La plupart des développeurs passent un nombre de millisecondes pour avoir un contrôle plus précis sur la durée.

> Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
