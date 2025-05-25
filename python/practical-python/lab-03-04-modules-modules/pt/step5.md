# Execução do Módulo

Quando um módulo é importado, _todas as instruções no módulo são executadas_ uma após a outra até o final do arquivo ser alcançado. O conteúdo do namespace (espaço de nomes) do módulo são todos os nomes _globais_ que ainda estão definidos no final do processo de execução. Se houver instruções de script que realizam tarefas no escopo global (impressão, criação de arquivos, etc.), você as verá rodar na importação.
