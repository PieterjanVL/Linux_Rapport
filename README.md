* Rapport gemaakt op [2022-12-11_20:13:02](rapport/2022-12-11_20-13-02.md) 


# Scripts:

De data werd verkregen aan de hand van een publieke api van de stad Gent, [link naar api](https://data.stad.gent/explore/dataset/real-time-bezettingen-fietsenstallingen-gent/api/). De temperatuur data werd gehaald van [deze site](https://api.openweathermap.org/data/2.5/weather?lat=51.05&lon=3.73&appid=143b019e2b0934a0d44afa8002c8e3ce&units=metric). [1_main.sh](1_main.sh) is het overkoepelende bashscript die de andere cripts aanroept. Het script exporteert 2 argumenten namelijk dir en timestamp. Dir bevat het path waar de ruwe data en het csv bestand opgeslaan moeten worden. De timestamp worrdt gebruikt om de ruwe data te kunnen titelen met als formaat YYYY-MM-DD_hh:mm:ss. Dit kunnen we ook terugvinden in [ruwe_data](/ruwe_data/).

[2_setup.sh](2_setup.sh) bevat 2 functies namelijk file_bestaat en dir_bestaat. File_bestaat kijkt of erop de opgegeven dir een [data.csv](data.csv) staat indien dit niet het geval is zal het het bestand aanmaken en ook de heading toevoegen. Indien [data.csv](data.csv) bestaat zal het controleren of eral een header is indien dit niet het geval is wordt deze toegevoegd. dir_bestaat controleert of een folder al dan niet bestaat, indien het niet bestaat wordt er eentje aangemaakt.

[3_data_verzamelen.sh](3_data_verzamelen.sh) wordt gebruikt om de ruwe data van dat moment te scrapen en in de folder ruwe_data te steken. Hiervoor gebruikte ik het commando curl. Het weer en bezetting fietsenstalling werd apart opgeslagen. Bestandsnaam maakt gebruik van de timestamp die [1_main.sh](1_main.sh) exporteert

