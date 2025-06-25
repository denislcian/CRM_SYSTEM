from datetime import datetime
from typing import List


class Cliente:
    '''
    Clase para representar a un cliente del sistema
    '''
    
    def __init__(self, nombre: str, apellidos: str, email: str, telefono: str = "", direccion: str = ""):
        '''
        Inicia un nuevo cliente
        
        Args: 
        nombre : nombre del cliente
        apellidos : apellidos del cliente
        email : email del cliente ( debe ser unico )
        telefono : telefono del cliente ( opcional )
        direccion : direccion del cliente ( opcional )     
        '''
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono if telefono else "No especificado"
        self.direccion = direccion if direccion else "No especificado"
        self.id_cliente = None  # Se asigna automaticamente 
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y")
        self.facturas = []      # Lista de facturas asociadas 
        
    def nombre_completo(self) -> str:
        '''
        Muestra el nombre completo
        '''
        return f"{self.nombre} {self.apellidos}"
        
    def to_dict(self) -> dict:
        '''
        Convierte el cliente a diccionario JSON
        '''
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'email': self.email,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'fecha_registro': self.fecha_registro,
            'facturas': self.facturas
        }
            
    @classmethod
    def from_dict(cls, data: dict):
        '''
        Crea el cliente desde el diccionario
        '''
        
        cliente = cls(
            data['nombre'],  
            data['apellidos'],
            data['email'],
            data.get('telefono', ''),
            data.get('direccion', '')
        )
        
        cliente.id_cliente = data['id_cliente']
        cliente.fecha_registro = data.get('fecha_registro', cliente.fecha_registro)
        cliente.facturas = data.get('facturas', [])
        
        return cliente
    
    
class Factura: 
    '''
    Clase para representar la factura en el sistema 
    '''
    
    def __init__(self, id_cliente: str, descripcion: str, monto: float):
        '''
        Inicializa una nueva factura
    
        Args: 
        id_cliente: ID del cliente al que pertenece la factura
        descripcion: Descripcion del servicio o producto
        monto: Monto total de la factura
        '''
    
        self.id_cliente = id_cliente
        self.descripcion = descripcion
        self.monto = monto
        self.numero_factura = None  # Automatico por sistema
        self.fecha_emision = datetime.now().strftime("%d/%m/%Y") 
        self.estado = "Pendiente" 
    
    def to_dict(self) -> dict:
        '''
        Convierte la factura a diccionario JSON
        '''
        
        return {
            'numero_factura': self.numero_factura,
            'id_cliente': self.id_cliente,
            'descripcion': self.descripcion,
            'monto': self.monto,
            'fecha_emision': self.fecha_emision,
            'estado': self.estado
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        '''
        Crea la factura desde el diccionario
        '''
        
        factura = cls(
            data['id_cliente'],
            data['descripcion'],
            data['monto']
        )
        
        factura.numero_factura = data['numero_factura']
        factura.fecha_emision = data.get('fecha_emision', factura.fecha_emision)
        factura.estado = data.get('estado', 'Pendiente')
        
        return factura