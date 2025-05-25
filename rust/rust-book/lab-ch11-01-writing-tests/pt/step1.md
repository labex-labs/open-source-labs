# Como Escrever Testes

Testes são funções Rust que verificam se o código que não é de teste está funcionando da maneira esperada. Os corpos das funções de teste normalmente executam estas três ações:

- Configurar quaisquer dados ou estado necessários.
- Executar o código que você deseja testar.
- Afirmar (Assert) que os resultados são o que você espera.

Vamos analisar os recursos que o Rust fornece especificamente para escrever testes que executam essas ações, que incluem o atributo `test`, algumas macros e o atributo `should_panic`.
