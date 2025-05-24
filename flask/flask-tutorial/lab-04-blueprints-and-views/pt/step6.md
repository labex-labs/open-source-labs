# Implementar o Decorator (Decorador) de Login Obrigatório

Também precisaremos de um decorator (decorador) para proteger nossas views (visualizações) que exigem que um usuário esteja logado. Este decorator (decorador) será implementado em `flaskr/auth.py`.

```python
# flaskr/auth.py

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```
