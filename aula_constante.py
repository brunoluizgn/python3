"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
... <- Contagem de complexidade (ruim)
"""
velocidade = 61 #velocidade atual do carro
local_carro = 100 #local em que o carro esta na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar está
RADAR_RAGER = 1 # A distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RAGER) and \
    local_carro <= (LOCAL_1 + RADAR_RAGER) and \
        velocidade > RADAR_1:
    print('carro multado em radar 1')

