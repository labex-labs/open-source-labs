# Настраиваем макет и сохраняем график

Наконец, вы можете настроить макет своего графика и сохранить его в файл с использованием функций `fig.tight_layout()` и `fig.savefig()` соответственно.

```python
fig.tight_layout(pad=.5)

fig.savefig("pgf_texsystem.pdf")
fig.savefig("pgf_texsystem.png")
```
