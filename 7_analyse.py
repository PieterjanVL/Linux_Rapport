import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime
from mdutils.mdutils import MdUtils
from mdutils import Html

now = datetime.now()

dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")

dt_string2 = now.strftime("%Y-%m-%d_%H:%M:%S")

#print(dt_string + 'en ' + dt_string2)

save_grafiek = os.getcwd()+'/analyse/' + str(dt_string)

#print(os.path.exists(os.getcwd()))
#print('File is gemaakt' + os.getcwd())

#print(os.path.exists(os.getcwd() + '/analyse/2022-12-08_18-48-34'))
#print('File is gemaakt' + os.getcwd() + '/analyse')

os.makedirs(os.getcwd() + '/analyse/' + dt_string)

#print(os.path.exists(os.getcwd() + '/analyse/' + dt_string))

df = pd.read_csv(os.getcwd() + '/data.csv').drop_duplicates()
#print(df)

#Datum omzetten:
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%d/%m/%y %H:%M:%S')
#print(df)

#Algemene plot maken dat graden en bezetting bekijkt:
eerste_plot = df.pivot_table(index='graden', columns='facilityName', values='bezetting%', aggfunc='mean')
#print(eerste_plot)
eerste_plot.plot(title='Invloed temperatuur bezetting fietsenstalling', xlabel='graden celsius', ylabel='bezetting in %')
plt.savefig(save_grafiek+'/grafiek1')

#Algemene plot maken dat datum en bezetting bekijkt:
tweede_plot = df.pivot_table(index='time', columns='facilityName', values='bezetting%', aggfunc='mean')
#print(tweede_plot)
tweede_plot.plot(title='Bezetting wanneer data is opgenomen', xlabel='datum', ylabel='bezetting in %')
plt.savefig(save_grafiek+'/grafiek2')

#Mean plot maken dat graden en bezetting bekijkt:
derde_plot = df.pivot_table(index='time',values='bezetting%', aggfunc='mean')
#print(derde_plot)
derde_plot.plot(title='Gemiddelde invloed temperatuur bezetting fietsenstalling', xlabel='datum', ylabel='bezetting in %', legend='test')
plt.savefig(save_grafiek+'/grafiek3')

#Algemene plot maken dat datum en bezetting bekijkt:
vierde_plot = df.pivot_table(index='graden',values='bezetting%', aggfunc='mean')
#print(derde_plot)
vierde_plot.plot(title='Gemiddelde bezetting wanneer data is opgenomen', xlabel='graden', ylabel='bezetting in %')
plt.savefig(save_grafiek+'/grafiek4')

##################################################RAPORT###########################################################

rapport_link = os.getcwd()+'/rapport/' + str(dt_string)

#print(rapport_link)

mdFile = MdUtils(file_name=rapport_link, title='Invloed van temperatuur en tijdsaanduiding op de bezetting van fietsenstalling Braunplein en Korenmarkt te Gent. ')

mdFile.new_header(level=1, title='Inleiding')  # style is set 'atx' format by default.

mdFile.new_paragraph("Dit rapport beschrijft en analyseert de invloed van temperatuur en tijdsaanduiding op de bezetting van fietsenstalling Braunplein en Korenmarkt te Gent. De data werd verkregen aan de hand van een publieke api van de stad Gent, [link naar api](https://data.stad.gent/explore/dataset/real-time-bezettingen-fietsenstallingen-gent/api/) . Dit rapport is gemaakt voor het vak linux for data scientists aan de Hogent.   ")
mdFile.new_paragraph("**IMPORTANT:** dit rapport is gemaakt voor educatieve doeleinden, er kunnen fouten inzitten.")
mdFile.new_paragraph()

mdFile.new_header(level=1, title="Algemene analyse")
mdFile.new_paragraph("In de algemene analyse kijken we naar de gemmidelde waarde van beide fietsparkingen. Later in het rapport worden beide fietsparkingen apart besproken.")

mdFile.new_header(level=2, title="Invloed van temperatuur op de bezetting")
mdFile.new_paragraph(Html.image('../analyse/'+ str(dt_string) +'/grafiek4.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")

mdFile.new_header(level=2, title="Invloed van tijdsaanduiding op de bezetting")
mdFile.new_paragraph(Html.image('../analyse/'+ str(dt_string) +'/grafiek3.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")

# Available Features
mdFile.new_header(level=1, title="Individuele analyse")
mdFile.new_paragraph("De specifieke analyse bekijkt en analyseerd beide fietsparkingen apart.")

mdFile.new_header(level=2, title="Invloed van temperatuur op individuele bezetting")
mdFile.new_paragraph(Html.image('../analyse/'+ str(dt_string) +'/grafiek1.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie Braunplein: `` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")
mdFile.new_paragraph("``Conclusie Korenmarkt: `` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")

mdFile.new_header(level=2, title="Invloed van tijdsaanduiding op de individuele bezetting")
mdFile.new_paragraph(Html.image('../analyse/'+ str(dt_string) +'/grafiek2.png', size='400x300', align='center'))
mdFile.new_paragraph("``Conclusie Braunplein:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")
mdFile.new_paragraph("``Conclusie Korenmarkt:`` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra interdum vestibulum. Sed feugiat suscipit suscipit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum congue velit, non aliquet ante sollicitudin eget. Vestibulum ligula augue, luctus sed tortor eget, ornare pellentesque tortor. Fusce scelerisque arcu a augue condimentum commodo. Praesent id rhoncus mauris, et ornare augue. Donec a lectus quis massa vulputate ullamcorper.")


mdFile.write('  \n')
mdFile.write('  \n')
mdFile.new_paragraph("Project gemaakt door [Pieterjan Van Landeghem](https://www.linkedin.com/in/pieterjan-van-landeghem-339b7b163/).")
mdFile.write('  \n')
mdFile.new_paragraph("Dit rapport is gemaakt voor het vak linux for data scientists aan de Hogent.")
mdFile.write('  \n')
mdFile.new_paragraph('Published on ' + str(dt_string2 ), align='center')
# Create a table of contents
mdFile.new_table_of_contents(table_title='Contents', depth=2)
mdFile.create_md_file()
################################################################################





one_line = '* Rapport gemaakt op [' + str(dt_string2) + '](rapport/' + str(dt_string) + '.md) \n'
with open(os.getcwd() + '/README.md', 'r+') as fp:
    lines = fp.readlines()     # lines is list of line, each element '...\n'
    lines.insert(0, one_line)  # you can use any index if you know the line index
    fp.seek(0)                 # file pointer locates at the beginning to write the whole file again
    fp.writelines(lines) 