from PIL import Image, ImageFont, ImageDraw

afbeelding = Image.open('meme_background.jpg')


breedte = afbeelding.width
hoogte = afbeelding.height

print(afbeelding.width)
print(afbeelding.height)

# Breedte = 640
# Hoogte = 480

lettertype = ImageFont.truetype('impact', 40)

tekengebied = ImageDraw.Draw(afbeelding)

tekst = 'GET RICK ROLLED!'

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print('tekstbreedte=' + str(tekst_breedte) + ', tekst_hoogte=' + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2

tekengebied.multiline_text((tekst_x,tekst_y), tekst, font=lettertype, fill=(0,0,0))

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))


afbeelding.show()

afbeelding.save('meme_met_tekst.jpg')

# tekstbreedte=274, teksthoogte=86

