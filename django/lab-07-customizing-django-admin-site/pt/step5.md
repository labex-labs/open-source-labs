# Personalizar a página de índice do admin

De forma semelhante, você pode querer personalizar a aparência e a sensação da página de índice do admin do Django.

Por padrão, ela exibe todos os aplicativos em `INSTALLED_APPS` que foram registrados com o aplicativo admin, em ordem alfabética. Você pode querer fazer alterações significativas no layout. Afinal, o índice é provavelmente a página mais importante do admin, e deve ser fácil de usar.

O template a ser personalizado é `admin/index.html`. (Faça o mesmo que com `admin/base_site.html` na seção anterior -- copie-o do diretório padrão para seu diretório de templates personalizado). Edite o arquivo e você verá que ele usa uma variável de template chamada `app_list`. Essa variável contém todos os aplicativos Django instalados. Em vez de usar isso, você pode codificar links para páginas de administração específicas de objetos da maneira que achar melhor.
