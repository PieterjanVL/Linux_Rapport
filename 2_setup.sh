#!/bin/bash 
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes


CSV_FILE="${DIR}"/data.csv
RUWE_DATA="${DIR}"/ruwe_data/
RAPPORRT="${DIR}"/rapport/
ANALYSE="${DIR}"/analyse/

#Kijken of het csv bestand bestaat en eventueel toevoegen
file_bestaat(){
  if [ ! -f  "${1}" ]; then
      #echo "$CSV_FILE doesn't exists."
      echo "time,facilityName,bezetting%,graden" >"${1}"
      else
          if ! grep -q '[^[:space:]]' "${1}";then #Checks if the csv file has header, if not it adds one
              #echo 'Bestand is leeg'
              echo "time,facilityName,bezetting%,graden" > "${2}"
          fi
  fi
}

dir_bestaat(){
    if [ ! -d "${1}" ]; then
    ### Take action if $DIR exists ###
    #echo "DIR bestaat nog niet"
    mkdir "${DIR}"/"${2}"
fi   
}

file_bestaat "${CSV_FILE}" "data.csv"
dir_bestaat "${RUWE_DATA}" "ruwe_data"
dir_bestaat "${RAPPORRT}" "rapport"
dir_bestaat "${ANALYSE}" "analyse"
#dir_bestaat "${ANALYSE}${timestamp2}" "analyse/${timestamp2}"


