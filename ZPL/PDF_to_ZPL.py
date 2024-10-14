from zplgrf import GRF

dpi = 210
width_mm = 27.94  
height_mm = 55.88  

width_dots = int(width_mm * dpi / 26 )
height_dots = int(height_mm * dpi / 28 )

with open('prova.pdf', 'rb') as pdf:
    pages = GRF.from_pdf(pdf.read(), 'DEMO', center_of_pixel=True, dpi=dpi, width=width_dots, height=height_dots)

with open("output2.zpl", "w") as zpl:
    for grf in pages:
        zpl.write(grf.to_zpl() + '\n')

with open("outputTXT2.txt", "w") as zpl:
    for grf in pages:
        zpl.write(grf.to_zpl() + '\n')