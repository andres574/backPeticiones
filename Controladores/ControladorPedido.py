from Repositorios.RepositorioPedido import RepositorioPedido
from Repositorios.RepositorioEmpleado import RepositorioEmpleado
from Modelos.Pedido import Pedido
from Modelos.Empleado import Empleado

class ControladorPedido():
    def __init__(self):
        self.repositorioPedido = RepositorioPedido()
        self.repositorioEmpleado = RepositorioEmpleado()

    def index(self):
        return self.repositorioPedido.findAll()

    def create(self, infopedido):
        nuevoPedido = Pedido(infopedido)
        return self.repositorioPedido.save(nuevoPedido)

    def show(self, id):
        elPedido = Pedido(self.repositorioPedido.findById(id))
        return elPedido.__dict__

    def update(self, id, infopedido):
        pedidoActual = Pedido(self.repositorioPedido.findById(id))
        pedidoActual.fecha = infopedido["fecha"]
        pedidoActual.estado = infopedido["estado"]
        pedidoActual.observaciones = infopedido["observaciones"]
        return self.repositorioPedido.save(pedidoActual)

    def delete(self, id):
        return self.repositorioPedido.delete(id)

    """
       Relación Empleado - Pedido
       
    """

    def asignarEmpleado(self, id, id_empleado):
        pedidiActual = Pedido(self.repositorioPedido.findById(id))
        empleadoActual = Empleado(self.repositorioEmpleado.findById(id_empleado))
        pedidiActual.empleado = empleadoActual
        return self.repositorioPedido.save(pedidiActual)
