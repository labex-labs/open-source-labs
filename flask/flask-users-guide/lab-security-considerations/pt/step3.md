# Segurança JSON

Em Flask, é importante garantir a segurança das respostas JSON. Em versões anteriores ao Flask 0.10, arrays de nível superior não eram serializados para JSON devido a uma vulnerabilidade de segurança. No entanto, esse comportamento foi alterado, e arrays de nível superior agora são serializados. É recomendado usar a versão mais recente do Flask para aproveitar essa melhoria de segurança.
