#!/bin/bash

> vocabulario.txt
# filtra as palavras começadas em letra minúscula maiores que 4 caracteres
grep -Eo '\b[a-z][a-zA-Z]{3,}\b' O_cortico.txt > palavrasM4.txt

# coloca essas palavras em um array sem elementos repetidos
mapfile -t palavras_unicas < <(awk '!a[$0]++' palavrasM4.txt)

# procura as ocorrencias de cada elemento do array no palavrasM4.txt e concatena ao vocabulario.txt
for palavra in "${palavras_unicas[@]}"; do
    ocorr=$(grep -w -c "$palavra" palavrasM4.txt)
    echo "$palavra $ocorr" >> vocabulario.txt
done
