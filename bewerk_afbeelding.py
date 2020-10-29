from PIL import Image

# Dit is de afbeelding.
afbeelding = Image.open('hofner.jpg')

# Hier laat hij de afbeelding zien.
afbeelding.show()

# De lengte en breedte van de afbeelding.
breedte = afbeelding.width
hoogte = afbeelding.height

# De helft van de lengte en breedte van de afbeelding.
helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('hofner.jpg')
