# Einführung

In diesem Lab werden wir lernen, wie wir einen benutzerdefinierten React-Hook namens `useOnWindowResize` erstellen, der einen Callback ausführt, wenn das Fenster vergrößert oder verkleinert wird. Wir werden die Hooks `useRef()` und `useEffect()` verwenden, um das `'resize'`-Ereignis des globalen `Window`-Objekts zu hören und aufzuräumen, wenn die Komponente abmontiert wird. Dieser Hook kann nützlich sein, um responsive Webanwendungen zu erstellen, die an verschiedene Bildschirmgrößen anpassen müssen.
