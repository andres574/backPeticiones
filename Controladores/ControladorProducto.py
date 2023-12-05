from Repositorios.RepositorioProducto import RepositorioProducto
from Modelos.Producto import Producto

class ControladorProducto():
    def __init__(self):
        self.repositorioProducto = RepositorioProducto()

    def index(self):
        return self.repositorioProducto.findAll()

    def create(self, infoproducto):
        nuevoProducto = Producto(infoproducto)
        return self.repositorioProducto.save(nuevoProducto)

    def show(self, id):
        elProducto = Producto(self.repositorioProducto.findById(id))
        return elProducto.__dict__

    def update(self, id, infoproducto):
        productoActual= Producto(self.repositorioProducto.findById(id))
        productoActual.nombre = infoproducto["nombre"]
        productoActual.precio = infoproducto["precio"]
        productoActual.categoria = infoproducto["categoria"]
        return self.repositorioProducto.save(productoActual)

    def delete(self, id):
        return self.repositorioProducto.delete(id)