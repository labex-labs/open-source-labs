# Сохраняем график

Наконец, мы можем сохранить наш график на диск. Следуйте шагам:

1. Выведите поддерживаемые форматы файлов с использованием `print(fig.canvas.get_supported_filetypes())`.

```python
print(fig.canvas.get_supported_filetypes())
```

2. Сохраните фигуру в виде файла изображения с использованием `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`. Раскомментируйте эту строку, чтобы сохранить фигуру.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

Вы можете открыть сохраненный файл изображения с помощью проводника файлов в левом боковом меню.
