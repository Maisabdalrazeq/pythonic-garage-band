from abc import abstractmethod, ABC

class Band():
    members = []
    bands = []
    
    def __init__(self,name):
        self.name=name
        Band.bands.append(self)
    
    def new_members(self,newName):
        self.newName=newName
        Band.members.append(newName)
    
    def play_solos(self):
        result =''
        for i in Band.members:
            result+= f'{i.play_solo()}\n'
        return result
    
    @classmethod 
    def to_list(cls):
        return cls.members

    def __str__(self):
        return f"Band <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "

class Musician():
    
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def __str__(self):
        return f"Musician <{self.name}>"
    
    @abstractmethod
    def __repr__(self):
        return f" '{self.name}' "
    
    def play_solo(self):
        return f'{self.name} Play solo'

class Guitarist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"Guitarist <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "
    
    def get_instrument(self):
        return 'Guitarist'

class Bassist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"Bassist <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "
    
    def get_instrument(self):
        return 'Bassist'

class Drummer(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"Drummer <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "
    
    def get_instrument(self):
        return 'Drummer'

if __name__ == "__main__":
    mais = Guitarist('Mais')
    bashar=Drummer('Bashar')
    diana = Bassist('Diana')
    print(mais)
    print(mais.get_instrument())
    print(bashar)
    print(diana)
    print(diana.get_instrument())
    print(mais.play_solo())
    print(diana.play_solo())
    autostrad = Band('Autostrad')
    autostrad.new_members(mais)
    autostrad.new_members(bashar)
    autostrad.new_members(diana)
    print(autostrad.bands)
    print(autostrad.__str__())
    print(autostrad.to_list())
    print(autostrad.play_solos())