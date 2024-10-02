import tkinter as tk
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Conexion a la BD de Mongo
uri = 'mongodb+srv://Raul2998:tDmu2DLH8r0gkswN@dsc.cdzybzt.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['FLETES']
CLIENTES = db['CLIENTES']
CONDUCTOR = db['CONDUCTOR']
ENVIO = db['ENVIO']
FACTURA = db['FACTURA']
OPINION = db['OPINION']
SEGUIMIENTO = db['SEGUIMIENTO']
TARIFA = db['TARIFA']
TRANSPORTE = db['TRANSPORTE']

class Chofer:
    def __init__(self, nombre, apellido, licencia, telefono,  disponibilidad=True):
        self.nombre = nombre
        self.apellido = apellido
        self.licencia = licencia
        self.telefono = telefono
        self.disponibilidad = disponibilidad

    def actualizar_disponibilidad(self):
        self.disponibilidad = not self.disponibilidad

class Vehiculo:
    def __init__(self, marca, modelo, placa, disponibilidad=True):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.disponibilidad = disponibilidad

    def actualizar_disponibilidad(self):
        self.disponibilidad = not self.disponibilidad

class Ruta:
    def __init__(self, destino, distancia, origen, tiempo):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.tiempo = tiempo

# Crear función para mostrar ventana del menú principal
def menu_principal():
    # Crear ventana principal
    ventana_principal = tk.Toplevel()
    ventana_principal.title("Menú Principal")

    # Crear etiqueta para el título
    titulo = tk.Label(ventana_principal, text="Menú Principal")
    titulo.pack()

    # Crear botones para cada opción del menú
    boton_agregar_conductor = tk.Button(ventana_principal, text="Agregar Conductor", command=ventana_agregar_conductor)
    boton_agregar_conductor.pack()

    boton_agregar_cliente = tk.Button(ventana_principal, text="Agregar Cliente", command=ventana_agregar_cliente)
    boton_agregar_cliente.pack()

    boton_agregar_vehiculo = tk.Button(ventana_principal, text="Agregar Transporte", command=ventana_agregar_transporte)
    boton_agregar_vehiculo.pack()

    boton_agregar_envio = tk.Button(ventana_principal, text="Agregar Envio", command=ventana_agregar_envio)
    boton_agregar_envio.pack()
    
    boton_agregar_seguimiento = tk.Button(ventana_principal, text="Agregar Seguimiento", command=ventana_agregar_seguimiento)
    boton_agregar_seguimiento.pack()

    boton_agregar_factura = tk.Button(ventana_principal, text="Agregar Factura", command=ventana_agregar_factura)
    boton_agregar_factura.pack()

    boton_agregar_opinion = tk.Button(ventana_principal, text="Agregar Opinion", command=ventana_agregar_opinion)
    boton_agregar_opinion.pack()

    boton_agregar_tarifa = tk.Button(ventana_principal, text="Agregar Tarifa", command=ventana_agregar_tarifa)
    boton_agregar_tarifa.pack()
    
    boton_mostrar_chofer = tk.Button(ventana_principal, text="Mostrar Chofer", command=mostrar_choferes)
    boton_mostrar_chofer.pack()
    
    boton_mostrar_vehiculo = tk.Button(ventana_principal, text="Mostrar Vehiculo", command=mostrar_vehiculos)
    boton_mostrar_vehiculo.pack()
    
    # Crear botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana_principal, text="Cerrar", command=ventana_principal.destroy)
    boton_cerrar.pack()
    
    ventana_principal.mainloop()
 
