# Construindo um Servidor Web de Thread Única

Começaremos por fazer um servidor web de thread única funcionar. Antes de começarmos, vamos dar uma olhada em uma visão geral rápida dos protocolos envolvidos na construção de servidores web. Os detalhes desses protocolos estão além do escopo deste livro, mas uma breve visão geral fornecerá as informações necessárias.

Os dois principais protocolos envolvidos em servidores web são o _Hypertext Transfer Protocol_ _(HTTP)_ e o _Transmission Control Protocol_ _(TCP)_. Ambos os protocolos são protocolos de _requisição-resposta_ (_request-response_), o que significa que um _cliente_ inicia requisições e um _servidor_ escuta as requisições e fornece uma resposta ao cliente. O conteúdo dessas requisições e respostas é definido pelos protocolos.

TCP é o protocolo de baixo nível que descreve os detalhes de como a informação chega de um servidor para outro, mas não especifica qual é essa informação. HTTP constrói em cima do TCP, definindo o conteúdo das requisições e respostas. É tecnicamente possível usar HTTP com outros protocolos, mas na grande maioria dos casos, HTTP envia seus dados via TCP. Trabalharemos com os bytes brutos das requisições e respostas TCP e HTTP.
