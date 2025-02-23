# Personnaliser la page d'accueil de l'administrateur

Sur un ton similaire, vous pouvez vouloir personnaliser l'apparence et la sensation générale de la page d'accueil de l'administrateur Django.

Par défaut, elle affiche toutes les applications de `INSTALLED_APPS` qui ont été enregistrées auprès de l'application d'administrateur, dans l'ordre alphabétique. Vous pouvez vouloir apporter des modifications importantes à la disposition. Après tout, l'accueil est probablement la page la plus importante de l'administrateur, et elle devrait être facile à utiliser.

Le template à personnaliser est `admin/index.html`. (Faites comme avec `admin/base_site.html` dans la section précédente - copiez-le à partir du répertoire par défaut vers votre répertoire de templates personnalisé). Éditez le fichier, et vous verrez qu'il utilise une variable de template appelée `app_list`. Cette variable contient toutes les applications Django installées. Au lieu d'utiliser cela, vous pouvez coder en dur des liens vers les pages d'administrateur spécifiques aux objets de la manière que vous jugez la meilleure.
