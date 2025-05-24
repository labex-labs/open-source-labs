# Resumo

O laboratório Signals demonstra como lidar com sinais Unix em programas Go usando canais. Ao criar um canal com buffer para receber notificações `os.Signal` e registrar o canal para receber notificações de sinais especificados usando `signal.Notify`, podemos lidar graciosamente com sinais e sair do programa quando o sinal esperado é recebido.
