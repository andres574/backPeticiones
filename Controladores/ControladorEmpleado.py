from Repositorios.RepositorioEmpleado import RepositorioEmpleado
from Modelos.Empleado import Empleado


class ControladorEmpleado():
    def __init__(self):
        self.repositorioEmpleado = RepositorioEmpleado()
    def index(self):
        return self.repositorioEmpleado.findAll()

    def create(self, infoempleado):
        nuevolEmpleado = Empleado(infoempleado)
        return self.repositorioEmpleado.save(nuevolEmpleado)

    def show(self, id):
        elEmpleado = Empleado(self.repositorioEmpleado.findById(id))
        return elEmpleado.__dict__

    def update(self, id, infoEmpleado):
        empleadoActual = Empleado(self.repositorioEmpleado.findById(id))
        empleadoActual.cedula = infoEmpleado["cedula"]
        empleadoActual.nombre = infoEmpleado["nombre"]
        empleadoActual.apellido = infoEmpleado["apellido"]
        return self.repositorioEmpleado.save(empleadoActual)

    def delete(self, id):
        return self.repositorioEmpleado.delete(id)
