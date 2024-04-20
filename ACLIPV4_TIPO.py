#Crear un función y script en Python, que al momento que un usuario introduzca el número de ACL IPv4, señale si es una ACL Layer 2, Layer 3, Estándar, Extendida o si el número no corresponde a una lista de control de acceso.

def ACLIPV4_TIPO(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL IPv4 Estándar (Layer 3)"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL IPv4 Extendida (Layer 3)"
    elif numero_acl >= 1000 and numero_acl <= 1099:
        return "ACL IPv4 Estándar (Layer 2)"
    elif numero_acl >= 1100 and numero_acl <= 1199:
        return "ACL IPv4 Extendida (Layer 2)"
    else:
        return "El número no corresponde a una lista de control de acceso."

numero_acl = int(input("Ingrese el número de ACL IPv4: "))
print(ACLIPV4_TIPO(numero_acl))
