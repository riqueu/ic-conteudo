#!/bin/bash

# encontra todos os scripts no diretório
scripts=($(find * -name "*.sh"))

# loop por cada script, verificando sua primeira linha.
for script in ${scripts[@]}; do
    line=$(head -n 1 $script)
    # caso começe com #!/bin/bash, adiciona permissão para
    # o usuário e grupos de executar e remove de outros.
    if [ "$line" == "#!/bin/bash" ]; then
	    chmod ug+x,o-x "$script" # ou 'chmod 776 "$script"' para -rwxrwxrw-
    fi
done
