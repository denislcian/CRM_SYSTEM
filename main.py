'''
SISTEMA CRM - GESTION DE RELACIONES DE CLIENTES
Archivo principal de ejecucion
'''

from crm_system import CRMSystem

def main():
    '''
    Funcion principal del programa
    '''
    
    try:
        #Creamos instancia del programa
        sistema_crm = CRMSystem()
        
        #Ejecutamos el programa
        
        sistema_crm.ejecutar()
        
    
    except Exception as e : 
        print(f"Error critico: {e}")
    
    

if __name__ == "__main__":
    main()
    