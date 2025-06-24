import json
import os
from typing import Dict
from models import Cliente, Factura
from validators import Validador

class CRMSystem:
    '''
    Sistema principal de gestion de clientes
    '''
    
    def __init__(self):
        '''
        Inicia el sistema
        '''
        
        self.clientes: Dict[str, Cliente] = {}
        self.facturas: Dict[str, Factura] = {}
        self.contador_clientes = 1
        self.contador_facturas = 1
        self.archivos_clientes = "clientes.json"
        self.archivos_facturas = "facturas.json"
        self.cargar_datos()
        
    
    def cargar_datos(self):
        '''
        Carga los datos de los json si existen
        '''
        
        try: 
            
            #Carga los clientes
            if os.path.exists(self.archivos_clientes):
                with open(self.archivos_clientes, 'r' , encoding='utf-8') as f:
                    datos = json.load(f)
                    for id_cliente , data in datos.items():
                        self.clientes[id_cliente] = Cliente.from_dict(data)
                        
                        
                    #Actualiza el contador   
                    if self.clientes:
                        max_num = max([int(id_u[3:]) for id_u in self.clientes.keys()])
                        self.contador_clientes = max_num + 1
                    
                    
            #Carga facturas
            
            if os.path.exists(self.archovos_facturas):
                with open(self.archivos_facturas, 'r', encoding='utf-8') as f: 
                    datos = json.load(f)
                    for num_factura, data in datos.items():
                        self.facturas[num_factura] = Factura.from_dict(data)
                     
                    #Actualizamos contador    
                    if self.facturas:
                        max_num = max([int(nf[3:]) for nf in self.facturas.keys()])
                        self.contador_facturas = max_num + 1 
                        
        
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            
    
    
    def guardar_datos(self):
        '''
        Guardamos los archivos JSON
        '''
        
        try: 
            #Guardamos clientes
            with open(self.archivos_clientes , 'w' , encoding='utf-8') as f:
                datos = {id_u: cliente.to_dict() for id_u, cliente in self.clientes.items()}
                json.dump(datos, f, indent=2, ensure_ascii=False)
                
            #Guardamos facturas
            with open(self.archivos_facturas, 'w' , encoding='utf-8') as f:
                datos = {num_f: factura.to_dict() for num_f, factura in self.facturas.items()}
                json.dump(datos, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
    
    
    def generar_id_cliente(self) -> str:
        '''
        Genera la ID del cliente
        '''
        id_cliente = f"USR{self.contador_clientes:03d}"
        self.contador_clientes += 1
        return id_cliente
    
    def generar_numero_factura(self) -> str:
        '''
        Genera el nº de factura
        '''
        num_factura = f"FAC{self.contador_facturas:03d}"
        self.contador_facturas += 1
        return num_factura
    
    def email_existe(self, email: str, excluir_id: str = None) -> bool:
        '''
        Verifica si el email existe ya
    
        Args: 
        email :  email a revisar
        exluir_id : id de usuario a excluir de la verificacion
        
        returns:
        true si el email existe, false si no
        '''
        
        for id_cliente , cliente in self.clientes.items():
            if id_cliente != excluir_id and cliente.email.lower() == email.lower():
                return True
            return False
        
    
    def registrar_cliente(self):
        '''
        Opcion 1 : registrar cliente
        '''
        print("\n ===== REGISTRO DE CLIENTE =====")
        
        try:
            
            #Validamos nombre
            
            nombre = input("Ingrese su nombre: ").strip()
            if not Validador.validar_campo_obligatorio(nombre,"Ingrese nombre"):
                return
            
            #Validamos apellidos
            
            apellidos = input("Ingrese apellidos: ".strip())
            if not Validador.validar_campo_obligatorio(apellidos,"Ingrese apellidos"):
                return
            
            
            #Validamos email
            
            while True:
                email = input("Ingrese email: ").strip()
                if not Validador.validar_campo_obligatorio(email,"Ingrese email"):
                    return
                
                if not  Validador.validar_email(email):
                    print("Error: email no valido")
                    return
                
                if self.email_existe(email):
                    print("Error: el email ya existe")
                    continue
                
                
                break
            
            
            #Solicitamos datos adicionales
            
            telefono = input("Ingrese telefono(opcional): ").strip()
            direccion = input("Ingrese direccion(opcional): ").strip()
            
            #Creamos cliente 
            
            cliente = Cliente(nombre,apellidos,email,telefono,direccion)
            id_cliente = self.generar_id_cliente()
            cliente.id_cliente = id_cliente 
            
            #Guardamos cliente
            
            self.cliente[id_cliente] = cliente
            self.guardar_datos()
            
            print("\nClientere registrado correctametne")
            print(f"ID asignado:{id_cliente}")
            print(f"Fecha de registro:{cliente.fecha_registro}")
            
        except KeyboardInterrupt:
            print("\Registro cancelado")
            
        except Exception as e:
            print(f"Error en el registro del cliente: {e}")
            
            
    def buscar_cliente(self):
        '''
        Opcion 2: buscar cliente
        '''
        
        print("\n ===== BUSCAR CLIENTE =====")
        
        if not self.clientes:
            print("No hay clientes registrado")
            return
        
        try:
            print("1. Busca por email")
            print("2. Busca por nombre")
            
            while True:
                metodo = input("\nSelecciona un metodo de busqueda: ").strip()
                
                if metodo in ["1" , " 2"]:
                    break
                
                print("Opcion invalida: solo validas opcion 1 y 2")
                
            if metodo == "1":
                email = input("Ingresa email: ").strip()
                cliente_encontrado = None 
                
                for cliente in self.clientes.values():
                    if cliente.email.lower() == email.lower():
                        cliente_encontrado = cliente
                        break
                    
                if cliente_encontrado:
                    print("\n --- USUARIO ENCONTRADO ---")
                    self.mostrar_detalle_cliente(cliente_encontrado)
                
                else:
                    print("Cliente no encontrado")
                    
            elif metodo == "2":
                nombre = input("Ingresa nombre: ").strip().lower()
                clientes_encontrados = []
                
                
                for cliente in self.clientes.values():
                    if (nombre in cliente.nombre.lower() or
                        nombre in cliente.apellidos.lower() or
                        nombre in cliente.nombre_completo().lower()):
                       
                       clientes_encontrados.append(cliente)
                
                if clientes_encontrados:
                    print(f"\n --- USARIOS ENCONTRADOS ({len(clientes_encontrados)}) ---")
                    for cliente in clientes_encontrados:
                        self.mostrar_detalle_cliente(cliente)
                        print("-" * 50)
                        
                else: 
                    print("No se encontraron clientes con ese nombre")
                    
        except KeyboardInterrupt:
            print("\nBusqueda cancelada")
            
        except Exception as e:
            print(f"Error de busqueda: {e}")
            
    
    def crear_factura(self):
        '''
        Opcion 3: Crear factura para el cliente
        '''
        
        print("\n ===== CREAR FACTURA =====")
        
        if not self.clientes:
            print("No hay clientes registrados. Registra un cliente primero")
            return
        
        try:
            
            #Solicitamos email del cliente
            
            email = input("Ingresa email del cliente: ").strip()
            
            #Buscamos cliente por email
            
            cliente_encontrado = None
            
            for cliente in self.clientes.values():
                if cliente.email.lower() == email.lower():
                    cliente_encontrado = cliente
                    break
        
            if not cliente_encontrado:
                print("Cliente no encontrado")
                return
            
            
            print(f"\nCliente encontrado: {cliente_encontrado.nombre_completo()}")
            
            #Solicitamos descripcion
            
            descripcion = input("Introduce la descripcion del servicio o producto: ").strip()
            if not Validador.validar_campo_obligatorio(descripcion, "Introduce la descripcion"):
                return
            
            #Solicitamos monto
            
            while True:
                monto_str = input("Introduce el monto: ").strip()
                es_valido, monto = Validador.validar_monto(monto_str)
                if es_valido:
                    break
                print("Error: introduce un monto valido ( numero positivo )")
                
                
            
            #Solicitamos estado
            
            print("Selecciona estado de factura:")
            print("1. Pendiente")
            print("2. Pagada")
            print("3. Cancelada")
            
            while True:
                estado_opcion = input("Estado: ").strip()
                if estado_opcion == "1":
                    estado = "Pendiente"
                    break
                elif estado_opcion == "2":
                    estado = "Pagada"
                    break
                elif estado_opcion == "3":
                    estado = "Cancelada"
                    break
                
                else: 
                    print("Opcion invalida, introduce 1 , 2 o 3 ")
                    
                    
            #Creamos factura
            
            factura = Factura(cliente_encontrado.id_cliente,descripcion,monto)
            factura.estado = estado
            numero_factura = self.generar_numero_factura()
            factura.numero_factura = numero_factura
            
            #Guardamos factura
            
            self.facturas[numero_factura] = factura
            cliente_encontrado.facturas.append(numero_factura)
            self.guardar_datos()
            
            print("\nFactura creada correctamente")
            print(f"Numero de factura: {numero_factura}")
            print(f"Fecha emision: {factura.fecha_emision}")
            print(f"Cliente: {cliente_encontrado.nombre_completo()}")
            print(f"Descripcion: {descripcion}")
            print(f"Monto: {monto:.2f}")
            print(f"Estado: {estado}")
            
        except KeyboardInterrupt:
            print("Operacion cancelada")
            
        except Exception as e:
            print(f"Error al crear la factura: {e}")
    
    def mostrar_todos_clientes(self):
        '''
        Opcion 4: Mostrar todos los clientes
        '''
        
        print("\n ===== LISTA DE CLIENTES =====")
        
        if not self.clientes:
            print("No hay clientes registrados")
            return
        
        contador = 1 
        
        for cliente in self.clientes.values():
            print(f"\nCliente #{contador}:")
            print(f"ID: {cliente.id_cliente}")
            print(f"Nombre: {cliente.nombre_completo()}")
            print(f"Email: {cliente.email}")
            print(f"Telefono: {cliente.telefono}")
            print(f"Fecha de registro: {cliente.fecha_registro}")
            contador +=1
            
        print(f"\nTotal de clientes registrados: {len(self.clientes)}")
        
    
    def mostrar_facturas_cliente(self):
        '''
        Opcion 5: Mostrar factura de 1 cliente
        '''
        
        print("\n ===== MOSTRAR FACTURAS DEL CLIENTE =====")
        
        if not self.clientes:
            print("No hay clientes registrados")
            return

        
        try:
            #Mostramos lista de clientes
            
            print("\nClientes disponibles:")
            for cliente in self.clientes.values():
                print(f"ID: {cliente.id_cliente} - {cliente.nombre_completo()}")
                

            #Solicitamos ID del cliente
            
            id_cliente = input("\nIngrese el ID del cliente: ").strip().upper()
            
            if id_cliente not in self.clientes:
                print("Cliente no encontrado")
                return
            
            cliente = self.clientes[id_cliente]
            print(f"\n ===== FACTURAS DE  {cliente.nombre_completo().upper()} =====")
            
            if not cliente.facturas:
                print("Este cliente no tiene facturas")
                return
            
            #Mostramos facturas
            
            total_facturas = 0
            total_monto = 0 
            
            for numero_factura in cliente.facturas:
                if numero_factura in self.facturas:
                    factura = self.facturas[numero_factura]
                    print(f"\nFactura #{numero_factura}")
                    print(f"Fecha: {factura.fecha_emision}")
                    print(f"Descripcion: {factura.descripcion}")
                    print(f"Monto: {factura.monto:.2f} €")
                    print(f"Estado: {factura.estado}")
                    total_facturas += 1
                    total_monto += factura.monto
                    
            print(f"\nResumen:")
            print(f"Total facturas: {total_facturas}")
            print(f"Monto total: {total_monto:.2f} €")
            
        except KeyboardInterrupt:
            print("\nOperacion cancelada")
        except Exception as e:
            print(f"Error al mostrar facturas: {e}")
    
    def resumen_financiero(self):
        '''
        Opcion 6: Resumen financiero del cliente 
        '''
        
        print("\n ===== RESUMEN FINANCIERO =====")
        
        if not self.clientes:
            print("No hay clientes registrados")
            return

        total_clientes = 0 
        total_facturas_sistema = 0
        ingresos_totales = 0 
        ingresos_recibidos = 0
        ingresos_pendientes = 0
        
        for cliente in self.clientes.values():
            total_facturas_cliente = len(cliente.facturas)
            monto_total_cliente = 0
            facturas_pagadas_cliente = 0
            facturas_pendientes_cliente = 0
            
            #Calculamos totales por cliente
            
            for numero_factura in cliente.facturas:
                if numero_factura in self.facturas:
                    factura = self.facturas[numero_factura]
                    monto_total_cliente += factura.monto
                    
                    if factura.estado == "Pagada":
                        facturas_pagadas_cliente += factura.monto
                    
                    elif factura.estado == "Pendiente":
                        facturas_pendientes_cliente += factura.monto
            
            
            #Mostramos informacion del cliente
            
            print(f"\nCliente:  {cliente.nombre_completo()} ({cliente.email})")
            print(f"- TOTAL FACTURAS: {total_facturas_cliente}")
            print(f"- Monto total: {monto_total_cliente:.2f}€")
            print(f"- Facturas pagadas: {facturas_pagadas_cliente:.2f}")
            print(f"- Facturas pendientes: {facturas_pendientes_cliente:.2f}")
            
            #Acumulamos totales del sistema
            
            total_clientes += 1
            total_facturas_sistema += total_facturas_cliente
            ingresos_totales += monto_total_cliente
            ingresos_recibidos += facturas_pagadas_cliente
            ingresos_pendientes += facturas_pendientes_cliente
            
        
        #Mostrar resumen general
        
        print(f"\nn --- RESUMEN GENERAL --- ")
        print(f"Total clientes: {total_clientes}")
        print(f"Total facturas emitidas: {total_facturas_sistema}")
        print(f"Ingresos totales: {ingresos_totales:.2f} €")
        print(f"Ingresos pendientes: {ingresos_pendientes:.2f} €")
        print(f"Ingresos recibidos: {ingresos_recibidos:.2f} €")
        
    def mostrar_detalle_cliente(self, cliente: Cliente):
        '''
        Funcion auxiliar para mostrar informacion detallada de un cliente
        '''
        
        print(f"ID: {cliente.id_cliente}")
        print(f"Nombre: {cliente.nombre_completo()}")
        print(f"Email: {cliente.email}")
        print(f"Telefono: {cliente.telefono}")
        print(f"Direccion: {cliente.direccion}")
        print(f"Fecha de registro: {cliente.fecha_registro}")
        
    
    def mostrar_menu(self):
        '''
        Muestra el menu principal del sistema
        '''
        
        print("\n" + "=" *30)
        print("=== SISTEMA CRM ===")
        print("=" * 30)
        print("1. Registrar cliente")
        print("2. Buscar cliente")
        print("3. Crear factura al cliente")
        print("4. Mostrar todos los clientes")
        print("5. Mostrar facturas de un cliente")
        print("6. Resumen financiero por cliente")
        print("7. Salir")
        print("=" * 30)
        
    def ejecutar(self):
        '''
        Funcion para ejecutar el sistema CRM
        '''
        
        print("BIENVENIDO AL SISTEMA CRM")
        print("Sistema de gestion de relaciones con clientes")
        
        while True:
            
            try:
                
                self.mostrar_menu()
                opcion = input("Selecciona una opción: ").strip()
                
                if opcion == "1":
                    self.registrar_cliente()
                    
                elif opcion == "2":
                    self.buscar_cliente()
                    
                elif opcion == "3":
                    self.crear_factura()
                    
                elif opcion == "4":
                    self.mostrar_todos_clientes()
                    
                elif opcion == "5":
                    self.mostrar_facturas_cliente()
                    
                elif opcion == "6":
                    self.resumen_financiero()
                    
                elif opcion == "7":
                    print("\n GRACIAS POR USAS EL SISTEMA")
                    print("DATOS GUARDADOS CORRECTAMENTE")
                    break
                else:
                    print("Opcion no valida. Introduce una opcion del 1 al 7 ")
                    
                input("\nPresiona Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n SALIENDO DEL SISTEMA...")
                self.guardar_datos
                break
        
            except Exception as e :
                print(f"Error inesperado: {e}")
                input("Presiona Enter para continuar...")