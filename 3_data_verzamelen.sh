#!/bin/bash 
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

#URL: data ophalen
URL1="https://data.stad.gent/api/records/1.0/search/?dataset=real-time-bezettingen-fietsenstallingen-gent&q=&facet=facilityname&timezone=Europe%2FBrussels"
URL2="https://api.openweathermap.org/data/2.5/weather?lat=51.05&lon=3.73&appid=143b019e2b0934a0d44afa8002c8e3ce&units=metric" 

RUWE_DATA="$DIR"/ruwe_data/

file_fiets="${RUWE_DATA}"/"fietsenstalling_${timestamp}".json
file_weer="${RUWE_DATA}"/"weer_${timestamp}".json


curl -s "$URL1" --http1.1 | jq . >> "${file_fiets}"
curl -s "$URL2" | jq . >> "${file_weer}"


