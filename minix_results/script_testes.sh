#!/bin/sh

# Lista de testes
TESTES="10 100 10000
50 1000 10000
100 10000 100000
200 15000 150000"

NUM_TESTE=1

for PARAMS in $TESTES; do
    echo "Executando teste $NUM_TESTE..."
    ./teste_processos $PARAMS > "resultados_lottery_$NUM_TESTE.txt"
    echo "Teste $NUM_TESTE concluído!"
    NUM_TESTE=$((NUM_TESTE + 1))
done

echo "Todos os testes foram executados."
echo "Lembre-se de dar reboot!!!"
