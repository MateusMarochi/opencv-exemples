import cv2 as cv

img = cv.imread('imagens/Lenna.png')            # Lê a imagem  

cv.imshow('Lenna', img)                         # Mostra a imagem

cv.waitKey(0)                                   # Faz uma pausa na execução até que tenha algum retorno do teclado

cv.destroyAllWindows()                          # Fecha todas as janelas abertas