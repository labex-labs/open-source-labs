# Criar Objeto Timer

Crie um novo objeto timer. Defina o intervalo para 100 milissegundos (1000 é o padrão) e diga ao timer qual função deve ser chamada.

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
