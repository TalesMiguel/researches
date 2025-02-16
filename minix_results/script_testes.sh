#!/bin/sh

# Lista de testes
TESTES="10 100 10000
50 1000 10000
100 10000 100000
200 15000 150000"

# Contador do número do teste
NUM_TESTE=1

for PARAMS in $TESTES; do
    echo "Executando teste $NUM_TESTE..."
    ./teste_processos $PARAMS > "minix_results/resultados_lottery_$NUM_TESTE.txt"
    # Garantir que o próximo teste só será iniciado após a finalização do anterior
    wait
    echo "Teste $NUM_TESTE concluído!"
    NUM_TESTE=$((NUM_TESTE + 1))
done

echo "Todos os testes foram executados."
echo "Lembre-se de dar reboot!!!"
