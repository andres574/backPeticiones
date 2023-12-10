from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEmpleado import ControladorEmpleado
from Controladores.ControladorProducto import ControladorProducto
from Controladores.ControladorPedido import ControladorPedido
from Controladores.ControladorPedidoProducto import ControladorPedidoProducto

app = Flask(__name__)
cors = CORS(app)

miControladorEmpleado = ControladorEmpleado()
miControladorPruducto = ControladorProducto()
miControladorPedido = ControladorPedido()
miControladorPedidoProducto = ControladorPedidoProducto()



@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ...jhon leon"
    return jsonify(json)

""""

GESTION DE EMPLEADOS 

"""
@app.route("/empleado",methods=['GET'])
def getEmpleado():
    json=miControladorEmpleado.index()
    return jsonify(json)

@app.route("/empleado",methods=['POST'])
def crearEmpleado():
    data = request.get_json()
    json = miControladorEmpleado.create(data)
    return jsonify(json)

@app.route("/empleado/<string:id>",methods=['GET'])
def getEmpleados(id):
    json=miControladorEmpleado.show(id)
    return jsonify(json)

@app.route("/empleado/<string:id>",methods=['PUT'])
def modificarEmpleado(id):
    data = request.get_json()
    json=miControladorEmpleado.update(id,data)
    return jsonify(json)

@app.route("/empleado/<string:id>",methods=['DELETE'])
def eliminarEmpleado(id):
    json=miControladorEmpleado.delete(id)
    return jsonify(json)


"""

GESTION DE PRODUCTOS

 
"""

@app.route("/producto",methods=['GET'])
def getProductos():
    json=miControladorPruducto.index()
    return jsonify(json)

@app.route("/producto",methods=['POST'])
def creaProducto():
    data = request.get_json()
    json = miControladorPruducto.create(data)
    return jsonify(json)

@app.route("/producto/<string:id>",methods=['GET'])
def getProducto(id):
    json=miControladorPruducto.show(id)
    return jsonify(json)

@app.route("/producto/<string:id>",methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json=miControladorPruducto.update(id,data)
    return jsonify(json)

@app.route("/producto/<string:id>",methods=['DELETE'])
def eliminarProducto(id):
    json=miControladorPruducto.delete(id)
    return jsonify(json)

"""

  GESTION DE PEDIDOS 

"""

@app.route("/pedido",methods=['GET'])
def getPedidos():
    json=miControladorPedido.index()
    return jsonify(json)

@app.route("/pedido",methods=['POST'])
def creaPedido():
    data = request.get_json()
    json = miControladorPedido.create(data)
    return jsonify(json)

@app.route("/pedido/<string:id>",methods=['GET'])
def getPedido(id):
    json=miControladorPedido.show(id)
    return jsonify(json)

@app.route("/pedido/<string:id>",methods=['PUT'])
def modificarPedido(id):
    data = request.get_json()
    json=miControladorPedido.update(id,data)
    return jsonify(json)

@app.route("/pedido/<string:id>",methods=['DELETE'])
def eliminarPedido(id):
    json=miControladorPedido.delete(id)
    return jsonify(json)

@app.route("/pedido/<string:id>/empleado/<string:id_empleado>", methods=['PUT'])
def asignarEmpleadoPedido(id, id_empleado):
    json = miControladorPedido.asignarEmpleado(id, id_empleado)
    return jsonify(json)


"""

  PEDIDO DE PRODUCTO PLAZA DE MERCADO  

"""

@app.route("/pedidoProducto", methods=['GET'])
def getPedidoProductos():
    json = miControladorPedidoProducto.index()
    return jsonify(json)

@app.route("/pedidoProducto/<string:id>", methods=['GET'])
def getPedidoProducto(id):
    json = miControladorPedidoProducto.show(id)
    return jsonify(json)

@app.route("/pedidoProducto/producto/<string:id_producto>/pedido/<string:id_pedido>", methods=['POST'])
def crearPedidoProduto(id_producto, id_pedido):
    data = request.get_json()
    json = miControladorPedidoProducto.create(data,id_producto,id_pedido)
    return jsonify(json)

@app.route("/pedidoProducto/<string:id_Pedidoproducto>/producto/<string:id_producto>/pedido/<string:id_pedido>", methods=['PUT'])
def modificarPedidoProducto(id_Pedidoproducto, id_producto, id_pedido):
    data = request.get_json()
    json = miControladorPedidoProducto.update(id_Pedidoproducto, data, id_producto, id_pedido)
    return jsonify(json)


@app.route("/pedidoProducto/<string:id_PedidoProducto>", methods=['DELETE'])
def eliminarPedidoProducto(id_PedidoProducto):
    json = miControladorPedidoProducto.delete(id_PedidoProducto)
    return jsonify(json)



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__== '__main__':
     dataConfig = loadFileConfig()
     print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
     serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])