# Crear funcion para agregar un transporte
def ventana_agregar_transporte():
    # Crear ventana para agregar transporte
        ventana_transporte = tk.Toplevel()
        ventana_transporte.title("Agregar Vehiculo")


        # Crear etiquetas y entradas de texto para ingresar los datos del transporte
        etiqueta_marca = tk.Label(ventana_transporte, text="Marca:")
        etiqueta_marca.pack()
        entrada_marca = tk.Entry(ventana_transporte)
        entrada_marca.pack()

        etiqueta_modelo = tk.Label(ventana_transporte, text="Modelo:")
        etiqueta_modelo.pack()
        entrada_modelo = tk.Entry(ventana_transporte)
        entrada_modelo.pack()

        etiqueta_capacidad = tk.Label(ventana_transporte, text="Capacidad:")
        etiqueta_capacidad.pack()
        entrada_capacidad = tk.Entry(ventana_transporte)
        entrada_capacidad.pack()

        etiqueta_placas = tk.Label(ventana_transporte, text="Placas:")
        etiqueta_placas.pack()
        entrada_placas = tk.Entry(ventana_transporte)
        entrada_placas.pack()

        # Crear botón para agregar el transporte
        def agregar_vehiculo():
                marca = entrada_marca.get()
                modelo = entrada_modelo.get()
                capacidad = entrada_capacidad.get()
                placas = entrada_placas.get()
                
                # Se guarda el vehiculo en la DB
                trans = { "capacidad": capacidad, "marca": marca, 'modelo': modelo, 'placas': placas }
                TRANSPORTE.insert_one(trans)

                messagebox.showinfo("Vehiculo Agregado", "Se ha agregado el vehiculo exitosamente.")

                # Cerrar la ventana
                ventana_transporte.destroy()

        boton_agregar = tk.Button(ventana_transporte, text="Agregar", command=agregar_vehiculo)
        boton_agregar.pack()

        # Mostrar ventana para agregar transporte
        ventana_transporte.mainloop()

# Crear funcion para agregar un cliente
def ventana_agregar_cliente():
        
        # Crear ventana para agregar un cliente
        ventana_cliente = tk.Toplevel()
        ventana_cliente.title("Agregar Cliente")

        # Crear etiquetas y entradas de texto para ingresar los datos del cliente
        etiqueta_nombre = tk.Label(ventana_cliente, text="Nombre:")
        etiqueta_nombre.pack()
        entrada_nombre = tk.Entry(ventana_cliente)
        entrada_nombre.pack()

        etiqueta_direccion = tk.Label(ventana_cliente, text="Dirección:")
        etiqueta_direccion.pack()
        entrada_direccion = tk.Entry(ventana_cliente)
        entrada_direccion.pack()

        etiqueta_email = tk.Label(ventana_cliente, text="Email:")
        etiqueta_email.pack()
        entrada_email = tk.Entry(ventana_cliente)
        entrada_email.pack()

        etiqueta_tel = tk.Label(ventana_cliente, text="Telefono:")
        etiqueta_tel.pack()
        entrada_tel = tk.Entry(ventana_cliente)
        entrada_tel.pack()
        

        # Crear botón para agregar el cliente
        def agregar_cliente():
            nombre = entrada_nombre.get()
            email = entrada_email.get()
            direccion = entrada_direccion.get()
            telefono = entrada_tel.get()

            # Se guarda el cliente en la DB
            client = {"nombre": nombre, "direccion": direccion, 'email': email, 'telefono': telefono}
            res = CLIENTES.insert_one(client)

            # Se muestra el ulitmo ID agregado en un messagebox
            ultimo_id = res.inserted_id
            messagebox.showinfo("Su ID es: ", ultimo_id)

            messagebox.showinfo("Chofer Agregado", "Se ha agregado el chofer exitosamente")

            # Cerrar la ventana
            ventana_cliente.destroy()

        boton_agregar = tk.Button(ventana_cliente, text="Agregar", command=agregar_cliente)
        boton_agregar.pack()
        
        ventana_cliente.mainloop()

