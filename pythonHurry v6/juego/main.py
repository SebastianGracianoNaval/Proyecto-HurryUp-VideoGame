import pygame, sys
import math
from pygame.locals import *
from button import Button
import tkinter as tk
from tkinter import messagebox
import random
import os.path

pygame.init()



pygame.mixer.music.load('assets/intro.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


#HURRY = pygame.display.set_mode((900, 250))

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/fondo_menu.png")

#HP = pygame.image.load("assets/titulo.png")


#modifica la fuente
def get_font(size):
    return pygame.font.Font("assets/Glossy Sheen Shine DEMO.ttf", size)

#es el encargado de poder cambiar las fuentes en el menu
def get_fontMenu(size):
    return pygame.font.Font("assets/Woodtrap.ttf", size)

#Menu
def menu_principal():
    pygame.display.set_caption("menu")
    while True:
        SCREEN.blit(BG, (0, 0))
        
        #TITULO HURRY UP HURRY.blit(HP, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(160).render("Hurry UP", True, "#971539")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        JUGAR_BOTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="JUGAR", font=get_fontMenu(75), base_color="#8A5943", hovering_color="Black")
        OPCIONES_BOTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPCIONES", font=get_fontMenu(75), base_color="#8A5943", hovering_color="Black")
        SALIR_BOTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="SALIR", font=get_fontMenu(75), base_color="#8A5943", hovering_color="Black")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [JUGAR_BOTON, OPCIONES_BOTON, SALIR_BOTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JUGAR_BOTON.checkForInput(MENU_MOUSE_POS):
                    jugar()
                if OPCIONES_BOTON.checkForInput(MENU_MOUSE_POS):
                    opciones()
                if SALIR_BOTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
 
#Opciones muestra el menu donde se encuentra toda la parte de ajustes  
def opciones():
    pygame.display.set_caption("opciones")
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        OPTIONS_TEXT = get_font(100).render("OPCIONES", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        VOLUMEN_BOTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250), 
                            text_input="VOLUMEN", font=get_font(75), base_color="#8A5943", hovering_color="Black")
        OPCIONES_BOTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPCION x", font=get_font(75), base_color="#8A5943", hovering_color="Black")
        SALIR_BOTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="SALIR", font=get_font(75), base_color="#8A5943", hovering_color="Black")

        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        for button in [ VOLUMEN_BOTON, OPCIONES_BOTON, SALIR_BOTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  VOLUMEN_BOTON.checkForInput(OPTIONS_MOUSE_POS):
                    volumen()
                #if OPCIONES_BOTON.checkForInput(OPTIONS_MOUSE_POS):
                    #opciones()
                if SALIR_BOTON.checkForInput(OPTIONS_MOUSE_POS):
                    menu_principal()

        pygame.display.update()

#El menu del volumen que se encuentra adentro de opciones      
def volumen():
    pygame.display.set_caption("volumen")
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        SCREEN.fill("White")

        VOLUMEN_TEXT = get_font(160).render("VOLUMEN", True, "#971539")
        VOLUMEN_RECT =  VOLUMEN_TEXT.get_rect(center=(640, 100))

        BAJAR_VOLUMEN_BOTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300,  250), 
                            text_input="bajar", font=get_fontMenu(75), base_color="#8A5943", hovering_color="Black")
        SUBIR_VOLUMEN_BOTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(900, 250), 
                            text_input="subir", font=get_fontMenu(75), base_color="#8A5943", hovering_color="Black")
        MUTEAR_VOLUMEN_BOTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 400), 
                            text_input="mutear", font=get_fontMenu(75), base_color="#8A5943", hovering_color="Black")
        SALIR_BOTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="volver al menu", font=get_fontMenu(75), base_color="#8A5943", hovering_color="Black")



        SCREEN.blit( VOLUMEN_TEXT, VOLUMEN_RECT)

        for button in [BAJAR_VOLUMEN_BOTON, SUBIR_VOLUMEN_BOTON,  MUTEAR_VOLUMEN_BOTON,SALIR_BOTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BAJAR_VOLUMEN_BOTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
                if SUBIR_VOLUMEN_BOTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
                if  MUTEAR_VOLUMEN_BOTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.set_volume(0.0)
                if  SALIR_BOTON.checkForInput(MENU_MOUSE_POS):
                    menu_principal()

        pygame.display.update()
 
#Aca se encuentra la parte de seleccion de niveles con el barco
def jugar():
          
    pygame.display.set_caption("jugar")
    #esto es para que el movimiento sea random
    #self.dir_x = random.choice([-5, 5])
    #self.dir_y = random.choice([-5, 5])
    SCREEN.fill("black")
    
    
    FPS  = 60
    mar = (93, 173, 226)

    carpeta_juego = os.path.dirname(__file__)






#Esta clase tiene la imagen y las dimenciones de la isla
    class islita:
        def __init__(self,fichero_imajen):
            
            #imagen
            self.imagen =pygame.image.load("assets/isla.png").convert_alpha()
            
            #dimenciones
            self.ancho,self.alto = self.imagen.get_size()

            
#Esta clase tiene la imagen,dimenciones  y funcion de movimiento del barquito           
    class barquito:
        def __init__(self,fichero_imajen):
            #atributos de la clase
        
            #imagen
            self.imagen =pygame.image.load("assets/barquito.png").convert_alpha()
            
            #dimenciones
            self.ancho,self.alto = self.imagen.get_size()
            
            
            #direccion de movimiento
            self.dir_x = 0
            self.dir_y = 0
            
            
            
        def mover(self):
            # moverse en y
            self.y += self.dir_y
            if self.y <= 0:
                self.y = 0
           
            # moverse en x
            self.x += self.dir_x
            if self.x <= 29:
                self.x = 0
            
                
#en esta clase se proyecta la parte jugable del barco y las islas            
    def main():
        
        pygame.init()
        
        SCREEN.fill("black")
        pygame.display.set_caption("juego1")
        
        #creacion de barco
        barco = barquito(os.path.join(carpeta_juego,"barquito.png"))
        barco.y = 200
        barco.x = 400
        
        
        isla = islita(os.path.join(carpeta_juego,"isla.png"))  
        isla.y = 60
        isla.x = 60
        
        #obtener rectángulos de las imágenes
        barquito_rect = pygame.Rect(barco.x, barco.y, barco.ancho, barco.alto)
        islita_rect = isla.imagen.get_rect()
        
        #bucle principal
        jugando = True
        colisionando = False
        while jugando:
            barco.mover()
            
            
            SCREEN.fill(mar)
            SCREEN.blit(barco.imagen, (barco.x,barco.y))   
            SCREEN.blit(isla.imagen, (isla.x,isla.y)) 
            
                    
            
        # actualizar rectángulo del barco
            barquito_rect = pygame.Rect(barco.x, barco.y, barco.ancho, barco.alto)
            
            if not colisionando and barquito_rect.colliderect(islita_rect):
                colisionando = True
                
            if colisionando:
                
                for event in pygame.event.get():
                    if colisionando and barquito_rect.colliderect(islita_rect):
                        inicio_pantalla_matematica()
                
            
            
                        
                    

            for event in pygame.event.get():
                if event.type == QUIT:
                    jugando = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        barco.dir_y = -5
                    elif event.key == pygame.K_s:
                        barco.dir_y = 5
                    elif event.key == pygame.K_a:
                        barco.dir_x = -5
                    elif event.key == pygame.K_d:
                        barco.dir_x = 5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        barco.dir_y = 0
                    elif event.key == pygame.K_a or event.key == pygame.K_d:
                        barco.dir_x = 0
                    elif event.key == pygame.K_ESCAPE:
                        menu_principal()
            
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)
                
        pygame.quit()
    if __name__ == "__main__":
        main()       

