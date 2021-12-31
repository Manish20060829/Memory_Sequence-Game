import pygame
from pygame.constants import MOUSEBUTTONDOWN
import random as r
pygame.init()
slices = 0
guess = 0
length1 = 0
right = False
guess_check = True
sequence = True
choose = False        
#creates the board using nested for loop and updates x and y
def create_board(win,x,y,width,height,grey):
    for j in range(3):
        x = 120
        if j > 0:
            y+=height+20
        for i in range(3):
            pygame.draw.rect(win, grey,(x,y,width,height))
            x+=width+20

#draws a white square over when going throught the list
def start_sequence(x,y,width,height,win,order,white):
    if order == 1:
        pygame.draw.rect(win, white,(x,y,width,height))
    if order == 2:
        pygame.draw.rect(win, white,(x+width+20,y,width,height))
    if order == 3:
        pygame.draw.rect(win, white,(x+(width+20)*2,y,width,height))
    if order == 4:
        pygame.draw.rect(win, white,(x,y+height+20,width,height))
    if order == 5:
        pygame.draw.rect(win, white,(x+width+20,y+height+20,width,height))
    if order == 6:
        pygame.draw.rect(win, white,(x+(width+20)*2,y+height+20,width,height))
    if order == 7:
        pygame.draw.rect(win, white,(x,y+(height+20)*2,width,height))
    if order == 8:
        pygame.draw.rect(win, white,(x+width+20,y+(height+20)*2,width,height))
    if order == 9:
        pygame.draw.rect(win, white,(x+(width+20)*2,y+(height+20)*2,width,height))

#allows player to click on the square and makes sure he follows the right sequence
def memory(x,y,width,height,win,white,s):
    global slices, guess, right, length1, guess_check, sequence, choose
    sequence_list = [1,2,3,4,5,6,7,8,9]
    pressed = False
    mouse = pygame.mouse.get_pos()
    mousedown = pygame.mouse.get_pressed()
    #checks mouse position and if it is clicking on a certain square
    if x < mouse[0] < x+width and y < mouse[1] < y+height and sequence == False and mousedown[0] == True:
       pygame.draw.rect(win, white,(x,y,width,height))
       guess = 1
       pressed = True
    if x+width+20 < mouse[0] < x+width+20+width and y < mouse[1] < y+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x+width+20,y,width,height))
        guess = 2 
        pressed = True
    if x+(width+20)*2 < mouse[0] < x+(width+20)*2+width and y < mouse[1] < y+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x+(width+20)*2,y,width,height))
        guess = 3
        pressed = True
    if x < mouse[0] < x+width and y+height+20 < mouse[1] < y+height+20+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x,y+height+20,width,height))
        guess = 4
        pressed = True
    if x+width+20 < mouse[0] < x+width+20+width and y+height+20 < mouse[1] < y+height+20+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x+width+20,y+height+20,width,height))
        guess = 5
        pressed = True
    if x+(width+20)*2 < mouse[0] < x+(width+20)*2+width and y+height+20 < mouse[1] < y+height+20+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x+(width+20)*2,y+height+20,width,height))
        guess = 6
        pressed = True
    if x < mouse[0] < x+width and y+(height+20)*2 < mouse[1] < y+(height+20)*2+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x,y+(height+20)*2,width,height))
        guess = 7
        pressed = True
    if x+width+20 < mouse[0] < x+width+20+width and y+(height+20)*2 < mouse[1] < y+(height+20)*2+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x+width+20,y+(height+20)*2,width,height))
        guess = 8
        pressed = True
    if x+(width+20)*2 < mouse[0] < x+(width+20)*2+width and y+(height+20)*2 < mouse[1] < y+(height+20)*2+height and sequence == False and mousedown[0] == True:
        pygame.draw.rect(win, white,(x+(width+20)*2,y+(height+20)*2,width,height))
        guess = 9
        pressed = True
    #checks if a square has been clicked and add to length variable also makes sure it adds 1 value for each click
    if guess == s[slices] and guess_check == True and pressed == True:
        guess_check = False
        length1 += 1
        right = True
    elif pressed == False:
        guess_check = True
    if length1 >= len(s) and pressed == False:
        slices = 0
        guess = 0
        length1 = 0
        choose = True
        right = False
    #goes to the next part of the sequence after the person let go of the press
    if right == True and pressed == False and length1 < len(s):
        slices += 1
        right = False
    #checks if their is an incorrect guess
    elif guess != s[slices] and pressed == True:
        exit()
    #increases the level and adds a number to the sequence
    if choose == True:
        number = r.choice([i for i in sequence_list if i != s[-1]])
        s.append(number)
        choose = False
        sequence = True
        print("_")

#diplays the level
def level(white,win,s,y):
    font = pygame.font.SysFont('freesansbold.ttf', 32)
    text = font.render(F'Level: {len(s)}', None, white)
    win.blit(text,(600/2-45, y/2-16))

def main():
    global slices, sequence,choose
    white = (255,255,255)
    grey = (50,100,150)
    s = [r.randint(1,9)]
    clock = pygame.time.Clock()
    x = 120
    y = 120
    width = 100
    height = 100
    index = -1
    length = 0
    order = 0
    #timer to update the events.
    pygame.time.set_timer(pygame.USEREVENT,1000)
    win = pygame.display.set_mode((600,600))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #checkcs if event was updated and sequence is playing and uses length to see if sequence is finished
            if event.type == pygame.USEREVENT and length < len(s) and sequence == True:
                index += 1
                length += 1
                order = s[index]
                print(order)
            elif length >= len(s):
                index = -1
                length = 0
                order = 0
                sequence = False
        win.fill((2,190,252))
        level(white,win,s,x)
        create_board(win,x,y,width,height,grey)
        start_sequence(x,y,width,height,win,order,white)
        memory(x,y,width,height,win,white,s)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
main()

