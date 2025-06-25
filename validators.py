import re

class Validador:
    '''
    Clase para validaciones del sistema
    '''
    
    @staticmethod
    
    def validar_email(email : str) -> bool:
        '''
        Valida el formato del email
        
        Args: 
        email : email a validar
        
        returns:
        True si el email es valido, false si no lo es 
        '''
        
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #Con {2,} valida que la extension tenga 2 caracteres despues del correo (.com, .es ,etc)
        
        return re.match(patron,email) is not None
    
    @staticmethod
    
    def validar_monto (monto_str : str) -> tuple:
        
        '''
        Valida el monto y lo convierte en float
        
        Args: 
        monto_str : String del monto
        
        returns: 
        Tupla (es_valido : bool , monto : float )
        '''
        
        try:
            monto = float(monto_str)
            return monto > 0, monto
        
        except ValueError:
            return False, 0.0  
        
        
    @staticmethod
    
    def validar_campo_obligatorio(valor: str , nombre_campo: str) -> bool:
        '''
        Valida que los campos obligatorios no esten vacios
        
        Args: 
        
        valor: valor del campo
        nombre_campo: nombre del campo para mostrar error
        
        returns: 
        true si es valido, false si no
        '''
        
        if not valor or valor.strip() == "":
            print(f"Error: {nombre_campo} no puede estar vacio")
            return False
        return True
    