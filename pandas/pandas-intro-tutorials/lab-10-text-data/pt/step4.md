# Extrair Dados Específicos dos Passageiros

Em seguida, vamos extrair os dados dos passageiros para as condessas a bordo do Titanic. Usaremos o método `str.contains()` para encontrar as linhas onde a coluna `Name` contém a palavra 'Countess'.

```python
# Encontrar linhas onde 'Name' contém 'Countess'
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
