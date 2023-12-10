from Modelos.PedidoProducto import PedidoProducto
from Modelos.Producto import Producto
from Modelos.Pedido import Pedido
from Repositorios.RepositorioPedidoProducto import RepositorioPedidoProducto
from Repositorios.RepositorioProducto import RepositorioProducto
from Repositorios.RepositorioPedido import RepositorioPedido

class ControladorPedidoProducto():

    def __init__(self):
        self.repositorioPedidoProdudcto = RepositorioPedidoProducto()
        self.repositorioProducto = RepositorioProducto()
        self.repositorioPedido = RepositorioPedido()

    def index(self):
        return self.repositorioPedidoProdudcto.findAll()

    def create(self, infoPediddoProducto , id_producto, id_pedido):
        nuevoPedidoProducto = PedidoProducto(infoPediddoProducto)
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        elpedido = Pedido(self.repositorioPedido.findById(id_pedido))
        nuevoPedidoProducto.producto = elProducto
        nuevoPedidoProducto.pedido = elpedido
        return self.repositorioPedidoProdudcto.save(nuevoPedidoProducto)

    def show(self, id):
        elPedidoProducto = PedidoProducto(self.repositorioPedidoProdudcto.findById(id))
        return elPedidoProducto.__dict__

    def update(self, id, infoPediddoProducto, id_producto, id_pedido):
        elPedidoProducto = PedidoProducto(self.repositorioPedidoProdudcto.findById(id))
        elPedidoProducto.cantidad = infoPediddoProducto["cantidad"]
        elPedidoProducto.descripcion = infoPediddoProducto["descripcion"]
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        elpedido = Pedido(self.repositorioPedido.findById(id_pedido))
        elPedidoProducto.producto = elProducto
        elPedidoProducto.pedido = elpedido
        return self.repositorioPedidoProdudcto.save(elPedidoProducto)

    def delete(self, id):
        return self.repositorioPedidoProdudcto.delete(id)
