# Implementar Send e Sync Manualmente é Inseguro

Como os tipos que são compostos pelas traits `Send` e `Sync` são automaticamente também `Send` e `Sync`, não precisamos implementar essas traits manualmente. Como traits marcadores, elas nem sequer têm nenhum método para implementar. Elas são apenas úteis para impor invariantes relacionadas à concorrência.

Implementar manualmente essas traits envolve implementar código Rust inseguro (unsafe). Falaremos sobre o uso de código Rust inseguro no Capítulo 19; por enquanto, a informação importante é que a construção de novos tipos concorrentes que não são compostos por partes `Send` e `Sync` requer uma reflexão cuidadosa para manter as garantias de segurança. "The Rustonomicon" em *https://doc.rust-lang.org/stable/nomicon* tem mais informações sobre essas garantias e como mantê-las.
