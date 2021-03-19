import requests

def main():
    url_name = input("introduce la url: ")

    formato = ""
    i = len(url_name)-1
    while(i >= 0):
        formato += url_name[i]
        if(url_name[i] == "."):
            break
        i -= 1

    
    my_file = requests.get(url_name)
    file_name = input("nombre del fichero: ")
    f = open(file_name + formato[::-1],"wb")
    f.write(my_file.content)
    f.close()

if __name__ == "__main__":
    main()


Haz un programa que lee un fichero de texto con palabras y guarda estas palabras en unas listas.
Hay 27 listas, una lista para cada palabra. Cuando se mete una palabra nueva, hay que ver que este en orden alfabetico.
Finalmente cuando las tengas ordenadas, escribes las palabras en orden alfabetico sobre otro fichero

* los nombres de los ficheros son los que quieras (da igual hacerlo con o sin input)

fichero_lectura = "fichero1.txt"
fichero_escritura = "fichero2.txt"

hash_alfabeto = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

def posicionar(lista,palabra,posicion):
	lista.extend([""])
	for i in range(len(lista)-1,pos):
		lista[i+1] = lista[i]
	lista[pos] = palabra
	
def guardarPalabra(palabra):
	for i in range(0,len(hash_alfabeto[ord(palabra.lower()[0])-65])) :
		if (len(palabra)>len(hash_alfabeto[ord(palabra.lower()[0])-65][i])):
			for j in range(0,len(palabra)-1):
				if (palabra[j] < hash_alfabeto[ord(palabra.lower()[0])-65][i][j] or j == len(palabra)-1):
					posicionar(hash_alfabeto[ord(palabra.lower()[0])-65],palabra,i)
					break
				else:
					
					
		else:
			for j in range(0,len(i)-1):
			
		
		
		
		
