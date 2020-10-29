# Hier importeer je de os module
import os

# De huidige directory opvragen en oplaan in de variable: werkmap
werkmap = os.getcwd()

# De letters cwd staan voor: current working directory (de huidige map!)

# Op het scherm printen
print('De huidige map is: ' + werkmap)

mapnaam = ''

lengte_mapnaam = 0

while lengte_mapnaam == 0:
    mapnaam = input('Welke naam wil je voor de map?')
    lengte_mapnaam = len(mapnaam)

    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
        print('Je hebt geen naam ingevoerd')

print('De map' + mapnaam + 'is gemaakt.')

