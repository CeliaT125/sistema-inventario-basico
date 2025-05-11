#Definimos la clase producto
class Producto:
    #Añadimos los atributos privados con el constructor
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    #Añadimos los getters y setters
    def get_nombre(self):
        return self.__nombre
    
    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad     

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio  

    def set_cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    #Mostramos los detalles del producto
    def __str__(self):
        return f"Producto: {self.__nombre}, categoria: {self.__categoria}, precio: {self.__precio} €, cantidad: {self.__cantidad}"
    
#Definimos la clase inventario
class Inventario:
    #Creamos una lista vacia donde se agregarán los productos que introduzca el usuario
    def __init__(self):
        self.__productos = []

    #Creamos un método para agregar productos al inventario, donde se añade cada producto introducido a la lista
    def agregar_producto(self, producto):
        self.__productos.append(producto)
        #Indicamos al usuario que hemos agregado el nuevo producto al inventario
        print("El producto se ha agregado al inventario.")

    #Creamos método para pedir al usuario los datos del nuevo producto
    def pedir_datos(self):
        #Solicitamos nombre del producto en minusculas y sin espacios
        while True:
            nombre = input("Introduce el nombre del nuevo producto: ").strip().lower()
            #Revisamos que el nombre no esté vacio
            if not nombre:
                print("No debe estar vacío. Pruebe de nuevo.")
                continue
            #Miramos si hay otro producto con el mismo nombre, si es así pedimos uno nuevo
            if any(producto.get_nombre() == nombre for producto in self.__productos):
                print("Nombre en uso. Introduce un nuevo nombre.")
                continue
            break

        #Solicitamos al usuario la categoria, sin espacios y en minusculas            
        while True:
            categoria = input("Introduce la categoría del nuevo producto: ").strip().lower()
            #Nos aseguramos que no esté vacio
            if not categoria: 
                print("No debe estar vacío. Pruebe de nuevo.") 
                continue
            break
                     
        #Solicitamos el precio del producto, comprobando que el usuario introduce un número válido
        while True:
            try:
                precio = float(input("Introduce el precio: "))
                #Comprobamos que el número sea mayor que cero
                if precio > 0:
                    break
                else:
                    print("Introduce un precio correcto, debe ser un número positivo. Prueba de nuevo.")
            #Comprobamos que haya introducido un número y no otro caracter
            except ValueError:
                print("Introduce un precio correcto, debe ser un número positivo. Prueba de nuevo.")

        #Solicitamos la cantidad del nuevo producto, comprobando que el usuario introduce un número válido
        while True:
            try:
                cantidad = int(input("Introduce la cantidad: "))
                if cantidad >= 0:
                    break
                else:
                    print("Introduce una cantidad correcta, debe ser un número igual o mayor a cero. Prueba de nuevo.")
            except ValueError:
                print("Introduce una cantidad correcta, debe ser un número igual o mayor a cero. Prueba de nuevo.")

        #Creamos el producto con sus atributos mediante los datos recogidos por el usuario
        return Producto(nombre, categoria, precio, cantidad)

    #Creamos un método para mostrar la lista de productos que haya en el inventario
    def mostrar_inventario(self):
        #Primero comprobamos si hay productos en el inventario
        if not self.__productos:
            print("No hay productos en el inventario.")

        #Buscamos los productos que haya en el inventario y los muestra por pantalla
        else:
            for producto in self.__productos:
                print(producto)

    #Creamos un método para buscar un producto dentro del inventario
    def buscar_producto(self, nombre):
        #Recorremos la lista de productos en el inventario para comprobar que haya un producto con el mismo nombre
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        return None
    
    #Creamos un método para mostrar el producto que hayamos buscado
    def mostrar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    #Creamos un método para ver si el producto que se desea actualizar o eliminar está en el inventario
    def identificar_producto(self, nombre):
        while True: 
            #Recorremos la lista de productos del inventario para ver si alguno coincide con el nombre introducido por el usuario
            #Si hay coincidencia, con next conseguimos añadirlo a producto_encontrado. Si no hay coincidencia producto_encontrado estaría vacio
            producto_encontrado = next((producto for producto in self.__productos if producto.get_nombre() == nombre), None)

            #Si se encuentra el producto, se almacena para poder modificar el precio/cantidad o para eliminarlo
            if producto_encontrado:
                print(f'Producto encontrado: {producto_encontrado.get_nombre()}')
                return producto_encontrado
            
            else:
                print(f'El producto no se encuentra en el inventario.')
                return
            
    #Creamos un método para actualizar el precio y/o la cantidad
    def actualizar_precio_y_cantidad(self, nombre):
        #Miramos si el producto está en el inventario gracias al método anterior identificar_producto
        producto = self.identificar_producto(nombre)

        #Si no está, indicamos al usuario que no se ha actualizado nada
        if not producto:
            print("No se ha podido actualizar ningún producto. Volviendo al menú principal")
            return
        
        #Actualizamos precio si el producto está en el inventario
        while True:
            try:
                #Solicitamos nuevo precio, asegurando que introduce un precio correcto
                nuevo_precio = float(input(f'Si no desea actualizar, indique el precio actual ({producto.get_precio()}€). Introduce el nuevo precio: '))
                if nuevo_precio > 0:
                    #Actualizamos precio con setter
                    producto.set_precio(nuevo_precio)
                    print(f'Precio actualizado a: {nuevo_precio} €')
                    break
                else:
                    print("El nuevo precio debe ser un numero positivo. Prueba de nuevo")
            except ValueError:
                print("El nuevo precio debe ser un numero positivo. Prueba de nuevo")
        
        #Actualizamos cantidad si el producto está en el inventario
        while True:
            try:
                #Solicitamos nueva cantidad, asegurando que introduce un número correcto
                nueva_cantidad = int(input(f'Si no desea actualizar, indique la cantidad actual ({producto.get_cantidad()} unidades). Introduce la nueva cantidad: '))
                if nueva_cantidad >= 0:
                    #Actualizamos cantidad con setter
                    producto.set_cantidad(nueva_cantidad)
                    print(f'Cantidad actualizada a: {nueva_cantidad} unidades.')
                    break
                else:
                    print("La nueva cantidad no puede ser negativa. Prueba de nuevo")
            except ValueError:
                print("La nueva cantidad debe ser un numero igual o mayor a cero. Prueba de nuevo")

        print(f'El producto se ha actualizado correctamente.')

    #Creamos método para eliminar un producto del inventario
    def eliminar_producto(self, nombre):
        #Miramos si el producto está en el inventario gracias al método identificar_producto
        producto = self.identificar_producto(nombre)

        #Si está el producto, lo eliminamos
        if producto: 
            self.__productos.remove(producto)
            print("Producto eliminado correctamente. ")

        #Si no está, indicamos al usuario que no se ha eliminado nada    
        else:
            print("No se ha podido eliminar ningún producto. Volviendo al menú principal")


