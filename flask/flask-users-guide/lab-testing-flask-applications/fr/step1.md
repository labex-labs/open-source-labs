# Configurer l'environnement de test

Avant de commencer à écrire des tests pour votre application Flask, vous devez configurer l'environnement de test. Voici les étapes pour ce faire :

1. Installez le framework `pytest` en exécutant la commande suivante :

   ```bash
   pip install pytest
   ```

2. Créez un nouveau fichier nommé `conftest.py` dans le dossier `tests` de votre application Flask.

3. Dans le fichier `conftest.py`, importez les modules nécessaires :

   ```python
   import pytest
   from my_app import create_app
   ```

4. Définissez un fixture nommé `app` qui crée et configure une instance d'application :

   ```python
   @pytest.fixture()
   def app():
       app = create_app()
       app.config.update({
           "TESTING": True,
       })
       yield app
   ```

   Notez que si vous utilisez un modèle de fabrique d'applications, vous devriez modifier le fixture en conséquence.

5. Définissez des fixtures pour le client de test et le lanceur de CLI :

   ```python
   @pytest.fixture()
   def client(app):
       return app.test_client()

   @pytest.fixture()
   def runner(app):
       return app.test_cli_runner()
   ```
