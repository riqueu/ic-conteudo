#!/bin/bash

# verifica argumento de entrada
if [ "$#" -ne 1 ] || [[ ! "$1" =~ ^[0-9]+$ ]]; then
    echo "Argumento invalido -> Uso: $0 <número de palavras>"
    exit 1
fi

n=$1

cat inicio.html > palavras.html

# ordena vocabulario.txt por ordem de frequencia e faz um loop que itera por n linhas
echo "<br>" >> palavras.html
sort -k2nr < vocabulario.txt | head -n "$n" | while read -r palavra ocorrencias; do
    # PROBLEMA 5 SEM A BONUS -> 'echo "<tr><td>$palavra</td>: <td>$ocorrencias</td></tr><br>" >> palavras.html'
    # Parte bonus:
    # se estiver no palavras_antigas.lst, pinta de vermelho e adiciona no palavras.html, caso não, só adiciona.
    if grep -q "^$palavra$" palavras_antigas.lst; then
        echo "    <tr><td><span style='color:red;'>$palavra</td>: <td>$ocorrencias</td></tr></span><br>" >> palavras.html
    else
        echo "    <tr><td>$palavra</td>: <td>$ocorrencias</td></tr><br>" >> palavras.html
    fi
done

# adiciona o fim da tabela no html e a sua parte final
echo "</table>" >> palavras.html
cat fim.html >> palavras.html
