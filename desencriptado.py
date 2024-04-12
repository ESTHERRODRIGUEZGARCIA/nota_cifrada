import codecs

# Texto cifrado extraído del archivo
encrypted_text = """
Yn fvthvragr vasbeznpvba rf pbasvqrapvny. Gr nlhqnen n cebfrthve ra yn vairfgvtnpvba. Ab gr pbasvrf, ab gbqnf ynf vasbeznpvbarf qr ynf dhr qvfcbarzbf fba gna snpvyrf pbzb rfgn ebgnpvba qr pnenpgrerf. Sveznqb: ha nzvtb. 
synt{rfgnzbf_rzcrmnaqb_n_pbabpre_nytb_qr_uvfgbevn}
"""

# Aplicar ROT13 al texto cifrado
decrypted_text = codecs.decode(encrypted_text, 'rot_13')

# Imprimir el texto descifrado
print(decrypted_text)
