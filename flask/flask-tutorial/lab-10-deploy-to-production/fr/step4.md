# Run the Application with a Production Server

Pour un environnement de production, vous devriez utiliser un serveur WSGI au lieu du serveur de développement intégré. Nous allons utiliser Waitress comme notre serveur WSGI.

Tout d'abord, installez Waitress :

```bash
# Install Waitress
pip install waitress
```

Maintenant, indiquez à Waitress de servir votre application :

```bash
# Run the application with Waitress
waitress-serve --call 'flaskr:create_app'
```
