class bcolors:
    GREEN = '\033[92m'
    Orange = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def get_colored_string(string, color):
    return color + string + bcolors.ENDC

#region Figures
class Figure:
    '''@param owner : char, 'w' for white, 'b' for black
    '''
    owner = None
    def __init__(self, owner):
        self.owner= owner
    
    def to_owner_color(self, string):
        if self.owner=="w":
            return get_colored_string(string, bcolors.CYAN)
        if self.owner=="b":
            return get_colored_string(string, bcolors.Orange)
    
    def __str__(self):
        return "?"
    

class King(Figure) :
    def __str__(self):
        return self.to_owner_color("K")

class Queen(Figure) :
    def __str__(self):
        return self.to_owner_color("Q")

class Rock(Figure) :
    def __str__(self):
        return self.to_owner_color("R")

class BishHop(Figure) :
    def __str__(self):
        return self.to_owner_color("B")

class Knight(Figure):
    def __str__(self):
        return self.to_owner_color("H")

class Pawn(Figure):
    def __str__(self):
        return self.to_owner_color("P")

#endregion 




class ChessBoard:
    _emty_field = " "
    __field= None
    __field=([Rock("b"),Knight("b"),BishHop("b"),King("b"),Queen("b"),BishHop("b"),Knight("b"),Rock("b")],
            [Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b"),Pawn("b")],
            [" "," "," "," "," "," "," "," ",],
            [" "," "," "," "," "," "," "," ",],
            [" "," "," "," "," "," "," "," ",],
            [" "," "," "," "," "," "," "," ",],
            [" "," "," "," "," "," "," "," ",],
            [Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w"),Pawn("w")],
            [Rock("w"),Knight("w"),BishHop("w"),King("w"),Queen("w"),BishHop("w"),Knight("w"),Rock("w")])



    def to_string(self):
        field_string = "\033[92m" #green coloured text

        # add letters top
        letters = ["a","b","c","d","e","f","g","h"]
        field_string+= "".ljust(3, " ") # add "blanks" offset
        for letter in letters:
            field_string += "|"+letter+"|"
        field_string += "\n" + "\033[0m" #end green coloured string 


        row_count=0
        for row in self.__field:
            #add line number begin
            field_string+= "\033[92m" +"|"+ str(row_count)+"|"+"\033[0m" #green coloured text
            row_count+=1
            for cell in row:
                field_string+="["+ str(cell) +"]"
            #add line number end
            field_string+= "\033[92m" +"|"+ str(row_count)+"|"+"\033[0m" +"\n"  #green coloured text

        # add letters botom
        field_string += "\033[92m" #green coloured text
        field_string+= "".ljust(3, " ") # add "blanks" offset
        for letter in letters:
            field_string += "|"+letter+"|"
        field_string += "\n" + "\033[0m" #end green coloured string 

        return field_string

