

A = set("abcdefghijklmnopqrstuvwxyz")
D = set("0123456789")
LOCAL = A.union(D)

SUFIJO = "@uptc.edu.co"

def validar_correo(cadena: str) -> bool:
  
  
    if not cadena.endswith(SUFIJO):
        return False

  
    parte_local = cadena[:-len(SUFIJO)]

 
    if len(parte_local) == 0 or parte_local[0] not in A:
        return False

  
    for simbolo in parte_local[1:]:
        if simbolo not in LOCAL:
            return False

   
    return True


# ---------------- PRUEBAS ----------------
print("Correo Ingresado                  Estado de Aceptación")
cadenas_prueba = [
    "juan3@uptc.edu.co",
    "maria@uptc.edu.co",
    "abc123@uptc.edu.co",
    "123juan@uptc.edu.co",
    "juan@uptc.com",
    "MARIA@uptc.edu.co",
    
    "luisa07@uptc.edu.co",  
    "juan3@uptc.edu.co",   
    "aa@uptc.edu.co",       
    "Luisa@uptc.edu.co",    
    "07luisa@uptc.edu.co",  
    "maria@uptc.com",      
    "pepe!@uptc.edu.co",     
]

for c in cadenas_prueba:
    print(f"{c:<30} -> {'   ACEPTADA ✅' if validar_correo(c) else '   RECHAZADA ❌'}")
