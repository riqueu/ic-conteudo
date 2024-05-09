#!/bin/bash

> ocorrencias.txt
# cria um array com todas as palavras em palavras_antigas.lst (sem repetidas na array)
mapfile -t palavras < <(awk '!a[$0]++' palavras_antigas.lst)

# roda um loop que conta a ocorrencia de cada palavra e adiciona ela no ocorrencias.txt
for palavra in "${palavras[@]}"; do
    ocorr=$(grep -w -c "$palavra" O_cortico.txt)
    echo "$palavra $ocorr" >> ocorrencias.txt
done
