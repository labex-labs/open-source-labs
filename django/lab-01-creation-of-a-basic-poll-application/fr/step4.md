# Création de l'application Polls

Maintenant que votre environnement - un "projet" - est configuré, vous êtes prêt à commencer à travailler.

Chaque application que vous écrivez dans Django est composée d'un package Python qui suit une certaine convention. Django est livré avec une utilité qui génère automatiquement la structure de répertoires de base d'une application, de sorte que vous pouvez vous concentrer sur l'écriture de code plutôt que sur la création de répertoires.

> Projets vs. applications
> Quelle est la différence entre un projet et une application? Une application est une application web qui fait quelque chose - par exemple, un système de blog, une base de données de registres publics ou une petite application de sondage. Un projet est une collection de configurations et d'applications pour un site web particulier. Un projet peut contenir plusieurs applications. Une application peut être incluse dans plusieurs projets.

Vos applications peuvent se trouver n'importe où sur votre `Python path <tut-searchpath>`. Dans ce tutoriel, nous allons créer notre application de sondage dans le même répertoire que votre fichier `manage.py` afin qu'elle puisse être importée comme un module de niveau supérieur autonome, plutôt qu'un sous-module de `mysite`.

Pour créer votre application, assurez-vous d'être dans le même répertoire que `manage.py` et tapez cette commande :

```bash
cd ~/project/mysite
python manage.py startapp polls
```

Cela créera un répertoire `polls`, qui est structuré comme suit :

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Cette structure de répertoires contiendra l'application de sondage.
