class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of all pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Adds an owner to a pet after validating that pet is an instance of Pet."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of the Pet class")
        pet.owner = self  

    def get_sorted_pets(self):
        """Returns a list of this owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"pet_type must be one of {self.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = None 

        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of the Owner class")
            self.owner = owner  

        Pet.all.append(self)  
