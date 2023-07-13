from controllers.AssuntoController import AssuntoController

try:
    AssuntoController().listar()
except Exception as exception:
    print(exception)