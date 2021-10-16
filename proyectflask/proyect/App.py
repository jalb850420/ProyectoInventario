from flask import Flask, render_template, request

App = Flask(__name__)

tipousuario = {
    101: "Super Amnistrador", 
    102: "Administrador", 
    103: "Usuario Final",     
}

listaproduct = {
    111: "Llantas", 
    222: "Rines", 
    333: "Espejos", 
    444: "Motor"
}

listaprov = {
    123: "CarrosST", 
    456: "MotorsSA", 
    789: "Carsport", 
    537: "Servicar"
}

@App.route('/', methods=["GET"])
def Home():
    return render_template('home.html')

@App.route('/', methods=["GET"])
def Inicio():
    return render_template('inicio.html')

@App.route('/Usuario', methods=["GET"])
def Usuario():
    return render_template('usuario.html')

@App.route('/Productos', methods=["GET"])
def Productos():
    return render_template('productos.html')

@App.route('/Proveedores', methods=["GET"])
def Proveedores():
    return render_template('proveedores.html')

@App.route('/Productos/<idproducto>', methods=["GET"])
def infoproduct(idproducto):
    try:
        idproducto=int(idproducto)
    except Exception as e:
            idproducto = 0
    
    if idproducto in listaproduct:
        return listaproduct[idproducto]
    else:
        return f"El Producto {idproducto} no existe"

@App.route('/Proveedores/<idproveedor>', methods=["GET"])
def infoproveedor(idproveedor):
    try:
        idproveedor=int(idproveedor)
    except Exception as e:
        idproveedor = 0

    if idproveedor in listaprov:
       return listaprov[idproveedor]
    else:
        return f"El Proveedor no existe: {idproveedor}"

@App.route('/Usuario/<idusuario>', methods=["GET"])
def infousuario(idusuario):
    try:
        idusuario=int(idusuario)
    except Exception as e:
        idusuario = 0
        
    if idusuario in tipousuario:
       return tipousuario[idusuario]
    else:
        return f"El usuario no existe: {idusuario}"

@App.errorhandler(404)
def not_found(error):
        return "La página no existe"

if __name__ == '__main__':
    App.run(debug = True)
