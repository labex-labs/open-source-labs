# Incluir Arquivos Necessários

O backend de build setuptools precisa de outro arquivo chamado `MANIFEST.in` para incluir arquivos não-Python no projeto.

Crie um `MANIFEST.in` com o seguinte conteúdo:

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

Isso informa ao build para copiar tudo nos diretórios `static` e `templates`, e o arquivo `schema.sql`, enquanto exclui todos os arquivos bytecode.
