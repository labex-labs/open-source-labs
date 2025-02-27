# Cuando usar código inseguro

Usar `unsafe` para utilizar una de las cinco "superpoderes" que acabamos de discutir no está mal o ni siquiera es reprobado, pero es más difícil hacer que el código `unsafe` sea correcto porque el compilador no puede ayudar a mantener la seguridad de la memoria. Cuando tienes una razón para usar código `unsafe`, puedes hacerlo, y tener la anotación `unsafe` explícita hace más fácil localizar la fuente de problemas cuando ocurren.
