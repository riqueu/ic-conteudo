#!/bin/bash

grep "Title: " "O_cortico.txt" | sed 's/Title: //g' 
echo "Linhas:" $(cat "O_cortico.txt" | wc -l)
echo "Palavras:" $(cat "O_cortico.txt" | wc -w)
echo "Caracteres:" $(cat "O_cortico.txt" | wc -m)
grep -r "Original publication: " "O_cortico.txt" | tail -c 5
