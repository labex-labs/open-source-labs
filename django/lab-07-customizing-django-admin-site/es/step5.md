# Personalizar la página de índice del administrador

En un tono similar, es posible que desee personalizar la apariencia y sensación de la página de índice del administrador de Django.

Por defecto, muestra todas las aplicaciones en `INSTALLED_APPS` que se han registrado con la aplicación de administración, en orden alfabético. Es posible que desee realizar cambios significativos en el diseño. Después de todo, el índice es probablemente la página más importante del administrador y debe ser fácil de usar.

La plantilla para personalizar es `admin/index.html`. (Haga lo mismo que con `admin/base_site.html` en la sección anterior: cópiela del directorio predeterminado a su directorio de plantillas personalizadas). Edite el archivo y verá que utiliza una variable de plantilla llamada `app_list`. Esa variable contiene cada aplicación de Django instalada. En lugar de utilizar eso, puede codificar en duro enlaces a las páginas de administración específicas de objetos de la manera que crea más adecuada.
