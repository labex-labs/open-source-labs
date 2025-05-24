# Visão Geral

Uma view (visualização) é um "tipo" de página web em sua aplicação Django que geralmente serve a uma função específica e possui um template (modelo) específico. Por exemplo, em uma aplicação de blog, você pode ter as seguintes views:

- Página inicial do blog -- exibe as últimas entradas.
- Página de "detalhes" da entrada -- página de permalink (link permanente) para uma única entrada.
- Página de arquivo baseada em ano -- exibe todos os meses com entradas no ano especificado.
- Página de arquivo baseada em mês -- exibe todos os dias com entradas no mês especificado.
- Página de arquivo baseada em dia -- exibe todas as entradas no dia especificado.
- Ação de comentário -- lida com a publicação de comentários em uma determinada entrada.

Em nossa aplicação de enquetes, teremos as seguintes quatro views:

- Página "index" (índice) da pergunta -- exibe as últimas perguntas.
- Página de "detalhes" da pergunta -- exibe o texto da pergunta, sem resultados, mas com um formulário para votar.
- Página de "resultados" da pergunta -- exibe os resultados de uma pergunta específica.
- Ação de voto -- lida com a votação em uma escolha específica em uma pergunta específica.

No Django, páginas web e outros conteúdos são entregues por views. Cada view é representada por uma função Python (ou método, no caso de views baseadas em classe). O Django escolherá uma view examinando a URL que foi solicitada (para ser preciso, a parte da URL após o nome do domínio).

Agora, em seu tempo na web, você pode ter se deparado com belezas como `ME2/Sites/dirmod.htm?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B`. Você ficará satisfeito em saber que o Django nos permite padrões de _URL_ muito mais elegantes do que isso.

Um padrão de URL é a forma geral de uma URL - por exemplo: `/newsarchive/<ano>/<mês>/`.

Para ir de uma URL para uma view, o Django usa o que é conhecido como 'URLconfs'. Uma URLconf mapeia padrões de URL para views.

Este tutorial fornece instruções básicas sobre o uso de URLconfs, e você pode consultar `/topics/http/urls` para obter mais informações.
