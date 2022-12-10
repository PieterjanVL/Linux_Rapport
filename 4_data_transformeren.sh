#!/bin/bash 
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

RUWE_DATA="$DIR"/ruwe_data/
CSV_FILE="$DIR"/data.csv

file_fiets="${RUWE_DATA}"/"fietsenstalling_${timestamp}".json
file_weer="${RUWE_DATA}"/"weer_${timestamp}".json

#braunPlein_time=`jq -r ' .records[] | select(.fields.facilityname=="Braunplein") | [.fields.time] | @csv'  "${file_fiets}"`
#korenMarkt_time=`jq -r ' .records[] | select(.fields.facilityname=="Korenmarkt") | [.fields.time] | @csv'  "${file_fiets}"`

temp=`jq -r '.main | [.temp ]| @csv' "${file_weer}"`

datum_omzetten() {
    echo "${1}"| cut -c 2- |sed 's/\(.*\)T\([0-9]*:[0-9]*\).*/\1 \2/'
}

datum_eruit_halen() {
    datum=`echo | jq -r ' .records[] | select(.fields.facilityname=="Braunplein") | [.fields.time] | @csv'  "${file_fiets}"`
    echo `datum_omzetten "${datum}" `
}

data_eruit_halen(){
    echo `jq -r " .records[] | select(.fields.facilityname=="${1}") | [.fields.facilityname, .fields.bezetting] | @csv"  "${file_fiets}"`
    
}


#echo `datum_omzetten "${braunPlein_time}"`,`data_eruit_halen '"Braunplein"'`,"$temp" >> "${CSV_FILE}"
#echo `datum_omzetten "${korenMarkt_time}"`,`data_eruit_halen '"Korenmarkt"'`,"$temp" >> "${CSV_FILE}"

echo `datum_eruit_halen "Braunplein"`,`data_eruit_halen '"Braunplein"'`,"$temp" >> "${CSV_FILE}"
echo `datum_eruit_halen "Korenmarkt"`,`data_eruit_halen '"Korenmarkt"'`,"$temp" >> "${CSV_FILE}"