# Crear funcion para agregar un conductor
def ventana_agregar_conductor():
        
        # Crear ventana para agregar conductor
        ventana_conductor = tk.Toplevel()
        ventana_conductor.title("Agregar Conductor")

        # Crear etiquetas y entradas de texto para ingresar los datos del conductor
        etiqueta_nombre = tk.Label(ventana_conductor, text="Nombre:")
        etiqueta_nombre.pack()
        entrada_nombre = tk.Entry(ventana_conductor)
        entrada_nombre.pack()

        etiqueta_direccion = tk.Label(ventana_conductor, text="Dirección:")
        etiqueta_direccion.pack()
        entrada_direccion = tk.Entry(ventana_conductor)
        entrada_direccion.pack()

        etiqueta_email = tk.Label(ventana_conductor, text="Email:")
        etiqueta_email.pack()
        entrada_email = tk.Entry(ventana_conductor)
        entrada_email.pack()

        etiqueta_tel = tk.Label(ventana_conductor, text="Telefono:")
        etiqueta_tel.pack()
        entrada_tel = tk.Entry(ventana_conductor)
        entrada_tel.pack()

        etiqueta_lic = tk.Label(ventana_conductor, text="Licencia:")
        etiqueta_lic.pack()
        entrada_lic = tk.Entry(ventana_conductor)
        entrada_lic.pack()

        # Crear botón para agregar el conductor
        def agregar_conductor():
            nombre = entrada_nombre.get()
            email = entrada_email.get()
            direccion = entrada_direccion.get()
            telefono = entrada_tel.get()
            licencia = entrada_lic.get()
            
            # Se guarda el chofer en la DB
            cond = { "nombre": nombre, "direccion": direccion, 'email': email, 'telefono': telefono, 'licencia': licencia }
            res = CONDUCTOR.insert_one(cond)
    
            # Se muestra el ulitmo ID agregado en un messagebox
            ultimo_id = res.inserted_id
            messagebox.showinfo("Su ID es: ", ultimo_id)

            messagebox.showinfo("Chofer Agregado", "Se ha agregado el chofer exitosamente.")

            # Cerrar la ventana
            ventana_conductor.destroy()

        boton_agregar = tk.Button(ventana_conductor, text="Agregar", command=agregar_conductor)
        boton_agregar.pack()

        ventana_conductor.mainloop()

# Crear funcion para agregar un envio
def ventana_agregar_envio():
        
    # Crear ventana para agregar chofer
    ventana_envio = tk.Toplevel()
    ventana_envio.title("Agregar Chofer")

    # Crear etiquetas y entradas de texto para ingresar los datos del chofer
    etiqueta_dir_origen = tk.Label(ventana_envio, text="Direccion de Origen:")
    etiqueta_dir_origen.pack()
    etiqueta_dir_origen = tk.Entry(ventana_envio)
    etiqueta_dir_origen.pack()

    etiqueta_dimensiones = tk.Label(ventana_envio, text="Dimensiones:")
    etiqueta_dimensiones.pack()
    etiqueta_dimensiones = tk.Entry(ventana_envio)
    etiqueta_dimensiones.pack()

    etiqueta_dir_final = tk.Label(ventana_envio, text="Direccion Final:")
    etiqueta_dir_final.pack()
    etiqueta_dir_final = tk.Entry(ventana_envio)
    etiqueta_dir_final.pack()

    etiqueta_num_seguimiento = tk.Label(ventana_envio, text="Numero de Seguimiento:")
    etiqueta_num_seguimiento.pack()
    etiqueta_num_seguimiento = tk.Entry(ventana_envio)
    etiqueta_num_seguimiento.pack()

    etiqueta_peso = tk.Label(ventana_envio, text="Peso:")
    etiqueta_peso.pack()
    etiqueta_peso = tk.Entry(ventana_envio)
    etiqueta_peso.pack()

    etiqueta_tipo_mercancia = tk.Label(ventana_envio, text="Tipo de Mercancia:")
    etiqueta_tipo_mercancia.pack()
    etiqueta_tipo_mercancia = tk.Entry(ventana_envio)
    etiqueta_tipo_mercancia.pack()

    etiqueta_cliente_id = tk.Label(ventana_envio, text="Cliente ID:")
    etiqueta_cliente_id.pack()
    etiqueta_cliente_id = tk.Entry(ventana_envio)
    etiqueta_cliente_id.pack()
        
    # Crear botón para agregar un envio
    def agregar_envio():
        dir_origen = etiqueta_dir_origen.get()
        dimensiones = etiqueta_dimensiones.get()
        dir_final = etiqueta_dir_final.get()
        num_seguimiento = etiqueta_num_seguimiento.get()
        peso = etiqueta_peso.get()
        tipo_mercancia = etiqueta_tipo_mercancia.get()
        cliente_id = etiqueta_cliente_id.get()
            
        # Se guarda el envio en la DB
        env = { "dir_origen": dir_origen, "dir_final": dir_final, 'dimensiones': dimensiones, 'num_seguimiento': num_seguimiento, 'peso': peso, 'tipo_mercancia': tipo_mercancia, 'cliente_id': cliente_id }
        res = ENVIO.insert_one(env)
    
        # Se muestra el ulitmo ID agregado en un messagebox
        ultimo_id = res.inserted_id
        messagebox.showinfo("Su ID es: ", ultimo_id)

        messagebox.showinfo("Envio Agregado", "Se ha agregado el envio exitosamente.")

    # Cerrar la ventana
    ventana_envio.destroy()

    boton_agregar_envio = tk.Button(ventana_envio, text="Agregar envio", command=agregar_envio)
    boton_agregar_envio.pack()

    ventana_envio.mainloop()

