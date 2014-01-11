__author__ = 'yoda'
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


def zdjecie():
    img = cv2.imread('/home/yoda/Obrazy/screen.jpg') #odczytanie zdjecia
    cv2.namedWindow('image',cv2.WINDOW_NORMAL) #ustalenie rozmiaru zdjecia
    cv2.imshow('image',img) #wlaczenie zdjecia
    cv2.waitKey(0) #czekanie na klawisz
    cv2.destroyAllWindows() #usuniecie okna

def zdjecie_z_Plottem():
    img = cv2.imread('/home/yoda/Obrazy/screen.jpg',0)
    #plt.imshow(img, cmap = 'gray', interpolation = 'nearest') #plot z efektami :) Warto obczaic dokumentacja

    plt.imshow(img, cmap = 'hot', interpolation = 'bicubic') #plot z efektami :) Warto obczaic dokumentacja
    #imwrite zapisuje zdjecie do pliku
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def camera():
    cap = cv2.VideoCapture(-1) #przyjecie kamery
    while(True):
        ret, frame = cap.read() #odczyt obrazu
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #odtwarzanie z czego i jakie kolory
        cv2.imshow('frame',gray) #pokazanie go
        if cv2.waitKey(10) & 0xFF == ord('q'): # klawisz q zamyka
            break

    cap.release() #czyszczenie bufora
    cv2.destroyAllWindows() #zamykanie okien




def readAvideo():
    cap = cv2.VideoCapture('/home/yoda/Video/cos.avi') # z jakiego pliku to czytamy
    while (cap.isOpened()): #dopoki plik otwarty
        ret,frame = cap.read() #odczytuj
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #inicjalizacja obrazu

        #gray = cv2.flip(frame,0) odwrocenie obrazu :)
        cv2.imshow('frame',gray) #pokazanie go
        if cv2.waitKey(1) & 0xFF == ord('q'): # q zamyka okna
            break
    cap.release() #czyszczenie bufora
    cv2.destroyAllWindows() # zamykanie okienek




def main():
    print('Czytanie obrazka')

if __name__ == "__main__":
    main()
