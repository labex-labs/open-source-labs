# Solução de Problemas

Para verificar se você instalou o Rust corretamente, abra um **novo shell** e insira esta linha:

```bash
# Open a new terminal first!
rustc --version
```

Você deve ver o número da versão, o hash do commit e a data do commit da versão estável mais recente que foi lançada, no seguinte formato:

```bash
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

Se você vir essas informações, você instalou o Rust com sucesso! Se você não vir essas informações, verifique se o Rust está na sua variável de sistema `%PATH%` da seguinte forma.

No Linux, use:

```bash
echo $PATH
```

Se tudo estiver correto e o Rust ainda não estiver funcionando, há vários lugares onde você pode obter ajuda. Descubra como entrar em contato com outros Rustaceans (um apelido engraçado que nos damos) na página da comunidade em *https://www.rust-lang.org/community*.
