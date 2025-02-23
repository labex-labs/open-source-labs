# Presentación de las pruebas automatizadas

## ¿Qué son las pruebas automatizadas?

Las pruebas son rutinas que verifican el funcionamiento de su código.

Las pruebas se realizan a diferentes niveles. Algunas pruebas pueden aplicarse a un detalle minúsculo (_¿devuelve un método de modelo particular los valores esperados?_), mientras que otras examinan el funcionamiento general del software (_¿produce una secuencia de entradas de usuario en el sitio el resultado deseado?_). Eso no es diferente al tipo de pruebas que realizó anteriormente en `**Configurar la base de datos**`, usando la `shell` para examinar el comportamiento de un método, o ejecutando la aplicación y entrando datos para comprobar cómo se comporta.

Lo que es diferente en las pruebas _automatizadas_ es que el trabajo de prueba se realiza por el sistema. Crea un conjunto de pruebas una vez, y luego, a medida que realiza cambios en su aplicación, puede comprobar que su código sigue funcionando como originalmente planeó, sin tener que realizar pruebas manuales que consumen mucho tiempo.

## Por qué es necesario crear pruebas

Entonces, ¿por qué crear pruebas y por qué ahora?

Es posible que sienta que tiene bastante en su plato solo aprendiendo Python/Django, y que tener otra cosa que aprender y hacer puede parecer abrumador y quizás innecesario. Después de todo, nuestra aplicación de sondeos está funcionando muy bien ahora; pasar por el trabajo de crear pruebas automatizadas no la hará funcionar mejor. Si crear la aplicación de sondeos es la última parte de programación de Django que hará, entonces, es cierto, no necesita saber cómo crear pruebas automatizadas. Pero, si no es el caso, ahora es un excelente momento para aprender.

### Las pruebas ahorrarán tiempo

Hasta cierto punto, "verificar que parece funcionar" será una prueba satisfactoria. En una aplicación más sofisticada, es posible que haya docenas de interacciones complejas entre componentes.

Un cambio en cualquiera de esos componentes podría tener consecuencias inesperadas en el comportamiento de la aplicación. Verificar que todavía "parece funcionar" podría significar probar la funcionalidad de su código con veinte variaciones diferentes de sus datos de prueba para asegurarse de que no ha roto nada, lo que no es una buena utilización de su tiempo.

Eso es especialmente cierto cuando las pruebas automatizadas podrían hacer esto por usted en segundos. Si algo ha salido mal, las pruebas también ayudarán a identificar el código que está causando el comportamiento inesperado.

A veces puede parecer una tarea molesta apartarse de su trabajo productivo y creativo de programación para enfrentarse al trabajo sin glamour y aburrido de escribir pruebas, especialmente cuando sabe que su código está funcionando correctamente.

Sin embargo, la tarea de escribir pruebas es mucho más gratificante que pasar horas probando manualmente su aplicación o tratar de identificar la causa de un problema recientemente introducido.

### Las pruebas no solo identifican problemas, sino que los previenen

Es un error pensar en las pruebas solo como un aspecto negativo del desarrollo.

Sin pruebas, el propósito o el comportamiento previsto de una aplicación puede ser bastante opaco. Incluso cuando es su propio código, a veces se encontrará buscando en él tratando de averiguar exactamente lo que está haciendo.

Las pruebas cambian eso; iluminan su código desde dentro, y cuando algo sale mal, enfocan la luz en la parte que ha fallado, _incluso si no se había dado cuenta de que había salido mal_.

### Las pruebas hacen que su código sea más atractivo

Es posible que haya creado un excelente software, pero encontrará que muchos otros desarrolladores se negarán a mirarlo porque carece de pruebas; sin pruebas, no lo confiarán. Jacob Kaplan-Moss, uno de los primeros desarrolladores de Django, dice: "El código sin pruebas está roto por diseño".

Que otros desarrolladores quieran ver pruebas en su software antes de tomarlo en serio es otra razón para que empiece a escribir pruebas.

### Las pruebas ayudan a los equipos a trabajar juntos

Los puntos anteriores se escriben desde el punto de vista de un solo desarrollador que mantiene una aplicación. Las aplicaciones complejas serán mantenidas por equipos. Las pruebas garantizan que los colegas no rompan inadvertidamente su código (y que usted no lo rompa sin saber). Si desea ganarse la vida como programador de Django, debe ser bueno escribiendo pruebas.