# Crear funcion para agregar un seguimiento
def ventana_agregar_seguimiento():
    # Crear ventana para agregar un seguimiento
    ventana_agregar_seguimiento = tk.Toplevel()
    ventana_agregar_seguimiento.title("Agregar Seguimiento")

     # Crear campos de entrada de datos
    etiqueta_origen = tk.Label(ventana_agregar_seguimiento, text="Origen:")
    etiqueta_origen.pack()

    etiqueta_origen = tk.Entry(ventana_agregar_seguimiento)
    etiqueta_origen.pack()

    etiqueta_destino = tk.Label(ventana_agregar_seguimiento, text="Destino:")
    etiqueta_destino.pack()

    etiqueta_destino = tk.Entry(ventana_agregar_seguimiento)
    etiqueta_destino.pack()

    etiqueta_distancia = tk.Label(ventana_agregar_seguimiento, text="Distancia:")
    etiqueta_distancia.pack()

    etiqueta_distancia = tk.Entry(ventana_agregar_seguimiento)
    etiqueta_distancia.pack()

    etiqueta_tiempo = tk.Label(ventana_agregar_seguimiento, text="Tiempo:")
    etiqueta_tiempo.pack()

    etiqueta_tiempo = tk.Entry(ventana_agregar_seguimiento)
    etiqueta_tiempo.pack()

     # Crear función para agregar un seguimiento
    def agregar_seguimiento():

        # Obtener los valores ingresados por el usuario
        destino = etiqueta_destino.get()
        origen = etiqueta_origen.get()
        distancia = etiqueta_distancia.get()
        tiempo = etiqueta_tiempo.get()
        
        # Se guarda el seguimiento en la DB
        seg = { "destino": destino, "distancia": distancia, 'origen': origen, 'tiempo': tiempo }
        SEGUIMIENTO.insert_one(seg)

        # Mostrar mensaje de éxito y cerrar la ventana
        messagebox.showinfo("Ruta Agregada", "Se ha agregado el seguimiento exitosamente.")
        ventana_agregar_seguimiento.destroy()

    # Crear botón para agregar el seguimiento
    boton_agregar_ruta = tk.Button(ventana_agregar_seguimiento, text="Agregar Seguimiento", command=agregar_seguimiento)
    boton_agregar_ruta.pack()

# Crear funcion para agregar una factura
def ventana_agregar_factura():
    # Crear ventana para agregar una factura
    ventana_agregar_factura = tk.Toplevel()
    ventana_agregar_factura.title("Agregar Factura")

     # Crear campos de entrada de datos
    etiqueta_importe = tk.Label(ventana_agregar_factura, text="Importe:")
    etiqueta_importe.pack()
    etiqueta_importe = tk.Entry(ventana_agregar_factura)
    etiqueta_importe.pack()

    etiqueta_estado_pago = tk.Label(ventana_agregar_factura, text="Estado Pago:")
    etiqueta_estado_pago.pack()
    etiqueta_estado_pago = tk.Entry(ventana_agregar_factura)
    etiqueta_estado_pago.pack()

    etiqueta_fecha_emision = tk.Label(ventana_agregar_factura, text="Fecha Emision:")
    etiqueta_fecha_emision.pack()
    etiqueta_fecha_emision = tk.Entry(ventana_agregar_factura)
    etiqueta_fecha_emision.pack()

    etiqueta_envio_id = tk.Label(ventana_agregar_factura, text="Envio ID:")
    etiqueta_envio_id.pack()
    etiqueta_envio_id = tk.Entry(ventana_agregar_factura)
    etiqueta_envio_id.pack()

    etiqueta_cliente_id = tk.Label(ventana_agregar_factura, text="Cliente ID:")
    etiqueta_cliente_id.pack()
    etiqueta_cliente_id = tk.Entry(ventana_agregar_factura)
    etiqueta_cliente_id.pack()

     # Crear función para agregar una factura
    def agregar_factura():

        # Obtener los valores ingresados por el usuario
        estado_pago = etiqueta_estado_pago.get()
        importe = etiqueta_importe.get()
        cliente_id = etiqueta_cliente_id.get()
        envio_id = etiqueta_envio_id.get()
        fecha_emision = etiqueta_fecha_emision.get()
        
        # Se guarda el seguimiento en la DB
        fact = { "estado_pago": estado_pago, "importe": importe, 'cliente_id': cliente_id, 'envio_id': envio_id, 'fecha_emision': fecha_emision}
        FACTURA.insert_one(fact)

        # Mostrar mensaje de éxito y cerrar la ventana
        messagebox.showinfo("Factura Agregada", "Se ha agregado la factura exitosamente.")
        ventana_agregar_factura.destroy()

    # Crear botón para agregar la factura
    boton_agregar_factura = tk.Button(ventana_agregar_factura, text="Agregar factura", command=agregar_factura)
    boton_agregar_factura.pack()

