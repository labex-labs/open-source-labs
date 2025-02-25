# Introduction

Ce tutoriel vous guidera sur la manière de tracer une courbe avec une bande d'erreur à l'aide de Python Matplotlib. Une bande d'erreur est utilisée pour indiquer l'incertitude de la courbe. Dans cet exemple, nous supposons que l'erreur peut être donnée sous forme d'un scalaire `_err_` qui décrit l'incertitude perpendiculaire à la courbe en chaque point. Nous visualisons cette erreur comme une bande colorée autour de la trajectoire à l'aide d'un `.PathPatch`. Le patch est créé à partir de deux segments de chemin `(xp, yp)` et `(xn, yn)` qui sont déplacés de +/- `_err_` perpendiculairement à la courbe `(x, y)`.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
