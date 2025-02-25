# Mode interactif

Lorsque vous lancez Python, vous obtenez un mode _interactif_ dans lequel vous pouvez expérimenter.

Si vous commencez à taper des instructions, elles seront exécutées immédiatement. Il n'y a pas de cycle d'édition/ compilation/ exécution/ débogage.

```python
>>> print('hello world')
hello world
>>> 37*42
1554
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

Ce qu'on appelle _read-eval-print-loop_ (ou REPL) est très utile pour le débogage et l'exploration.

**ARRÊT**: Si vous ne savez pas comment interagir avec Python, arrêtez ce que vous faites et trouvez comment le faire. Si vous utilisez un IDE, il peut être caché derrière une option de menu ou une autre fenêtre. De nombreuses parties de ce cours supposent que vous pouvez interagir avec l'interpréteur.

Regardons de plus près les éléments du REPL:

- `>>>` est l'invite de commande de l'interpréteur pour commencer une nouvelle instruction.
- `...` est l'invite de commande de l'interpréteur pour continuer une instruction. Appuyez sur Entrée pour terminer de taper et exécuter ce que vous avez entré.

L'invite `...` peut ou non être affichée selon votre environnement. Pour ce cours, elle est affichée comme des espaces pour faciliter la copie/collage d'échantillons de code.

Le tiret bas `_` contient le dernier résultat.

```python
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

_Cela ne vaut que dans le mode interactif._ Vous n' utilisez jamais `_` dans un programme.
