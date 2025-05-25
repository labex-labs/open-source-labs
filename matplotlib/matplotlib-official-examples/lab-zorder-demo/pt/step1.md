# Compreendendo o Zorder

O atributo `zorder` no Matplotlib é um número de ponto flutuante que determina a ordem de desenho dos artistas. Artistas com um `zorder` mais alto são desenhados sobre aqueles com um `zorder` mais baixo. O valor padrão de `zorder` depende do tipo de artista. Por exemplo, imagens têm um `zorder` padrão de 0, enquanto patches (retalhos) têm um `zorder` padrão de 1.
