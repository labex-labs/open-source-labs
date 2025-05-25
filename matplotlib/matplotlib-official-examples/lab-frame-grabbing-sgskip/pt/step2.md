# Configurar o escritor (writer)

Precisamos configurar o escritor (writer) que será usado para escrever os frames em um arquivo. Definimos os frames por segundo (fps) e adicionamos metadados como o título, artista e comentário.

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
