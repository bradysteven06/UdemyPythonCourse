

class Dog:

    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


if __name__ == '__main__':

    sam = Dog(breed='Lab', name='Sam')
    frank = Dog(breed='Huskie', name='Frank')

    print(f'{sam.name} is a {sam.breed}')
    print(sam.species)
    print(f'{frank.name} is a {frank.breed}')

