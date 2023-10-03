import prefect
from prefect import task, Flow

@task
def tarea1():
    return "Hola, "

@task
def tarea2():
    return "Mundo!"

@task
def tarea3(a, b):
    return f"{a}{b}"

# Crea un flujo de trabajo Prefect
with Flow("MiFlujoDeTrabajo") as flow:
    resultado1 = tarea1()
    resultado2 = tarea2()
    resultado_final = tarea3(resultado1, resultado2)

# Ejecuta el flujo de trabajo
flow_state = flow.run()

# Imprime el resultado final
print(flow_state.result[resultado_final])