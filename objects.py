


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def display_product_details(self):
        return f"Buy {self.name} today with only {self.price} Ksh with {self.description}."
     


product = Product("widget",50.0,"high quality")
print(product.display_product_details())



class Customer:
    def __init__(self, name, email, location, phoneNumber):
        self.name = name
        self.email = email
        self.location = location
        self.phoneNumber = phoneNumber
        self.total_purchase = 0

    def add_purchase(self, amount):
        self.total_purchase += amount

    def remove_purchase(self, amount):
        if self.total_purchase >= amount:
            self.total_purchase -= amount
        else:
            print("Error: The amount to remove exceeds the total purchase.")

    def discount(self):
        if self.total_purchase >= 100:
            return 0.1
        return 0.0


# Test the methods
customer1 = Customer("Mwangi", "mwangi@gmail.com", "Kasarani", "5234-456-987")

customer1.add_purchase(120)
print(customer1.total_purchase)  # Output: 120

customer1.remove_purchase(50)
print(customer1.total_purchase)  # Output: 70

customer1.remove_purchase(100)
print(customer1.total_purchase)  # Output: Error: The amount to remove exceeds the total purchase.

print(customer1.discount())  # Output: 0.0


 #Q1The ever changing Ankara:You are a fashion designer known for your unique and vibrant Ankara designs .
#Recently,you have discovered that some of your fabric patterns change their designs based on 
#temperature and mood of the wearer.You want to create a software application that can predict the changes ,
#in the fabric design given the mood and the temperature data.Think about the classes you will need to model,
#changing Ankara and how to predict the changes.


class Ankara:
    def __init__(self, mood, temperature):
        self.mood = mood
        self.temperature = temperature

    def predict_pattern_changes(self):
        if self.temperature >=40 and self.mood == "happy":
            return "Wear light and more patterned Ankara."
        elif self.temperature <= 40 and self.mood == "sad":
            return "Wear dull and less patterned Ankara."
        else:
            return "No change in pattern"
ankara=Ankara("happy",45)            
print(ankara.predict_pattern_changes()) 
 
#Q2

#The great migration Forecast:Every year,millions of wildebeest ,zebras and other animals participate,
#in the Great Migration across the serengeti_mara ecosystem .As a conservationist,you want to develop a
#software system that models this migration ,predicting the movement of the herds based on weather 
#patterns ,river levels and predator location.Consider what classes you will need to represent the 
#animals ,the environment and the various factors that influence the migration.

class Animal:
    def __init__(self, species, name, current_location):
        self.species = species
        self.name = name
        self.current_location = current_location

    def migrate(self, next_location):
        print(f"The {self.name}, one of the {self.species}, is migrating from {self.current_location} to {next_location}.")


class Environment:
    def __init__(self, weather, river, predators):
        self.weather = weather
        self.river = river
        self.predators = predators

    def check_conditions(self):
        if self.weather == "Sunny" and self.river == "Low" and not self.predators:
            return "Migration possible"
        else:
            return "No migration"


animal = Animal("panthera leo", "lion", "South")
animal.migrate("North")

env = Environment("Sunny", "Low", False)
print(env.check_conditions())



#The Magical Baobab:In a small village,there is a Baobab tree believed to have magical properties .
#Every season ,it bears different types of fruits,each with its own unique power.You've decided to 
#create a software system that tracks the changes in the tree and predict what type of fruit will bear 
#next season and what powers it will possess.The system should also record the effect of each fruit 
#when consumed.

class Possible_fruits:
    def __init__(self,powers,name,effects,season):
        self.powers=powers
        self.name=name
        self.effects=effects
        self.season=season
fruit1=Possible_fruits("strength","baobab","healthy","dry")       
fruit2=Possible_fruits("Health","mango","strong","wet") 
empty_list=[]
empty_list.extend([fruit1,fruit2])

class Season:
    def __init__(self,season):
        self.season=season
    def predict_fruit(self):
     list_of_fruits=[fruit for fruit in empty_list if fruit.season == self.season] 
     for fruit in list_of_fruits :
        print(f"{fruit.name},{fruit.season},{fruit.effects},{fruit.powers}" )
season1=Season("dry")  
season1.predict_fruit()  

#The legendary african drum circles:You are part of community that hosts one of the largest drum circles 
#in Africa .There are different types of traditional drums used in circles,each with unuque sound and
#rhythm.The Djembe,Talking_drum and Bougarabou are among the popular ones.THese drums have common 
#properties such as material they are made from and their sizes,but they are also have distinct x-tics.
#For instance,the Talking_drum can mimicthe lines of human speech ,the Djembeis known for its wide range
#of tones ,and the Bougarabou is noted for its deep ,rich bass tones.

#You want to create a software model of the drum circles that encapsulates these different types of drums.
#You wish to include methods of each drum that represent the sound it makess and also group similar drums
#together .Think about creating a base Drum class that contain properties and methods common to all drums 
#and the create sub classes for each specific type of drum (like Djembe,Talking_drum and Bougarabou).

#The sub classes should inherit from the base Drum class and also implement their unique characteristics 
#This software model would help newcomers understand characteristics of each drum and how they contribute
#to the overall rhythm of the drum circle.

class Drum:
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def make_sound(self):    
        print(f"{self.__class__.__name__}:{self.sound}") 


class Djembe(Drum):
    sound="wide range of tones"
class Talking_drum(Drum):
    sound="mimic lines of human speech"   
class Bougarabou(Drum):
    sound="deep,rich,bass,tone"   


Drum1=Djembe("skin","large")
Drum1.make_sound()

Drum2=Talking_drum("metalic","small")
Drum2.make_sound()


#The Magical Baobab:In a small village,there is a Baobab tree believed to have magical properties .
#Every season ,it bears different types of fruits,each with its own unique power.You've decided to 
#create a software system that tracks the changes in the tree and predict what type of fruit will bear 
#next season and what powers it will possess.The system should also record the effect of each fruit 
#when consumed.










