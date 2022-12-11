* Rapport gemaakt op [2022-12-11_20:13:02](rapport/2022-12-11_20-13-02.md) 


# Scripts:

De data werd opgenomen tussen 08/12/2022 tot en met 11/12/2022 adhv van een [crontab](crontab.sh) die om de 2 uur werd uitegvoerd. **IMPORTANT:** Na het opmaken van de grafieken is het mij opgevallen dat de bezetting van Braunplein altijd 24 is en dat dit waarschijnlijk niet klopt en een fout van de api is. 

De data werd verkregen aan de hand van een publieke api van de stad Gent, [link naar api](https://data.stad.gent/explore/dataset/real-time-bezettingen-fietsenstallingen-gent/api/). De temperatuur data werd gehaald van [deze site](https://api.openweathermap.org/data/2.5/weather?lat=51.05&lon=3.73&appid=143b019e2b0934a0d44afa8002c8e3ce&units=metric). [1_main.sh](1_main.sh) is het overkoepelende bashscript die de andere cripts aanroept. Het script exporteert 2 argumenten namelijk dir en timestamp. Dir bevat het path waar de ruwe data en het csv bestand opgeslaan moeten worden. De timestamp worrdt gebruikt om de ruwe data te kunnen titelen met als formaat YYYY-MM-DD_hh:mm:ss. Dit kunnen we ook terugvinden in [ruwe_data](/ruwe_data/).

[2_setup.sh](2_setup.sh) bevat 2 functies namelijk file_bestaat en dir_bestaat. File_bestaat kijkt of erop de opgegeven dir een [data.csv](data.csv) staat indien dit niet het geval is zal het het bestand aanmaken en ook de heading toevoegen. Indien [data.csv](data.csv) bestaat zal het controleren of eral een header is indien dit niet het geval is wordt deze toegevoegd. dir_bestaat controleert of een folder al dan niet bestaat, indien het niet bestaat wordt er eentje aangemaakt.

[3_data_verzamelen.sh](3_data_verzamelen.sh) wordt gebruikt om de ruwe data van dat moment te scrapen en in de folder ruwe_data te steken. Hiervoor gebruikte ik het commando curl. Het weer en bezetting fietsenstalling werd apart opgeslagen. De bestandsnaam maakt gebruik van de timestamp die [1_main.sh](1_main.sh) exporteert.

[4_data_transformeren.sh](4_data_transformeren.sh) gaat de ruwe data die in het vorige script werd verkegen filteren omzetten naar het juiste formaat en wegschijven naar [data.csv](data.csv). Het script gaat eerst de temp uit de juiste ruwe data file halen. Vervolgens zijn er 3 functie datum_omzetten, datum_eruit_halen, data_eruit_halen. datum_eruit_halen roept datum_omzetten aan om de gegeven datum die de functie er zelf heeft uitgefilterd om te zetten naar het juiste datumformaat. data_eruit_halen haalt de nodige data eruit die bij Braunplein hoort en daarna voor Korenmarkt. Op het einde worden deze waardes weggeschreven naar [data.csv](data.csv).

[5_data_analyseren.py](5_data_analyseren.py) en [6_raport_genereren.py](6_raport_genereren.py) worden gebruikt om 4 grafieken te generen en op te slaan in de folder [analyse](/analyse/). Vervolgens wordt er een markown gegenereert die deze grafieken verwerkt en een mooi rapport van maakt. Vervolgens wordt dit rapport met behulp van github pages online gezet.

**IMPORTANT:** [7_analyse.py](7_analyse.py) is file [5_data_analyseren.py](5_data_analyseren.py) en [6_raport_genereren.py](6_raport_genereren.py) samengevoegd. Dit heb ik gedaan zodanig dat ik gebruik kon maken van github actions. Deze [repo]( https://github.com/PieterjanVL/Linux_Rapport) kan je het gebruik van github actions zien. [5_data_analyseren.py](5_data_analyseren.py) en [6_raport_genereren.py](6_raport_genereren.py) worden niet meer gebruikt, maar je kan ze eenvoudig gebruiken als je de commentaar weghaald bij de scripts, ze zijn dus overbodig geworden door het gebruik van github actions.
De workflow wordt enkel uitevoerd wanneer er veranderingen zijn uitgevoerd en gepushed worden aan het bestand [data.csv](data.csv). Ook wordt github pages automatisch aangeroepen en de site veranderd. 

