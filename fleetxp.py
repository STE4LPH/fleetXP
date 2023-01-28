import sys,time,os,pyfiglet

#Rojo
R = '\033[1;31m'
GR = '\0;37[1;37'
#Verde
V = '\033[1;32m'
GK='\033[92m'

#Oscuro Verde
S = '\033[92m'

#Amarillo
A = '\033[1;33m'

#Azul
Z = '\033[0;34m'

#Morado
M = '\033[1;35m'

#Celeste
C = '\033[1;36m'

#Blanco
B = '\033[37;m'

#Negro
G = '\033[0;30'

#Reiniciar
E = '\033[0m'
muro = M+"----------------------------------"+E
muo = Z+"\n----------------------------------"+E
print (muro)
print (V)
banner = pyfiglet.figlet_format("Fleet XP") 
print(banner+E) 
print (A+"Creador :", R+" PIRATE FOUNDER",C+"(Top 8)"+E)
print (muro)
def numberpost(valor):
    try:
        valor = int(valor)
        if valor > 0:
            return valor
        mh = R+"No se permiten números negativos puto "+E
        for k in mh:
        	sys.stdout.flush()
        	print (k,end="")
        	time.sleep(0.1)
        time.sleep(1)
        return False
    except:
        print(muo)
        mk = R+"\nPorque mierda pones {LETRAS} feo de mierda \n"+E
        for k in mk:
        	sys.stdout.flush()
        	print (k,end="")
        	time.sleep(0.1)
        time.sleep(1)
        print (muo)
        return False
##############################
def kram(pregunta):
    respuesta = False
    while respuesta is False:
        respuesta = numberpost(input(pregunta))
    return int(respuesta)
while True:
	jugador = "Player"
	name = input(f"\nNombre del [{A+jugador+E}] => "+E)
	print ("\n"+muro)
	name = name.title()
	level = kram(f"\nNivel de [{C+name+E}] => ")
	print ("\n"+muro)
	level_one = int(level) - 1
	anlecel =  str(level_one) + "9"
	result = int(anlecel) * level_one - 90000
	coding =  (format(result, ',d'))
	for i in coding:
		if i == ",":
			r = A+","+E
			whx = coding.replace(",",r)
	go = "XP"
	print (f"\nEl jugador {C+name+E} tiene {V+go+E}: {whx}\n")
	print (muro)
	print (muo)
	exit = R+"exit"+E
	print (A+f"\n- [{1}] {M}(Salir del programa)"+E)
	print (A+f"\n- [{2}] {M}(Seguir con el programa)"+E)
	print (muo)
	opcion = input("opciones => ")
	if opcion == "1":
		sys.exit()
