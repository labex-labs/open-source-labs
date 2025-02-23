# Encabezados de seguridad

Los navegadores reconocen varios encabezados de respuesta para controlar la seguridad. Se recomienda revisar y utilizar los siguientes encabezados de seguridad en su aplicación Flask:

- HTTP Strict Transport Security (HSTS): Indica al navegador que convierta todas las solicitudes HTTP a HTTPS.
- Content Security Policy (CSP): Especifica de dónde se pueden cargar varios tipos de recursos.
- X-Content-Type-Options: Fuerza al navegador a respetar el tipo de contenido de la respuesta.
- X-Frame-Options: Evita que sitios externos embeban su sitio en un iframe.

Puede utilizar la extensión `Flask-Talisman` para administrar HTTPS y encabezados de seguridad en su aplicación Flask.
