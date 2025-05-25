# Publicando uma Nova Versão de uma Crate Existente

Quando você fez alterações em sua crate e está pronto para lançar uma nova versão, você altera o valor `version` especificado em seu arquivo `Cargo.toml` e republica. Use as regras de Versionamento Semântico (Semantic Versioning) em *http://semver.org* para decidir qual é o número da próxima versão apropriada, com base nos tipos de alterações que você fez. Em seguida, execute `cargo publish` para fazer o upload da nova versão.
