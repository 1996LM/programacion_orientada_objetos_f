#primero se debe creqr un entorno virtual 
#usamos virtualenviroment(venv)
#venv es el nombre por defecto que trae la libreria virtual enviroment
#venv  venv es el nombre mas comun pero se le puede colocar cualquiera
#un entorno virtual es lugar donde coloco las librerias especificas con sus versiones especificas que debo utilizar en el proyecto
#porque en un futuro para poder correr son necesarias las librerias
#.tambien para aislar la libreria
#python -m venv (nombre) crea una carpeta , lo comun es llamarla venv
#usamos el codigo source venv/scripts/activate para activar el entorno virtual , me funciona utilizando gitbash
#antes de crear el repositorio debo crear un archivo .gitignore muy importante 
#que sirve para ignorar lo que yo no quiero versionar de mi proyecto.
#ahora si podemos crear el repositorio
#git init 
#git remote -v para ver que hay
#git push origin master para subir a el repositorio en github
# en github no me aparece la carpeta ven para evitar peso innecesario
#lo anterior son los pasos para crear un proyecto en python
#


#empezamos con FUNCIONES
#loo primero que uno se pregunta es sobre la palabra clave(keywors) que me permite hacer algo en el caso de las funciones 
#la palabra clave es def acompañada del identificador de la funcion que 
# es el nombre que se le da para que python logre identificar un espacio de memoria
#siguen el () que son los parametros que pueden sr muchos tipos y al final se deben colocar :
 def  identificador(params):
    ##############
    ############# bloque de codigo
    ###############
    return respuesta # es obcional tambien los parametros pero el keywords, (), : no son obcionales

#EJEMPLOS

def suma(num1: int,num2: int)-> int: #tambien podemos tipar pero no lo vamos aprender en este curso
    #en visula estudio una funcion se deberia documentar. 
    #
    """ Esta funcion suma dos numeros enteros

    Args:
        num1 (int): numero a suamar
        num2 (int): numero a sumar

    Returns:
        int: suma de los dos numeros
    """
    resultado = num1 + num2
    return resultado

#principios solids de programacion
#S single que indica que cada principio tiene una unica obligacion
#

resp = suma(2,4)
print(resp)


def multiplicacion(num1,num2):
    """Esta fncion multiplica los numeros ingresdos

    Args:
        num1 (int, float, string): numero a multiplicar
        num2 (int, float, string): numero a multiplicar

    Returns:
        int, float, string: numero resultante de multiplicar las dos entradas
    """
    resultado = num1*num2
    return resultado
resp = multiplicacion(8,10)
print(resp)
