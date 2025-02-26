# Introduction

Dans ce laboratoire, nous allons apprendre à créer un Hook React personnalisé appelé `useOnWindowResize` qui exécutera une fonction de rappel chaque fois que la fenêtre est redimensionnée. Nous utiliserons les hooks `useRef()` et `useEffect()` pour écouter l'événement `'resize'` de l'objet global `Window` et nettoyer lorsque le composant est démonté. Ce Hook peut être utile pour créer des applications web réactives qui doivent s'adapter à différentes tailles d'écran.
