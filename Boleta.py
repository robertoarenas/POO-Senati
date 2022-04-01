from Trabajador import Trabajador


class Boleta:
    def __init__(self,nombre,categoria,he,mt):
        self.nombre=nombre
        self.categoria=categoria
        self.horaExtra=he
        self.tardanza=mt
    
    # VALIDACION DE TIPO DE EMPLEADO
    
    def resultado (self):
        if self.categoria.lower() =="a":
            salary=3000 
            
            descuentoTardanza=((salary/240)/60)*self.tardanza
            pagoPorHorasExtras= (salary/240)*self.horaExtra
            print("***BOLETA DE PAGO***")
            print("NOMBRE:                  ",self.nombre)
            print("CATEGORIA:               ",self.categoria)
            print("SUELDO BASICO:           ",salary)
            print("DESCUENTO TARDANZA:      ",descuentoTardanza)
            print("PAGO POR HORAS EXTRAS:   ",pagoPorHorasExtras)
            print("SUELDO NETO:             ",salary - descuentoTardanza + pagoPorHorasExtras)

        elif  self.categoria.lower() =="b":
              salary=2500 
              descuentoTardanza=((salary/240)/60)*self.tardanza
              pagoPorHorasExtras= (salary/240)*self.horaExtra
              print("***BOLETA DE PAGO***")
              print("NOMBRE:                ",self.nombre)
              print("CATEGORIA:             ",self.categoria)
              print("SUELDO BASICO:         ",salary)
              print("DESCUENTO TARDANZA:    ",round(descuentoTardanza,2))
              print("PAGO POR HORAS EXTRAS: ",round(pagoPorHorasExtras,2))
              print("SUELDO NETO:           ",round(salary - descuentoTardanza + pagoPorHorasExtras,2))

            
        elif  self.categoria.lower() =="c":
                salary=2000 
                descuentoTardanza=((salary/240)/60)*self.tardanza
                pagoPorHorasExtras= (salary/240)*self.horaExtra
                print("***BOLETA DE PAGO***")
                print("  ")
                print("NOMBRE:                ",self.nombre)
                print("CATEGORIA:             ",self.categoria)
                print("SUELDO BASICO:         ",salary)
                print("DESCUENTO TARDANZA:    ",descuentoTardanza)
                print("PAGO POR HORAS EXTRAS: ",pagoPorHorasExtras)
                print("SUELDO NETO:           ",salary - descuentoTardanza + pagoPorHorasExtras)
                
        else:
            print("Categoría no válida")
                
                
Trabajador1=Boleta("Roberto Arenas","B",10,200)         

Trabajador1.resultado()                 
            
            
