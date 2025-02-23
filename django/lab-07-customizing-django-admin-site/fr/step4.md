# Personnaliser l'apparence et la sensation générale de l'administrateur

Il est clair que le fait d'avoir "Administration Django" en haut de chaque page d'administration est ridicule. C'est juste du texte de remplacement.

Cependant, vous pouvez le changer en utilisant le système de templates de Django. L'administrateur Django est alimenté par Django lui-même, et ses interfaces utilisent le système de templates propre à Django.

## Personnaliser les templates de votre _projet_

Créez un répertoire `templates` dans le répertoire de votre projet (celui qui contient `manage.py`). Les templates peuvent être situés n'importe où sur votre système de fichiers accessible par Django. (Django s'exécute avec le nom d'utilisateur sous lequel votre serveur s'exécute.) Cependant, il est bon de suivre la convention consistant à conserver vos templates au sein du projet.

Ouvrez votre fichier de paramètres (`mysite/settings.py`, souvenez-vous) et ajoutez une option `DIRS <TEMPLATES-DIRS>` dans la configuration `TEMPLATES` :

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

`DIRS <TEMPLATES-DIRS>` est une liste de répertoires de système de fichiers à vérifier lors du chargement des templates Django ; c'est un chemin de recherche.

## Organiser les templates

tout comme les fichiers statiques, nous _pourrions_ avoir tous nos templates ensemble, dans un grand répertoire `templates`, et cela fonctionnerait parfaitement. Cependant, les templates qui appartiennent à une application particulière devraient être placés dans le répertoire de templates de cette application (par exemple `polls/templates`) plutôt que dans celui du projet (`templates`). Nous en discuterons plus en détail dans le tutoriel sur les `applications réutilisables </intro/reusable-apps>` _pourquoi_ nous faisons cela.

Maintenant, créez un répertoire appelé `admin` à l'intérieur de `templates`, et copiez le template `admin/base_site.html` à partir du répertoire de templates d'administrateur par défaut dans le code source de Django lui-même (`django/contrib/admin/templates`) dans ce répertoire.

## Où sont les fichiers sources de Django?

Si vous avez du mal à trouver où se trouvent les fichiers sources de Django sur votre système, exécutez la commande suivante :

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

Ensuite, éditez le fichier et remplacez `{{ site_header|default:_('Django administration') }}` (y compris les accolades) par le nom de votre propre site tel que vous le jugez approprié. Vous devriez finir avec une section de code comme :

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Administration des sondages</a><div>
{% endblock %}
```

Nous utilisons cette approche pour vous apprendre à surcharger des templates. Dans un projet réel, vous utiliseriez probablement l'attribut `django.contrib.admin.AdminSite.site_header` pour effectuer cette personnalisation particulière plus facilement.

Ce fichier de template contient beaucoup de texte comme `{% block branding %}` et `{{ title }}`. Les balises `{%` et `{{` font partie du langage de templates de Django. Lorsque Django rend `admin/base_site.html`, ce langage de templates sera évalué pour produire la page HTML finale, tout comme nous l'avons vu dans `**Création des vues d'interface publique**`.

Notez que n'importe quel template d'administrateur par défaut de Django peut être surchargé. Pour surcharger un template, faites comme vous l'avez fait avec `base_site.html` - copiez-le à partir du répertoire par défaut dans votre répertoire personnalisé, et apportez les modifications.

## Personnaliser les templates de votre _application_

Les lecteurs perspicaces se demanderont : Mais si `DIRS <TEMPLATES-DIRS>` était vide par défaut, comment Django trouvait-il les templates d'administrateur par défaut? La réponse est que, puisque `APP_DIRS <TEMPLATES-APP_DIRS>` est définie sur `True`, Django recherche automatiquement un sous-répertoire `templates/` à l'intérieur de chaque package d'application, pour être utilisé en cas de panne (n'oubliez pas que `django.contrib.admin` est une application).

Notre application de sondage n'est pas très complexe et n'a pas besoin de templates d'administrateur personnalisés. Mais si elle devenait plus sophistiquée et nécessitait la modification des templates d'administrateur standard de Django pour certaines de ses fonctionnalités, il serait plus sage de modifier les templates de l'_application_, plutôt que ceux du _projet_. Ainsi, vous pourriez inclure l'application de sondages dans tout nouveau projet et être sûr qu'elle trouverait les templates personnalisés dont elle a besoin.

Consultez la `documentation sur le chargement de templates <template-loading>` pour plus d'informations sur la manière dont Django trouve ses templates.
