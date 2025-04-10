import math
import flet as ft

def main(page: ft.Page):
    page.title = "Sincronização de Semáforos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = False
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    def calcular(e):
        try:
            distancia = float(txt_distancia.value)
            velocidade = float(txt_velocidade.value)
            aceleracao = float(txt_aceleracao.value)
            
            velocidade_ms = velocidade / 3.6
            tempo = calcular_tempo_semaforo(distancia, velocidade_ms, aceleracao)
            
            resultado.value = f"O semáforo deve abrir {tempo:.2f} segundos após o anterior"
            page.update()
        except ValueError:
            resultado.value = "Por favor, insira valores numéricos válidos"
            page.update()

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

    titulo = ft.Text("Sincronização de Semáforos", size=24, weight=ft.FontWeight.BOLD)
    
    txt_distancia = ft.TextField(label="Distância entre semáforos (metros)", width=300)
    txt_velocidade = ft.TextField(label="Velocidade máxima da via (km/h)", width=300)
    txt_aceleracao = ft.TextField(label="Aceleração do veículo (m/s²)", width=300)
    
    btn_calcular = ft.ElevatedButton("Calcular", on_click=calcular, width=300)
    resultado = ft.Text(size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)

    page.add(
        ft.Column(
            [
                titulo,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                txt_distancia,
                txt_velocidade,
                txt_aceleracao,
                btn_calcular,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                resultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)