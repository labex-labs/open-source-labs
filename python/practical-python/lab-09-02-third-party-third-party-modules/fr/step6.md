# Environnements virtuels

Une solution courante aux problèmes d'installation de packages est de créer pour vous-même un soi-disant "environnement virtuel". Naturellement, il n'y a pas "une seule manière" de le faire - en fait, il existe plusieurs outils et techniques concurrentes. Cependant, si vous utilisez une installation standard de Python, vous pouvez essayer de taper ceci :

```bash
$ sudo apt install python3-venv
$ python -m venv mypython
bash %
```

Après quelques instants d'attente, vous aurez un nouveau répertoire `mypython` qui est une petite installation Python à vous. Dans ce répertoire, vous trouverez un répertoire `bin/` (Unix) ou un répertoire `Scripts/` (Windows). Si vous exécutez le script `activate` trouvé là, il "activera" cette version de Python, en la rendant la commande `python` par défaut pour le shell. Par exemple :

```bash
$ source mypython/bin/activate
(mypython) bash %
```

À partir d'ici, vous pouvez maintenant commencer à installer des packages Python pour vous-même. Par exemple :

    (mypython) $ python -m pip install pandas

...

Dans le cadre d'expériences et d'essais de différents packages, un environnement virtuel fonctionnera généralement bien. Si, d'autre part, vous créez une application et qu'elle a des dépendances de packages spécifiques, c'est un problème légèrement différent.
