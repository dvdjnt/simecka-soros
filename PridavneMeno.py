from Slovo import Slovo

class PridavneMeno(Slovo):
    def __init__(self,content,vzor,special=None, sklonovanie_array=None):
        super().__init__(content)
        self._vzor = vzor
    
    def getVzor(self):
        return self._vzor

    def transform(self, rod, cislo):
        vzor = self.getVzor()
        slovo = self.getContent()

        if vzor == 'pekny':
            return self.pekny(rod, cislo)
        elif vzor == 'cudzi':
            return self.cudzi(rod, cislo)
        else:
            return 0
            
    def pekny(self, rod, cislo):

        string = self.getContent()[:-1]
        char = ''

        if cislo == 'sg':
            if rod == 'm':
                char = ''
            if rod == 'z':
                char = 'a'
            if rod == 's':
                char = 'e'
        elif cislo == 'pl':
            if rod == 'm':
                char = ''
            if rod == 'z':
                char = 'e'
            if rod == 's':
                char = 'e'
        
        return string+char
    
    def cudzi(self, rod, cislo):
        
        string = self.getContent()
        char = ''

        if cislo == 'sg':
            if rod == 'm':
                char = ''
            if rod == 'z':
                char = 'a'
            if rod == 's':
                char = 'e'
        elif cislo == 'pl':
            if rod == 'm':
                char = 'i'
            else:
                char = 'e'


        return string+char