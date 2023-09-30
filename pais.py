paises= {"Mexico":1,"Estados Unidos":2, "Colombia":3}
pais= {1,2,3}
def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP
    """
    try: 
        return paises[pais]
    except KeyError: 
        return None