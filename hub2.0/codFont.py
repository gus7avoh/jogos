from random import choice, randint
import menu, smart, Jogos

sup = True
while sup == True:
    new = True
    while new == True:

        p = menu.menuPrincipal()
        
        if p == 1:
            Jogos.PPt()
   
        elif p == 2:
            Jogos.jogoDaForca()

        elif p == 3:
            Jogos.ParImpar()
 
        elif p == 4:
            Jogos.AdvUmNumero()


                
        

