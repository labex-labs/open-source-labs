# Implementar Send y Sync manualmente es inseguro

Debido a que los tipos compuestos por los rasgos `Send` y `Sync` son automáticamente `Send` y `Sync` también, no tenemos que implementar estos rasgos manualmente. Como rasgos marcadores, ni siquiera tienen métodos que implementar. Simplemente son útiles para imponer invariantes relacionados con la concurrencia.

Implementar manualmente estos rasgos implica escribir código Rust inseguro. Hablaremos sobre el uso de código Rust inseguro en el Capítulo 19; por ahora, la información importante es que construir nuevos tipos concurrentes que no estén compuestos por partes `Send` y `Sync` requiere un pensamiento cuidadoso para mantener las garantías de seguridad. "El Rustonomicon" en *https://doc.rust-lang.org/stable/nomicon* tiene más información sobre estas garantías y cómo mantenerlas.
