#! /usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd
#Finds the csv file
DIR = sys.argv[1]
#TIME = 'analyse/'+sys.argv[2]
TIME = 'analyse/' + str(sys.argv[2])
CSV_FILE = DIR + "/data.csv"
print(CSV_FILE)


df = pd.read_csv(CSV_FILE).drop_duplicates()
print(df)

#Datum omzetten:
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%d/%m/%y %H:%M:%S')
print(df)

#Algemene plot maken dat graden en bezetting bekijkt:
eerste_plot = df.pivot_table(index='graden', columns='facilityName', values='bezetting%', aggfunc='mean')
print(eerste_plot)
eerste_plot.plot(title='Invloed temperatuur bezetting fietsenstalling', xlabel='graden celsius', ylabel='bezetting in %')
plt.savefig(str(TIME)+'/grafiek1')

#Algemene plot maken dat datum en bezetting bekijkt:
tweede_plot = df.pivot_table(index='time', columns='facilityName', values='bezetting%', aggfunc='mean')
print(tweede_plot)
tweede_plot.plot(title='Bezetting wanneer data is opgenomen', xlabel='datum', ylabel='bezetting in %')
plt.savefig(str(TIME)+'/grafiek2')

#Mean plot maken dat graden en bezetting bekijkt:
derde_plot = df.pivot_table(index='time',values='bezetting%', aggfunc='mean')
print(derde_plot)
derde_plot.plot(title='Gemiddelde bezetting wanneer data is opgenomen', xlabel='datum', ylabel='bezetting in %', legend='test')
plt.savefig(str(TIME)+'/grafiek3')
#Gemiddelde bezetting wanneer data is opgenomen
#Algemene plot maken dat datum en bezetting bekijkt:
derde_plot = df.pivot_table(index='graden',values='bezetting%', aggfunc='mean')
print(derde_plot)
derde_plot.plot(title='Gemiddelde invloed temperatuur bezetting fietsenstalling', xlabel='graden', ylabel='bezetting in %')
plt.savefig(str(TIME)+'/grafiek4')
