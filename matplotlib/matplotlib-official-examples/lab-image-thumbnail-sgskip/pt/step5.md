# Criar Diretório de Saída

Nesta etapa, você criará um diretório chamado `thumbs` onde as miniaturas serão salvas. Se o diretório já existir, ele não será criado novamente.

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
