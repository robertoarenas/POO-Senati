class Trabajador():
    def __init__(self,trabajador,Categoria,horasextras,Tardanza):
        self.trabajador=trabajador
        self.Categoria=Categoria
        self.horasextras=horasextras
        self.Tardanza=Tardanza
       
    def calcular(self):
        print("***DATOS DE ENTRADA***") 
        print("TRABAJADOR:           ",Trabajador1.trabajador)   
        print("CATEGORIA:            ",Trabajador1.Categoria)
        print("HORAS EXTRAS:         ",Trabajador1.horasextras)
        print("TARDANZAS: (minutos)  ",Trabajador1.Tardanza)
        
Trabajador1=Trabajador("Roberto Arenas","B",10,200)         

Trabajador1.calcular() 