# Creamos el menú principal de la aplicación
def menu():
    inventario = Inventario()

#Creamos un bucle infinito para que el menú aparezca siempre al usuario
    while True:
        print("""
--MENU DEL INVENTARIO--
              
  1. Agregar producto
  2. Actualizar producto
  3. Eliminar producto
  4. Mostrar inventario
  5. Buscar producto
  6. Salir""")
        
        #Preguntamos al usuario que opcion quiere elegir
        eleccion = (input("""
Elija que opcion desea realizar: """))

        if eleccion == "1":
            #Llamamos al metodo pedir_datos para que el usuario intruzca los datos del nuevo producto      
            nuevo_producto = inventario.pedir_datos()

            #Llamamos al metodo agregar_producto para añadir el nuevo producto al inventario
            inventario.agregar_producto(nuevo_producto)

        elif eleccion == "2":
            #Pedimos al ussuario que escriba el nombre del producto que quiere actualizar en minusculas, sin espacios y nunca vacio
            nombre = input("Introduce el nombre del producto que desea actualizar: ").strip().lower()
            while len(nombre) == 0:
                nombre = input("Introduce el nombre del producto a actualizar (no debe estar vacio): ").strip().lower()

            #Llamamos al metodo actualizar_precio_y_cantidad para poder actualizar el producto
            inventario.actualizar_precio_y_cantidad(nombre)
    
        elif eleccion == "3":
            #Pedimos al ussuario que indique el nombre del producto a eliminar, en minusculas, sin espacios y nunca vacio
            nombre = input("Introduce el nombre del producto que desea eliminar: ").strip().lower()
            while len(nombre) == 0:
                nombre = input("Introduce el nombre del producto (no debe estar vacio): ").strip().lower()

            #Llamamos al método eliminar_producto para poder eliminar el producto 
            inventario.eliminar_producto(nombre)
            
        elif eleccion == "4":
            #Llamamos al método mostrar_inventario para imprimir por pantalla la lista de productos del inventario
            inventario.mostrar_inventario()

        elif eleccion == "5":
            #Pedimos al ussuario que escriba el nombre del producto a buscar, nunca vacio y en minusculas
            nombre = input("Introduce el nombre del producto que desea buscar: ").strip().lower()
            while len(nombre) == 0:
                nombre = input("Introduce el nombre del producto (no debe estar vacio): ").strip().lower()
                
            #Llamamos al método mostrar_producto para que lo muestre, además este método ha llamado al método buscar_producto
            inventario.mostrar_producto(nombre)
            
        elif eleccion == "6":
            #Indicamos al ususario que ha salido del programa
            print("Ha salido fuera del programa.")
            break
        
        #Nos aseguramos que introduce una opción válida
        else:
            print("No has seleccionado una opción disponible, elija un número entre 1 y 6")
menu()




