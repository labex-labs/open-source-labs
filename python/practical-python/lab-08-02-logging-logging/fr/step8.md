# Exercice 8.3 : Ajout de la journalisation à un programme

Pour ajouter la journalisation à une application, vous avez besoin d'un mécanisme pour initialiser le module de journalisation dans le module principal. Une manière de faire cela consiste à inclure du code de configuration qui ressemble à ceci :

    # Ce fichier configure de base le module de journalisation.
    # Changez les paramètres ici pour ajuster la sortie de journalisation selon vos besoins.
    import logging
    logging.basicConfig(
        filename = 'app.log',            # Nom du fichier de journal (omettez pour utiliser stderr)
        filemode = 'w',                  # Mode d'ouverture du fichier (utilisez 'a' pour ajouter)
        level    = logging.WARNING,      # Niveau de journalisation (DEBUG, INFO, WARNING, ERROR ou CRITICAL)
    )

Encore une fois, vous devriez placer ce code quelque part dans les étapes de démarrage de votre programme. Par exemple, où placeriez-vous ce code dans votre programme `report.py`?
