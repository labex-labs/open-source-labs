# Écrire des tests

Maintenant que vous avez configuré l'environnement de test, vous pouvez commencer à écrire des tests pour votre application Flask. Voici quelques exemples de tests courants que vous pourriez vouloir écrire :

1. Tester une route :

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   Ce test envoie une requête GET à la route racine ("/") et vérifie que le code de statut de la réponse est 200 et que les données de réponse contiennent la chaîne "Hello, World!".

2. Tester une requête POST :

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   Ce test envoie une requête POST à la route de connexion ("/login") avec des données de formulaire contenant un nom d'utilisateur et un mot de passe. Il vérifie que le code de statut de la réponse est 200 et que les données de réponse contiennent la chaîne "Logged in successfully".

3. Tester une commande :

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   Ce test invoque une commande nommée "hello" et vérifie que la commande se termine avec un code 0 et que la sortie contient la chaîne "Hello, World!".
