"""
Desarrollo guiado por pruebas
1. Elegir un requisito: Se elige de una lista el requisito que se cree que nos dará mayor conocimiento del problema y que a la vez sea fácilmente implementable.
2. Escribir una prueba: Se comienza escribiendo una prueba para el requisito.
3. Verificar que la prueba falla.
4. Escribir la implementación: Escribir el código más sencillo que haga que la prueba funcione.
5. Ejecutar las pruebas automatizadas: Verificar si todo el conjunto de pruebas funciona correctamente.
6. REPETIR desde 1
"""

# Ejemplo 1
"""
Especificacion: escribir una funcion que diga si un número es par o impar

Requisitos:
    1. Si se ingresa un numero par entonces la funcion debe devolver el string "es par"
    2. Si se ingresa un numero impar entonces la funcion debe devolver el string "es impar"
"""

def decidir_par_impar(numero):
    if numero % 2 == 0:
        return "Nro Par"
    else:
        return "Nro Impar"


valor_resultado = decidir_par_impar(4)
assert valor_resultado == "PAR", "Prueba 1 Fallida"

valor_resultado = decidir_par_impar(5)
assert valor_resultado == "IMPAR", "Prueba 2 Fallida"

valor_resultado = decidir_par_impar(1001)
assert valor_resultado == "IMPAR", "Prueba 3 Fallida"

valor_resultado = decidir_par_impar(-1000)
assert valor_resultado == "PAR", "Prueba 4 Fallida"


print("Todas las pruebas fueron superadas =)")