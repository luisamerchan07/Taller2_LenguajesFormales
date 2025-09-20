

A = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
B = set("abcdefghijklmnopqrstuvwxyz")
D = set("0123456789")

def validar_contrasena(cadena: str) -> bool:
  

    estado = "q0" 

    for i, simbolo in enumerate(cadena, start=1):

        if estado == "q0":  
            if simbolo in A:
                estado = "q1"
            else:
                return False

        elif estado == "q1":  
            if simbolo in B:       
                estado = "q1"
            elif simbolo in D:            
                estado = "q2"
            elif simbolo in A:    
                return False
            else:
                return False

        elif estado == "q2":  
            if simbolo in D:              
                estado = "q2"
            else:
                return False

      
    return estado == "q2"


# ---------------- PRUEBAS ----------------
print("Contraseña ingresada      ->     Estado de aceptación")
cadenas_prueba = [
    "A123",         
    "Sogamoso2025", 
    "Uptc9",       
    "X0",          
    "Z99",         
    "1234",        
    "soga2025",     
    "UPTC",    
    "aX99",      
    "AA1",         
]

for c in cadenas_prueba:
    print(c.ljust(20), "    ->", "   ACEPTADA ✅" if validar_contrasena(c) else "   RECHAZADA ❌")
