import matplotlib.pyplot as plt
import os

def contar_respuestas(respuestas):
    visual = respuestas.count(1)
    auditivo = respuestas.count(2)
    kinestesico = respuestas.count(3)
    return visual, auditivo, kinestesico

def generar_grafica(respuestas):
    visual, auditivo, kinestesico = contar_respuestas(respuestas)
    categorias = ['Visual', 'Auditivo', 'Kinestésico']
    valores = [visual, auditivo, kinestesico]

    plt.figure(figsize=(6, 4))
    bars = plt.bar(categorias, valores, color=['blue', 'green', 'orange'])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, int(yval), ha='center')

    plt.title("Distribución de respuestas por estilo")
    plt.ylim(0, 15)  
    plt.ylabel("Cantidad de respuestas")
    plt.tight_layout()

    os.makedirs("app", exist_ok=True)
    path = "app/grafica_estilo.png"
    plt.savefig(path)
    plt.close()
    return path