# Crear funcion para agregar una opinion
def ventana_agregar_opinion():
    # Crear ventana para agregar una opinion
    ventana_agregar_opinion = tk.Toplevel()
    ventana_agregar_opinion.title("Agregar Opinion")

    # Crear campos de entrada de datos
    etiqueta_calificacion = tk.Label(ventana_agregar_opinion, text="Calificacion:")
    etiqueta_calificacion.pack()
    etiqueta_calificacion = tk.Entry(ventana_agregar_opinion)
    etiqueta_calificacion.pack()

    etiqueta_comentarios = tk.Label(ventana_agregar_opinion, text="Comentarios:")
    etiqueta_comentarios.pack()
    etiqueta_comentarios = tk.Entry(ventana_agregar_opinion)
    etiqueta_comentarios.pack()

    etiqueta_fecha = tk.Label(ventana_agregar_opinion, text="Fecha:")
    etiqueta_fecha.pack()
    etiqueta_fecha = tk.Entry(ventana_agregar_opinion)
    etiqueta_fecha.pack()

    etiqueta_envio_id = tk.Label(ventana_agregar_opinion, text="Envio ID:")
    etiqueta_envio_id.pack()
    etiqueta_envio_id = tk.Entry(ventana_agregar_opinion)
    etiqueta_envio_id.pack()

    etiqueta_cliente_id = tk.Label(ventana_agregar_opinion, text="Cliente ID:")
    etiqueta_cliente_id.pack()
    etiqueta_cliente_id = tk.Entry(ventana_agregar_opinion)
    etiqueta_cliente_id.pack()

    # Crear función para agregar una opinion
    def agregar_opinion():

        # Obtener los valores ingresados por el usuario
        calificacion = etiqueta_calificacion.get()
        comentarios = etiqueta_comentarios.get()
        fecha = etiqueta_fecha.get()
        envio_id = etiqueta_envio_id.get()
        cliente_id = etiqueta_cliente_id.get()
        fecha = etiqueta_fecha.get()
        
        # Se guarda el seguimiento en la DB
        op = { "calificacion": calificacion, "comentarios": comentarios, 'fecha': fecha, 'envio_id': envio_id, 'cliente_id': cliente_id, 'fecha': fecha}
        OPINION.insert_one(op)

        # Mostrar mensaje de éxito y cerrar la ventana
        messagebox.showinfo("Opinion Agregada", "Se ha agregado la opinion exitosamente.")
        ventana_agregar_opinion.destroy()

    # Crear botón para agregar la opinion
    boton_agregar_opinion = tk.Button(ventana_agregar_opinion, text="Agregar Opinion", command=agregar_opinion)
    boton_agregar_opinion.pack()

