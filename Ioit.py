import time
import random
import psutil

def simular_dispositivos(num_devices: int = 20):
    print(f"Simulando {num_devices} dispositivos...")
    resultados = []

    for device_id in range(1, num_devices + 1):
        inicio = time.time()

        # Simula um tempo de envio entre 50 e 200 ms
        time.sleep(random.uniform(0.05, 0.2))

        # ~5% de chance de falha
        sucesso = random.random() > 0.05
        duracao = time.time() - inicio
        resultados.append((device_id, sucesso, duracao))

        status = "✔️ Envio realizado!" if sucesso else "❌ Falha no envio!"
        print(f"[Dispositivo {device_id}] {status} ({duracao:.4f} s)")

    # Métricas básicas
    tempo_medio = sum(r[2] for r in resultados) / len(resultados)
    perdas = sum(1 for r in resultados if not r[1])
    taxa_perda = perdas / len(resultados) * 100

    # Impacto na máquina (amostra de CPU/RAM num intervalo de 1s)
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()

    print("===== MÉTRICAS =====")
    print(f"⏱️ Tempo médio de envio: {tempo_medio:.4f} s")
    print(f"📉 Taxa de perda: {taxa_perda:.2f}%")
    print(f"💻 Impacto no sistema: CPU {cpu:.1f}%, RAM usada {mem.used / (1024**3):.2f} GB "
          f"de {mem.total / (1024**3):.2f} GB")

if __name__ == "__main__":
    simular_dispositivos(20)  # ajuste para 5–20 conforme pedido
