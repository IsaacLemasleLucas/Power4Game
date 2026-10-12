class Grille:
    
    ## INITALISATION
    def __init__(self, longueur:int=7,hauteur:int=6):
        self.long = longueur 
        self.haut = hauteur
        self.gril = []
        
    def init_grille(self):
        for i in range (self.haut):
            liste_haut = []
            for j in range(self.long):
                liste_haut += [0]
            self.gril += [liste_haut]

    ## PLAY
    def play(self, column:int, id=1):
        line = len(self.gril)
        full = True
        for i in range(line):
            try:
                if self.gril[line-i-1][column] == 0:
                    self.gril[line-i-1][column] = id
                    full = False
                    break
            except IndexError :
                print("Colonne complete --> En choisir une autre")
                break
        if full : print("Colonne complete --> En choisir une autre")

    #TODO
    def check(self):
        for elem in self.gril():
            pass
    
    #TODO
    def gril_status(self, column:int):
        line = len(self.gril)
        max_full = self.haut
        for i in range(self.haut):
            if self.gril[line-i-1][column] == 0:
                if i==0:
                    max_full = 0
                else: 
                    max_full = i
        return max_full
            
        
    ## GET & SET
    def get_nb_lines(self):
        return self.long
    def get_nb_column(self):
        return self.haut
    
    
    ## DISPLAY
    def print_grille(self):
        for elem in self.gril:
            print (elem)
            
            
    def print_dim(self):
        print(self.long)
        print(self.haut)