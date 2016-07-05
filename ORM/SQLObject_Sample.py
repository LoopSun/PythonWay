from sqlobject import StringCol, SQLObject, ForeignKey, sqlhub, connectionForURI

sqlhub.processConnection = connectionForURI('sqlite:/:memory:')

class Person(SQLObject):
    name = StringCol()
    sex = StringCol()

class Address(SQLObject):
    address = StringCol()
    person = ForeignKey('Person')

if __name__ == "__main__":
    Person.createTable()
    Address.createTable()
    p = Person(name = "Sun", sex = "Male")
    a = Address(address = "Here", person = p)
