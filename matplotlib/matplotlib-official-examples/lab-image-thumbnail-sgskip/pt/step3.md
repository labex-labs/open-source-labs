# Analisar Argumentos

Nesta etapa, você analisará os argumentos passados para o seu programa. Você precisa criar um objeto `ArgumentParser` e adicionar um argumento chamado `imagedir`. Este argumento especifica o caminho para o diretório contendo as imagens. Você pode usar o parâmetro `type` para especificar o tipo de dado do argumento. Neste caso, o argumento deve ser do tipo `Path`.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
