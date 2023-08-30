def division_segura(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: División entre cero no es valida"
    except TypeError:
        return "Error: Tipos de datos no válidos para la operación"

# Ejemplos de uso
num1 = 10
num2 = 0
resultado1 = division_segura(num1, num2)
print("\n",resultado1)

num3 = "10"
num4 = 2
resultado2 = division_segura(num3, num4)
print("\n",resultado2)

num5 = 10
num6 = 2
resultado3 = division_segura(num5, num6)
print("\n",resultado3,"\n")