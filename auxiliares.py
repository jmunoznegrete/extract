def split_path(nombrelargo):
    a = nombrelargo.split('/')
    nombre_archivo = a[-1]
    directorio = ""
    for item in a[0:-1]:
        directorio = directorio + item + '/'

    return directorio, nombre_archivo

