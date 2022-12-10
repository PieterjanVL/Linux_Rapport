#!/bin/bash 
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

DIR=/Users/pieterjan/Documents/Linux_Rapport
timestamp=$(date +%F_%T)
timestamp2=$(date +%F_%H-%M-%S)

echo "${timestamp}"

export DIR
export timestamp
export timestamp2
./2_setup.sh
./3_data_verzamelen.sh
./4_data_transformeren.sh
#python3 ./5_data_analyseren.py "${DIR}" "${timestamp2}"
#python3 ./6_raport_genereren.py "${DIR}" "${timestamp2}"
#printf "* Rapport gemaakt op [%s](rapport/%s.md)\n" "${timestamp}" "${timestamp2}" | cat - README.md > temp && mv temp README.md
