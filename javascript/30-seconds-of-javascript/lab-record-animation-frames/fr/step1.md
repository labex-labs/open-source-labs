# Guide to Record Animation Frames

Pour enregistrer les trames d'animation, suivez les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursivité pour invoquer le rappel fourni à chaque trame d'animation.
3. Si `running` est `true`, continuez d'invoquer `Window.requestAnimationFrame()`, qui invoque le rappel fourni.
4. Pour permettre un contrôle manuel de l'enregistrement, renvoyez un objet avec deux méthodes `start` et `stop`.
5. Omettez le second argument, `autoStart`, pour appeler implicitement `start` lorsque la fonction est invoquée.

Utilisez le code suivant pour enregistrer les trames d'animation :

```js
const recordAnimationFrames = (callback, autoStart = true) => {
  let running = false,
    raf;
  const stop = () => {
    if (!running) return;
    running = false;
    cancelAnimationFrame(raf);
  };
  const start = () => {
    if (running) return;
    running = true;
    run();
  };
  const run = () => {
    raf = requestAnimationFrame(() => {
      callback();
      if (running) run();
    });
  };
  if (autoStart) start();
  return { start, stop };
};
```

Exemple d'utilisation du code :

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// affiche 'Animation frame fired' à chaque trame d'animation
recorder.stop(); // arrête d'afficher
recorder.start(); // recommence
const recorder2 = recordAnimationFrames(cb, false);
// `start` doit être appelé explicitement pour commencer à enregistrer les trames
```
