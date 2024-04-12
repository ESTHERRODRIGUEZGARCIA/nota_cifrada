from collections import Counter

# Texto cifrado
texto_cifrado = "Yn fvthvragr vasbeznpvba rf pbasvqrapvny. Gr nlhqnen n cebfrthve ra yn vairfgvtnpvba. Ab gr pbasvrf, ab gbqnf ynf vasbeznpvbarf qr ynf dhr qvfcbarzbf fba gna snpvyrf pbzb rfgn ebgnpvba qr pnenpgrerf. Sveznqb: ha nzvtb. synt{rfgnzbf_rzcrmnaqb_n_pbabpre_nytb_qr_uvfgbevn}"

# Contar frecuencia de caracteres
frecuencia_caracteres = Counter(texto_cifrado.lower().replace(" ", "").replace(".", "").replace("{", "").replace("}", "").replace(":", "").replace(",", "").replace("-", ""))

# Ordenar por frecuencia
frecuencia_ordenada = sorted(frecuencia_caracteres.items(), key=lambda x: x[1], reverse=True)

# Mostrar resultados
print("Frecuencia de caracteres en el texto cifrado:")
for letra, frecuencia in frecuencia_ordenada:
    print(letra, ":", frecuencia)
