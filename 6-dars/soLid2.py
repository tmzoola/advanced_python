
class Database:
    
    def create(self):
        print("I can create")
        
    def save(self):
        print("I can create")
        
    def jointable(self):
        print("I can join tables")
        
class Postgres(Database):
    pass

class MongoDb(Database):
    pass


postgres = Postgres()
mongodb = MongoDb()

postgres.jointable()
mongodb.jointable()



# dog = Creature( "Reks", 5)
# cat = Creature("Kisa", 2)
# hen = Creature("noname", 4)
# horse = Creature("Olov", 8)


# arributes = (dog, cat, hen, horse)

# for i in arributes:
#     print(i.value["name"])
