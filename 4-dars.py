from collections import namedtuple

User= namedtuple('User',['name','age','location'])


def get_user():
    return [
        User('Boburjon',25,'Fergana'),
        User('Murodjon',26,'Namangan'),
        User('Javohir', 19,'Mars')
    ]
    
for i in get_user():
    print(f"{i[0]} is {i.age} years old from {i.location}")