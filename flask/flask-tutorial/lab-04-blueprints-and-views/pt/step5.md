# Implementar a View (Visualização) de Logout

Agora, vamos adicionar uma view (visualização) de logout em `flaskr/auth.py`. Esta view (visualização) lidará com a funcionalidade de logout do usuário.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