#islas

#Matematica

#Aca se muestra el inicio de la pantalla de matematica
def inicio_pantalla_matematica():
    pygame.display.set_caption("inicio de isla")
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        INGRESAR_TEXT = get_font(100).render("¿DESEA INGRESAR A LA ISLA?", True, "#b68f40")
        INGRESAR_RECT = INGRESAR_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(INGRESAR_TEXT, INGRESAR_RECT)
        
        SI_BOTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250), 
                            text_input="SI", font=get_font(75), base_color="#8A5943", hovering_color="Black")
        NO_BOTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="NO", font=get_font(75), base_color="#8A5943", hovering_color="Black")
        

        SCREEN.blit(INGRESAR_TEXT, INGRESAR_RECT)

        for button in [SI_BOTON, NO_BOTON, ]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SI_BOTON.checkForInput(OPTIONS_MOUSE_POS):
                        isla_geografia()
                    if NO_BOTON.checkForInput(OPTIONS_MOUSE_POS):
                        jugar()
                    


        pygame.display.update()

#Aca se muestra la isla 
def isla_geografia():
    pygame.display.set_caption("isla_matematica")
    
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        

        
        #PLAY_TEXT = get_font(45).render("ESTA PANTALLA ES LA ISLA", True, "black")
        #PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        #SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        # Definir las preguntas y respuestas
        preguntas = [
            {
                "pregunta": "¿Cuál es la capital de Francia?",
                "respuestas": ["Londres", "Madrid", "París", "Berlín"],
                "respuesta_correcta": "París"
            },
            {
                "pregunta": "¿Cuál es el río más largo del mundo?",
                "respuestas": ["Nilo", "Amazonas", "Yangtze", "Misisipi"],
                "respuesta_correcta": "Amazonas"
            },
            {
                "pregunta": "¿Cuál es la montaña más alta del mundo?",
                "respuestas": ["Everest", "K2", "Kilimanjaro", "Mont Blanc"],
                "respuesta_correcta": "Everest"
            }
        ]


        # Definir los colores
        BLANCO = (255, 255, 255)
        NEGRO = (0, 0, 0)

        # Definir el tamaño de la ventana
        ventana_tamaño = (1280, 720)

        # Crear la ventana de Pygame
        ventana = pygame.display.set_mode(ventana_tamaño)

        # Definir la fuente y el tamaño del texto
        font=get_fontMenu(75)

        # Inicializar variables del juego
        puntaje = 0
        preguntas_respondidas = 0
        preguntas_restantes = preguntas.copy()  # Copiar la lista de preguntas para tener una lista de preguntas restantes

        # Bucle principal del juego
        while preguntas_restantes:
            # Seleccionar una pregunta al azar de la lista de preguntas restantes
            pregunta_actual = random.choice(preguntas_restantes)

            # Mostrar la pregunta en la pantalla
            pregunta_texto = font.render(pregunta_actual["pregunta"], True, BLANCO)
            pregunta_rect = pregunta_texto.get_rect()
            pregunta_rect.center = (ventana_tamaño[0] / 2, ventana_tamaño[1] / 2 - 50)

            ventana.fill(NEGRO)
            ventana.blit(pregunta_texto, pregunta_rect)

            # Mostrar las respuestas en la pantalla
            respuesta_rects = []
            for i, respuesta in enumerate(pregunta_actual["respuestas"]):
                respuesta_texto = font.render(respuesta, True, BLANCO,)
                respuesta_rect = respuesta_texto.get_rect()
                respuesta_rect.center = (ventana_tamaño[0] / 2, ventana_tamaño[1] / 2 + 50 + i * 50)

                respuesta_rects.append(respuesta_rect)

                ventana.blit(respuesta_texto, respuesta_rect)

            # Actualizar la pantalla
            pygame.display.update()

            # Esperar a que el jugador seleccione una respuesta
            respuesta_seleccionada = None
            while respuesta_seleccionada is None:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        # Obtener la posición del cursor
                        cursor_posicion = pygame.mouse.get_pos()

                        # Verificar si el jugador ha seleccionado una respuesta
                        for i, respuesta_rect in enumerate(respuesta_rects):
                            if respuesta_rect.collidepoint(cursor_posicion):
                                respuesta_seleccionada = i
                                break

            # Mostrar si la respuesta seleccionada es correcta o incorrecta
            if pregunta_actual["respuestas"][respuesta_seleccionada] == pregunta_actual["respuesta_correcta"]:
                print("¡Respuesta correcta!")
                puntaje += 1
            else:
                
                jugar_volver = Button(image=None, pos=(640, 460), 
                            text_input="VOLVER", font=get_fontMenu(75), base_color="black", hovering_color="Green")

                jugar_volver.changeColor(PLAY_MOUSE_POS)
                jugar_volver.update(SCREEN)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if jugar_volver.checkForInput(PLAY_MOUSE_POS):
                            jugar()
                            
                print("Respuesta incorrecta.")

            # Eliminar la pregunta actual de la lista de preguntas restantes
            preguntas_restantes.remove(pregunta_actual)
            
            
            

            

        # Si se han respondido todas las preguntas, salir del juego
        print("Juego terminado. Tu puntaje es:", puntaje)
        

        

        pygame.display.update()
    
#lengua

#historia

#biologia

#conocimiento tecnico

#isla final    
   
    
    
    
    
    
   
menu_principal()