# Comment jQuery fonctionne

> Le fichier `index.html` a déjà été fourni dans la machine virtuelle.

Ce fichier sera automatiquement généré pendant l'initialisation de l'environnement. Si cela n'est pas fait automatiquement, créez le fichier et fonctionnez comme indiqué dans l'image ci-dessus. Le code de la fonction est le suivant :

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Démonstration</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // Votre code ici.
    </script>
  </body>
</html>
```

L'attribut `src` de l'élément `<script>` doit pointer vers une copie de jQuery. Téléchargez une copie de jQuery à partir de la page [Téléchargement de jQuery](https://jquery.com/download/) et stockez le fichier `jquery.min.js` dans le même répertoire que votre fichier HTML.

> Note : Lorsque vous téléchargez jQuery, le nom de fichier peut contenir un numéro de version, par exemple `jquery-x.y.z.js`. Assurez-vous soit de renommer ce fichier en `jquery.js`, soit de mettre à jour l'attribut `src` de l'élément `<script>` pour correspondre au nom de fichier.

#### Lancement du code au chargement du document

Pour s'assurer que leur code s'exécute après que le navigateur ait fini de charger le document, de nombreux programmeurs JavaScript enveloppent leur code dans une fonction `onload` :

```js
window.onload = function () {
  alert("bienvenue");
};
```

Malheureusement, le code ne s'exécute pas avant que toutes les images ne soient terminées téléchargées, y compris les publicités en bannière. Pour exécuter le code dès que le document est prêt à être manipulé, jQuery dispose d'une instruction connue sous le nom d'[événement ready](http://api.jquery.com/ready/) :

```js
$(document).ready(function () {
  // Votre code ici.
});
```

> Note : La bibliothèque jQuery expose ses méthodes et ses propriétés via deux propriétés de l'objet `window` appelées `jQuery` et `$`. `$` est simplement un alias pour `jQuery` et il est souvent utilisé car il est plus court et plus rapide à écrire.

Par exemple, à l'intérieur de l'événement ready, vous pouvez ajouter un gestionnaire de clic au lien :

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Bonjour jQuery!");
  });
});
```

Copiez le code jQuery ci-dessus dans votre fichier HTML à l'endroit où il est écrit `// Votre code va ici`. Ensuite, enregistrez votre fichier HTML et rechargez la page de test dans votre navigateur.

#### Exemple complet

L'exemple suivant illustre le code de gestion de clic discuté ci-dessus, intégré directement dans le corps HTML. Notez que dans la pratique, il est généralement préférable de placer votre code dans un fichier JS séparé et de le charger sur la page avec l'attribut `src` d'un élément `<script>`.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Démonstration</title>
  </head>
  <body>
    <button>cliquez sur moi</button>
    <p>Bonjour le monde</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Bonjour jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> Veuillez cliquer sur 'Démarrer' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
