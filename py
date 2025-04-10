import math

def calcular_tempo_semaforo(distancia, velocidade_permitida, aceleracao):
    tempo_aceleracao = velocidade_permitida / aceleracao
    distancia_aceleracao = 0.5 * aceleracao * (tempo_aceleracao ** 2)
    
    if distancia_aceleracao >= distancia:
        tempo_total = math.sqrt((2 * distancia) / aceleracao)
    else:
        distancia_constante = distancia - distancia_aceleracao
        tempo_constante = distancia_constante / velocidade_permitida
        tempo_total = tempo_aceleracao + tempo_constante
    
    tempo_semaforo = tempo_total - 3
    return max(0, tempo_semaforo)

distancia = 500
velocidade_permitida_kmh = 50
aceleracao = 2

velocidade_permitida = velocidade_permitida_kmh / 3.6
tempo = calcular_tempo_semaforo(distancia, velocidade_permitida, aceleracao)
print(f"O semáforo deve abrir {tempo:.2f} segundos após o semáforo anterior")