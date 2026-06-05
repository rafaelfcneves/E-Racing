import math
import cv2
import mediapipe as mp
import numpy as np
import pydirectinput

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
COLOR = (39, 127, 255)

class Comando:
    """
    Classe para automatizar o pressionar e soltar as teclas com pydirectinput
    """
    def __init__(self, nome, tecla):
        self.nome = nome # Nome do comando (TURN RIGHT, TURN LEFT, AHEAD)
        self.tecla = tecla
        self.pressionada = False # False indica que a tecla não está pressionada
    def pressionar(self):
        """Se a tecla não estiver pressionada, a função aperta ela"""
        if not self.pressionada:
            pydirectinput.keyDown(self.tecla)
            self.pressionada = True
    def soltar(self):
        """Se a tecla estiver pressionada, a função solta."""
        if self.pressionada:
            pydirectinput.keyUp(self.tecla)
            self.pressionada = False

def obter_coordenadas(frame, dados, mp_hands, mp_draw):
    """
    extrai as coordenadas do começo do dedo do meio (Landmark 9) e desenha os LandMarks.
    """
    y_left, y_right, x_left, x_right = None, None, None, None
    # Se não houver 
    if not dados.multi_hand_landmarks:
        return y_left, y_right, x_left, x_right
    
    height, width, _ = frame.shape
    # Recebe as mãos que estão na tela e as desenha
    for i, hand in enumerate(dados.multi_hand_landmarks):
        lm = hand.landmark   # Lista de tuplas com as coordenadas das landmarks
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS) # Desenha as LandMarks
        
        classificacao = dados.multi_handedness[i].classification[0]
        lado = classificacao.label # Variável que indica se é mão esquerda ou direita
        
        if lado == "Left": y_left, x_left = int(lm[9].y * height), int(lm[9].x * width)
        
        elif lado == "Right": y_right, x_right = int(lm[9].y * height), int(lm[9].x * width)

        # Faz uma lista de pontos x e y dos LandMarks e encontra o min para o texto de classificação
        coordenadas_x = [landmark.x for landmark in lm]
        coordenadas_y = [landmark.y for landmark in lm]
        text_x = int(min(coordenadas_x) * width)    # Coordenada x do texto
        text_y = int(min(coordenadas_y) * height) - MARGIN   # Coordenada y do texto

        cv2.putText(frame,lado,(text_x, text_y),cv2.FONT_HERSHEY_SIMPLEX, 0.8,COLOR,2, cv2.LINE_AA)
    
    return y_left, y_right, x_left, x_right

def calcular_angulacao(y_left, y_right, x_left, x_right):
    """
    Calcula o ângulo entre as mãos e retorna uma string que diz o comando que tem que ser executado.
    """
    comando=None
    if None in (y_left, y_right, x_left, x_right):
        return
    delta_y = y_right - y_left
    delta_x = x_right - x_left
    tetha = np.arctan2(delta_y, delta_x) # Calcula o ângulo entre as mãos
    if tetha < 0 and -(math.pi/2) < tetha < -(math.pi/12):
        comando = "TURN LEFT"
    elif tetha > 0 and math.pi/12 < tetha < math.pi/2:
        comando = "TURN RIGHT"
    elif -(math.pi/12) < tetha < (math.pi/12):
        comando = "AHEAD"
    return comando

def desenhar_comando(comando, frame):
    if comando is None:
        return
    h, width, _ = frame.shape
    cv2.putText(frame,comando,(int(width/2) - 100, 50),cv2.FONT_HERSHEY_SIMPLEX,0.8,COLOR,2,cv2.LINE_AA)

def executar_acao(comando, virar_esquerda, virar_direita, acelerar):
    """
    Executa as ações do carro. Virar para a esquerda, direita e seguir em frente
    """
    if comando != None:
        acelerar.pressionar()
        if comando == "TURN LEFT":
            virar_direita.soltar()
            virar_esquerda.pressionar()
        elif comando == "TURN RIGHT":
            virar_esquerda.soltar()
            virar_direita.pressionar()
        elif comando == "AHEAD":
            virar_direita.soltar()
            virar_esquerda.soltar()
    else:
        acelerar.soltar()
        virar_direita.soltar()
        virar_esquerda.soltar()


def main():
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    virar_esquerda = Comando(nome="TURN LEFT",tecla='a')
    virar_direita = Comando(nome="TURN RIGHT",tecla='d')
    acelerar = Comando(nome="AHEAD",tecla='w')

    # Chamada da WebCam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("A camera nao pode ser aberta.")

    # Evita vazamento de memória caso a aplicação feche
    with mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6,
    ) as hands:

    # Loop principal da transmissão de vídeo.
        while True:
            # Captura o frame da transmissão
            ok, frame = cap.read()
            if not ok:
                break

            # Espelha o frame
            frame = cv2.flip(frame, 1)

            # Converte o frame de BGR para RGB, pois MediaPipe só reconhece em RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Retorna um objeto que contém uma lista das mãos que estão na tela (máx 2),
            # Uma tupla que contém as coordenadas dos Landmarks
            dados = hands.process(frame_rgb)
            y_left, y_right, x_left, x_right = obter_coordenadas(frame, dados, mp_hands, mp_draw)

            comando = calcular_angulacao(y_left, y_right, x_left, x_right)
            desenhar_comando(comando,frame)

            # Executa a ação do volante
            executar_acao(comando, virar_esquerda, virar_direita, acelerar)
            
            # Função que cria a janela onde será transmitido o vídeo.
            cv2.imshow("Teste de camera", frame)

            # Quebra o loop da transmissão de vídeo ao apertar "q"
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    # Libera a Webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()