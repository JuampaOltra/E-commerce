

class Carro():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}
        #else:
        self.carro = carro


    def agregar_articulo(self, articulo):
        if str(articulo.id) not in self.carro.keys():
            self.carro[articulo.id]={
                'articulo_id':articulo.id,
                'nombre':articulo.nombre,
                'stock':articulo.stock,
                'ventas':articulo.num_ventas,
                'precio':str(articulo.precio),
                'cantidad':1,
                #'imagen':articulo.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(articulo.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + float(articulo.precio)
                    break

        self.guardar_carro()

    def guardar_carro(self):
        self.session ["carro"] = self.carro
        self.session.modified = True

    def eliminar_articulo(self, articulo):
        articulo.id = str(articulo.id)
        if articulo.id in self.carro:
            del self.carro[articulo.id]
            self.guardar_carro()


    def restar_articulo(self, articulo):
        for key, value in self.carro.items():
            if key == str(articulo.id):
                value['cantidad'] = value['cantidad'] - 1
                value["precio"] = float(value["precio"]) - float(articulo.precio)
                if value['cantidad'] < 1:
                    self.eliminar_articulo(articulo)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True


