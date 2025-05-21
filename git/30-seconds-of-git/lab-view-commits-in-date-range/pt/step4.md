# Usando Datas Relativas e Opções de Formatação

O Git também suporta datas relativas, o que pode ser muito conveniente para visualizar rapidamente a atividade recente.

Vamos visualizar todos os commits das últimas 12 semanas:

```bash
git log --since='12 weeks ago'
```

Dependendo de quando você estiver executando este comando, você pode ver todos os commits ou apenas alguns deles, se eles se enquadrarem nesse período de tempo.

Outros formatos de data relativa úteis incluem:

- `"X days ago"` (há X dias)
- `"X months ago"` (há X meses)
- `"yesterday"` (ontem)
- `"last week"` (semana passada)

Vamos tentar visualizar commits do último ano:

```bash
git log --since='1 year ago'
```

Este comando mostrará todos os commits feitos no último ano.

## Opções de Formatação Adicionais

O `git log` fornece várias opções de formatação para personalizar a saída. Aqui estão algumas úteis:

1. Para exibir um log mais conciso com cada commit em uma única linha:

```bash
git log --oneline --since='Apr 25 2023' --until='Apr 27 2023'
```

A saída será semelhante a:

```
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

2. Para ver os arquivos que foram alterados em cada commit:

```bash
git log --name-status --since='Apr 25 2023' --until='Apr 27 2023'
```

Este comando mostra o status dos arquivos que foram modificados em cada commit, o que pode ser útil para entender o que foi alterado.

Essas opções de formatação podem ser combinadas com filtros de data para criar consultas poderosas que ajudam você a entender o histórico de um projeto de forma mais eficaz.
