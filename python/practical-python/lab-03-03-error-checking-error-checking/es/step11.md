# Mejores prácticas para excepciones

No captures excepciones. Fallo rápido y con ruido. Si es importante, alguien más se ocupará del problema. Solo captura una excepción si eres _ese_ alguien. Es decir, solo captura errores donde puedas recuperarte y seguir adelante de manera razonable.
