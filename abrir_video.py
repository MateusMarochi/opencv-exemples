import cv2 as cv
import numpy as np

video = cv.VideoCapture('videos/bola.mp4')      # Lê o arquivo de video

if (video.isOpened()== False):                  # Verifica se o arquivo foi lido corretamente
  print("Erro ao abrir esse arquivo")

while(video.isOpened()):
  ret, frame = video.read()
  if ret == True:

    cv.imshow('Bola',frame)                     # Mostra frame-a-frame o video

    if cv.waitKey(25) & 0xFF == ord('q'):       # Pressione 'q' no teclado para finalizar
      break

  else: 
    break

video.release()                                 # Limpa o objeto com o video

cv.destroyAllWindows()                          # Fecha todas as janelas abertas