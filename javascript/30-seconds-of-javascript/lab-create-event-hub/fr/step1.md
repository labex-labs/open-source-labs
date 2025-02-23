# Création d'un hub d'événements

Pour créer un hub d'événements avec les méthodes `emit`, `on` et `off`, suivez les étapes suivantes :

1. Utilisez `Object.create(null)` pour créer un objet `hub` vide qui n'hérite pas des propriétés de `Object.prototype`.
2. Pour `emit`, résolvez le tableau d'attrapeurs (handlers) en fonction de l'argument `event`, puis exécutez chacun d'entre eux avec `Array.prototype.forEach()` en passant les données en tant qu'argument.
3. Pour `on`, créez un tableau pour l'événement s'il n'existe pas encore, puis utilisez `Array.prototype.push()` pour ajouter l'attrapeur au tableau.
4. Pour `off`, utilisez `Array.prototype.findIndex()` pour trouver l'index de l'attrapeur dans le tableau d'événements et le supprimer à l'aide de `Array.prototype.splice()`.

Voici le code :

```js
const createEventHub = () => ({
  hub: Object.create(null),
  emit(event, data) {
    (this.hub[event] || []).forEach((handler) => handler(data));
  },
  on(event, handler) {
    if (!this.hub[event]) this.hub[event] = [];
    this.hub[event].push(handler);
  },
  off(event, handler) {
    const i = (this.hub[event] || []).findIndex((h) => h === handler);
    if (i > -1) this.hub[event].splice(i, 1);
    if (this.hub[event].length === 0) delete this.hub[event];
  }
});
```

Pour utiliser le hub d'événements :

1. S'abonnez à des événements en écoutant différents types d'événements à l'aide de `on()`.
2. Publiez des événements pour invoquer tous les attrapeurs s'abonnés à eux, en passant les données à ceux-ci en tant qu'argument à l'aide de `emit()`.
3. Désabonnez-vous d'un événement en empêchant un attrapeur spécifique d'écouter l'événement à l'aide de `off()`.

Voici un exemple :

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// S'abonner : écouter différents types d'événements
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// Publier : émettre des événements pour invoquer tous les attrapeurs s'abonnés à eux, en passant les données à ceux-ci en tant qu'argument
hub.emit("message", "hello world"); // affiche 'hello world' et 'Message event fired'
hub.emit("message", { hello: "world" }); // affiche l'objet et 'Message event fired'
hub.emit("increment"); // la variable `increment` est maintenant égale à 1

// Désabonner : empêcher un attrapeur spécifique d'écouter l'événement 'message'
hub.off("message", handler);
```
