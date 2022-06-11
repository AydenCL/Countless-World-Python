#Main Styles - #1

class Flurry:

    def __init__(self, Color, Damage, Rate):

        self.Color = Color
        self.Damage = Damage
        self.Rate = Rate

    


class Ravage:

     def __init__(self, Color, Damage, Rate):

        self.Color = Color
        self.Damage = Damage
        self.Rate = Rate




class Pierce:

     def __init__(self, Color, Damage, Rate):

        self.Color = Color
        self.Damage = Damage
        self.Rate = Rate

     def TruePierce(self):
            print("Ignore damage reduction of shields")
       


#Weapon Styles - #2

class Katana(Flurry):

    def __init__(self, Color, Damage, Rate):

        Flurry.__init__(self, Color, Damage, Rate)

    def Damage(self):
        print("40 Base dmg")
   
    def Rate(self):
         print("x.75")

    def Color(self):
        print("Orange")






class Greatsword(Ravage):

    def __init__(self, Color, Damage, Rate):

        Ravage.__init__(self, Color, Damage, Rate)

    def Damage(self):
        print("60 Base dmg")
   
    def Rate(self):
         print("x1.25")

    def Color(self):
        print("Red")




class Spear(Pierce):

    def __init__(self, Color, Damage, Rate):

        Pierce.__init__(self, Color, Damage, Rate)

    def Damage(self):
        print("40 Base dmg + 10 Shield dmg")
    
    def Rate(self):
         print("x1")

    def Color(self):
        print("Yellow")

    def TruePierce(self):
        print("Ignore damage reduction of shields")
