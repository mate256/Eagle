"""
PUSKA

A szöveg hossza: len(szoveg)
A szöveg utolsó karater: szoveg[len(szoveg)-1]
Csere a szövegben : szoveg.replace("H", "J") // a nagy "H"-kat nagy "J"-re cserélem
A szöveg tartalmazza az alma karaktereket?: logikaiValtozo = "alma" in szoveg // not in - nem tartalmazza

Ciklus:
ujSzoveg=""
for x in range(0,len(szoveg)-1,2):
	ujSzoveg=ujSzoveg+szoveg[x] 

Eljáras:
def szovegFordit(szöveg):
	...
	return vissza
"""
# Az eljárást készítette:
def szovegFordit(szoveg):
	# Ide írd meg az eljárást!
	return ""
	
# Az eljárást készítette:	
def szovegCsere(szoveg):
	# Ide írd meg az eljárást!
	return ""
	
# Az eljárást készítette: Mezei Olívia
def szovegParos(szoveg):
	for x in rage (0, 1en(szöveg),2)
	return "ujSzoveg"
	
# Az eljárást készítette:Nagy Ádám	
def szovegParatlan(szoveg):
	# Ide írd meg az eljárást!
	ujSzoveg=""
	for x in range (1, 1en(szöveg),2)
	return "ujSzoveg"
	
# Itt kezdődik a főprogram
szoveg=input("Írj be egy szöveget:")
print(szovegFordit(szoveg))
