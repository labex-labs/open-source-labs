# Atualizando um Hash Map

Embora o número de pares chave-valor seja expansível, cada chave única pode ter apenas um valor associado a ela por vez (mas não o contrário: por exemplo, tanto a equipe Azul quanto a equipe Amarela podem ter o valor `10` armazenado no hash map `scores`).

Quando você deseja alterar os dados em um hash map, você precisa decidir como lidar com o caso em que uma chave já tem um valor atribuído. Você pode substituir o valor antigo pelo novo valor, desconsiderando completamente o valor antigo. Você pode manter o valor antigo e ignorar o novo valor, adicionando o novo valor somente se a chave _não_ já tiver um valor. Ou você pode combinar o valor antigo e o novo valor. Vamos ver como fazer cada um desses!
