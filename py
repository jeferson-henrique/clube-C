# Função para calcular o tempo de atraso entre semáforos
def calcular_tempo_atraso(distancia, velocidade):
    # Converter velocidade de km/h para m/s (1 km/h = 1000 m / 3600 s = 5/18 m/s)
    velocidade_ms = velocidade * (5 / 18)
    
    # Calcular o tempo (em segundos) = distância (em metros) / velocidade (em m/s)
    tempo = distancia / velocidade_ms
    return tempo

# Função para simular a sincronização dos semáforos
def sincronizar_semaforos(distancia, velocidade, num_semaforos):
    print(f"Velocidade permitida: {velocidade} km/h")
    print(f"Distância entre semáforos: {distancia} metros")
    print(f"Número de semáforos: {num_semaforos}")
    print("\nSincronização dos semáforos:")
    
    # O primeiro semáforo abre no tempo 0
    tempo_atual = 0
    print(f"Semáforo 1 abre no tempo: {tempo_atual:.2f} segundos")
    
    # Calcular o tempo de atraso entre semáforos
    tempo_entre_semaforos = calcular_tempo_atraso(distancia, velocidade)
    
    # Simular a abertura dos próximos semáforos
    for i in range(2, num_semaforos + 1):
        tempo_atual += tempo_entre_semaforos
        print(f"Semáforo {i} abre no tempo: {tempo_atual:.2f} segundos")

# Exemplo de uso
distancia = 50  # Distância entre semáforos em metros
velocidade = 60  # Velocidade permitida em km/h
num_semaforos = 4  # Número de semáforos na sequência

# Chamar a função para sincronizar os semáforos
sincronizar_semaforos(distancia, velocidade, num_semaforos)