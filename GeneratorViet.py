import random
import csv
# from gramatika.PodstatneMeno import PodstatneMeno
# from gramatika.PridavneMeno import PridavneMeno
# from gramatika.Sloveso import Sloveso
# from gramatika import * 
from gramatika.PodstatneMeno import PodstatneMeno
from gramatika.PridavneMeno import PridavneMeno
from gramatika.Sloveso import Sloveso

class GeneratorViet:
    def __init__(self):
        self._slovne_druhy_enum = [ 
            'null',
            'podstatne',
            'pridavne',
            'zameno',
            'sloveso',
            'cislovka',
            'prislovka',
            'predlozka',
            'spojka',
            'castica',
            'citoslovcia']
        
        self._slovne_druhy_methods = {
            'podstatne':PodstatneMeno,
            'pridavne':PridavneMeno,
            'zameno':3,
            'sloveso':Sloveso,
            'cislovka':5,
            'prislovka':6,
            'predlozka':7,
            'spojka':8,
            'castica':9,
            'citoslovcia':10
        }

        self._template_arr = [141]

    def getSentenceTemplate(self):
        random_index = random.randint(0,len(self._template_arr))
        return self._template_arr[random_index]
    
    def loadDB(self):
        
        words = []
        podstatne = []
        pridavne = []
        slovesa = []

        i = 1
        enum_counter = 0 # used for correct class creation according to _slovne_druhy_enum

        with open ('db.csv', mode ='r', encoding='utf-8') as file:
            csvFile = csv.reader(file)

            for line in csvFile:
                    if line:  # Ensure the row isn't empty

                        first_line_char = line[0][0]

                        if first_line_char == '#':
                            print('enum counter: '+str(enum_counter))
                            enum_counter+=1  # skips line
                            continue
                        if first_line_char == '\n':
                            continue

                        # access string from array through index 
                        sd_string = self._slovne_druhy_enum[enum_counter]

                        # access method (slovny druh constructor) through dictionary
                        method = self._slovne_druhy_methods.get(sd_string)

                        # call method - create new object 
                        if (sd_string == 'podstatne'):
                            obj = method(content=line[0], rod=line[1], vzor=line[2])
                            podstatne.append(obj)
                        
                        if (sd_string == 'pridavne'):
                            obj = method(content=line[0], vzor=line[1])
                            pridavne.append(obj)

                        if (sd_string == 'sloveso'):
                            obj = method(content=line[0])
                            print(obj.getContent())
                            slovesa.append(obj)

                        # words.append(obj)

                        if i == 100:
                            break
                        i+=1

        print(len(podstatne))
        print(len(pridavne))
        print(len(slovesa))

        # for word in words:
        #     print(word.getContent())
        #     print(word.getRod())
        #     print(word.getVzor())
        #     print()