# Crear funcion para agregar una tarifa
def ventana_agregar_tarifa():
    # Crear ventana para agregar una tarifa
    ventana_agregar_tarifa = tk.Toplevel()
    ventana_agregar_tarifa.title("Agregar Tarifa")

    # Crear campos de entrada de datos
    etiqueta_precio = tk.Label(ventana_agregar_tarifa, text="Precio:")
    etiqueta_precio.pack()
    etiqueta_precio = tk.Entry(ventana_agregar_tarifa)
    etiqueta_precio.pack()

    etiqueta_tipo_vehiculo = tk.Label(ventana_agregar_tarifa, text="Tipo Vehiculo:")
    etiqueta_tipo_vehiculo.pack()
    etiqueta_tipo_vehiculo = tk.Entry(ventana_agregar_tarifa)
    etiqueta_tipo_vehiculo.pack()

    etiqueta_carga = tk.Label(ventana_agregar_tarifa, text="Carga:")
    etiqueta_carga.pack()
    etiqueta_carga = tk.Entry(ventana_agregar_tarifa)
    etiqueta_carga.pack()

    etiqueta_tipo_mercancia = tk.Label(ventana_agregar_tarifa, text="Tipo Mercancia:")
    etiqueta_tipo_mercancia.pack()
    etiqueta_tipo_mercancia = tk.Entry(ventana_agregar_tarifa)
    etiqueta_tipo_mercancia.pack()

    # Crear función para agregar una tarifa
    def agregar_tarifa():

        # Obtener los valores ingresados por el usuario
        precio = etiqueta_precio.get()
        tipo_vehiculo = etiqueta_tipo_vehiculo.get()
        carga = etiqueta_carga.get()
        tipo_mercancia = etiqueta_tipo_mercancia.get()
           
        # Se guarda el seguimiento en la DB
        tar = { "precio": precio, "tipo_vehiculo": tipo_vehiculo, 'carga': carga, 'tipo_mercancia': tipo_mercancia}
        TARIFA.insert_one(tar)

        # Mostrar mensaje de éxito y cerrar la ventana
        messagebox.showinfo("Tarifa Agregada", "Se ha agregado la tarifa exitosamente.")
        ventana_agregar_tarifa.destroy()

    # Crear botón para agregar la tarifa
    boton_agregar_tarifa = tk.Button(ventana_agregar_tarifa, text="Agregar Tarifa", command=agregar_tarifa)
    boton_agregar_tarifa.pack()

# Crear funcion para mostrar un chofer
def mostrar_choferes():
    # Leer la información de los choferes desde el archivo

    
    # Crear la ventana para mostrar la información de los choferes
    ventana_choferes = tk.Toplevel()
    ventana_choferes.title("Choferes")

    # Crear un widget para mostrar la información de los choferes
    texto_choferes = tk.Text(ventana_choferes)
    texto_choferes.pack()
 
    # Agregar la información de los choferes al widget de texto
    resultados = CONDUCTOR.find()
    for indice, documento in enumerate(resultados):
        #ID = documento['_id']
        texto_choferes.insert(tk.END, f"Documento: {indice + 1}: {documento}\n")

    # Deshabilitar la edición del widget de texto
    texto_choferes.config(state=tk.DISABLED)
    
# Crear funcion para mostrar un vehiculo
def mostrar_vehiculos():
    # Leer la información de los choferes desde el archivo
    with open("vehiculos.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    # Crear la ventana para mostrar la información de los choferes
    ventana_vehiculos = tk.Toplevel()
    ventana_vehiculos.title("Vehiculos")

    # Crear un widget para mostrar la información de los choferes
    texto_vehiculos = tk.Text(ventana_vehiculos)
    texto_vehiculos.pack()

    # Agregar la información de los choferes al widget de texto
    for linea in lineas:
        chofer = linea.strip().split(",")
        texto_vehiculos.insert(tk.END, f"Vehiculo: {chofer[0]}\n")
        texto_vehiculos.insert(tk.END, f"Modelo: {chofer[1]}\n")
        texto_vehiculos.insert(tk.END, f"Placas: {chofer[2]}\n")
        texto_vehiculos.insert(tk.END, "\n")

    # Deshabilitar la edición del widget de texto
    texto_vehiculos.config(state=tk.DISABLED)

# Crear función para verificar las credenciales de usuario
def verificar_credenciales(usuario, contraseña):
    with open("usuarios.txt", "r") as archivo:
        credenciales = archivo.read().splitlines()

    if f"{usuario}:{contraseña}" in credenciales:
        print("Inicio de sesión exitoso.")
        # Crea y muestra la ventana del menú principal
        menu_principal()
    else:
        print("Credenciales incorrectas.")

# Creación de la ventana de bienvenida
ventana = tk.Tk()

etiqueta1 = tk.Label(ventana, text="Bienvenido a la aplicación de trailers")
etiqueta1.pack()

etiqueta2 = tk.Label(ventana, text="Ingrese sus credenciales:")
etiqueta2.pack()

entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.pack()

boton = tk.Button(ventana, text="Iniciar sesión", command=lambda: verificar_credenciales(entrada_usuario.get(), entrada_contraseña.get()))
boton.pack()

ventana.mainloop()
