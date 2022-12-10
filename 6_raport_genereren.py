#! /usr/bin/python
from mdutils.mdutils import MdUtils
from mdutils import Html
import sys

DIR = sys.argv[1] + '/'
TIME = sys.argv[2]

RAPPORT = str(DIR) + 'analyse/' + 'analyse1' + '/'

LINK = '../analyse/' + str(TIME)

#/Users/pieterjan/Documents/linux-22-23-PieterjanVL/data-workflow/rapport/analyse/2022-12-07_23:24:09/test4.png



print(str(RAPPORT)+'test4.png')

mdFile = MdUtils(file_name=str(DIR)+ 'rapport/' + str(TIME), title='Invloed van temperatuur en tijdsaanduiding op de bezetting van fietsenstalling Braunplein en Korenmarkt te Gent. ')

mdFile.new_header(level=1, title='Inleiding')  # style is set 'atx' format by default.

mdFile.new_paragraph("Dit rapport beschrijft en analyseert de invloed van temperatuur en tijdsaanduiding op de bezetting van fietsenstalling Braunplein en Korenmarkt te Gent. De data werd verkregen aan de hand van een publieke api van de stad Gent, [link naar api](https://data.stad.gent/explore/dataset/real-time-bezettingen-fietsenstallingen-gent/api/) . Dit rapport is gemaakt voor het vak linux for data scientists aan de Hogent.   ")
mdFile.new_paragraph("**IMPORTANT:** dit rapport is gemaakt voor educatieve doeleinden, er kunnen fouten inzitten.")
mdFile.new_paragraph()

mdFile.new_header(level=1, title="Algemene analyse")
mdFile.new_paragraph("In de algemene analyse kijken we naar de gemmidelde waarde van beide fietsparkingen. Later in het rapport worden beide fietsparkingen apart besproken.")

mdFile.new_header(level=2, title="Invloed van temperatuur op de bezetting")
mdFile.new_paragraph(Html.image(LINK + '/grafiek4.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")

mdFile.new_header(level=2, title="Invloed van tijdsaanduiding op de bezetting")
mdFile.new_paragraph(Html.image(LINK + '/grafiek3.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")

# Available Features
mdFile.new_header(level=1, title="Individuele analyse")
mdFile.new_paragraph("De specifieke analyse bekijkt en analyseerd beide fietsparkingen apart.")

mdFile.new_header(level=2, title="Invloed van temperatuur op individuele bezetting")
mdFile.new_paragraph(Html.image(LINK + '/grafiek1.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie Braunplein: `` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")
mdFile.new_paragraph("``Conclusie Korenmarkt: `` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")

mdFile.new_header(level=2, title="Invloed van tijdsaanduiding op de individuele bezetting")
mdFile.new_paragraph(Html.image(LINK + '/grafiek2.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie Braunplein:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")
mdFile.new_paragraph("``Conclusie Korenmarkt:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")


mdFile.write('  \n')
mdFile.write('  \n')
mdFile.new_paragraph("Project gemaakt door [Pieterjan Van Landeghem](https://www.linkedin.com/in/pieterjan-van-landeghem-339b7b163/).")
mdFile.write('  \n')
mdFile.new_paragraph("Dit rapport is gemaakt voor het vak linux for data scientists aan de Hogent.")
mdFile.write('  \n')
mdFile.new_paragraph('Published on ' + str(TIME), align='center')
# Create a table of contents
mdFile.new_table_of_contents(table_title='Contents', depth=2)
mdFile.create_md_file()

