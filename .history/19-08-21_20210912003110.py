class Empresa:
    def __init__(self,nom="El mas barato",ruc="0999999999",tel="042971234",dir="Juan Montalvo"):
        self.nombre=nom
        self.ruc=ruc
        self.telefono=tel
        self.direccion=dir
    
    def mostrarEmpresa(self):
        print("Empresa: {:17}, RUC: {}".format(self.nombre,self.ruc))

class Cliente:
    def __init__(self,nom,ced,tel):
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel
    
    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)

class ClienteCorporativo(Cliente):
    def __init__(self,nomb,cedu,telecontrato):
        super().__init__(nomb,cedu,tele,contrato)
        self.__contrato=contrato


    @property
    def contrato(self):     #getter: obtener el valor del atributo privado
        return self.__contrato
    @contrato.setter
    def contrato(self,value):     #setter: asigna el valor del atributo privado
        if value:
            self.__contrato=value     
        else:
            self.__contrato="Sin contrato"            

    def mostrarCliente(self):
        print(self.nombre, self.__contrato)

class ClientePersonal(Cliente):
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom,ced,tel,)
        self.__promocion=promocion

    @property
    def promocion(self):     #getter: obtener el valor del atributo privado
        if self.__promocion==True:
            return "10% descuento"
        else:    
            return "No hay descuento"


    def mostrarCliente(self):
        print(self.nombre, self.__promocion)        
 

class Articulo:
    secuencia=0
    iva=0.12
    def __init__(self,des,pre,sto):
        Articulo.secuencia+=1
        self.codigo=Articulo.secuencia
        self.descripcion= des
        self.precio=pre
        self.stock=sto
    def mostraArticulo(self):
        print(self.codigo,self.nombre)

class DetVenta:
    linea=0
    def __init__(self,articulo,cantidad):
            DetVenta.linea+=1
            self.lineaDetalle=DetVenta.linea
            self.articulo=articulo
            self.precio=articulo.precio
            self.cantidad=cantidad

    def agregarDetaññe                        
class CabVenta:
    def __init__(self,fac,empresa,fecha,cliente,tot=0):
        self.empresa=empresa
        self.factura=fac
        self.fecha=fecha
        self.cliente=cliente
        self.total=tot
        self.detalleVen=[]




# emp=Empresa("El mas barato","0953156049","0998132446","Coop. Juan Montalvo")
# emp.mostrarEmpresa()
# print(emp.nombre)

cli1=ClientePersonal("Jose","0912231499","042567890",True)
cli1.mostrarCliente
art1=Articulo("Aceite",2,100)
art1.mostraArticulo()
art2=Articulo("Coca Cola",1,200)
art2.mostraArticulo()

art3=Articulo("Leche",1.5,200)
art3.mostraArticulo()
print(Articulo.iva())



