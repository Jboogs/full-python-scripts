

# parent class and attributes
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'Unknown'
    carbon_based = True
    #methods
    def information(self):
        msg = '\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\
\nCarbon Based: {}'.format(self.name, self.species, self.legs, \
                self.arms, self.dna, self.origin, self.carbon_based)
        return msg



# child class based from the class Organism()
class Human(Organism):
    name = 'Justin'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    # method
    def ingenuity(self):
        msg = '\nCreates a weapon using only a paperclip, chewing gum and a \
roll of duct tape!'
        return msg

# second child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence_b'
    origin = 'Earth'
    #method
    def wag_of_tail(self):
        msg = '\nThe dogs tail ferociously wags in every direction when his human \
walks through the door after a long day of being alone'
        return msg

# third child class
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'sequence_c'
    origin = 'mars'
    # method for bacteria
    def replication(self):
        msg = '\nThe organism begins to deivide into two different organisms \
AND SO ON, AND SO ON!!!!'
        return msg



if __name__ == '__main__':
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.wag_of_tail())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())


    
