from peewee import SqliteDatabase, CharField, ForeignKeyField, Model

db = SqliteDatabase(':memory:')

class Person(Model):
    name = CharField()
    class Meta:
        datebase = db

class Address(Model):
    address = CharField()
    person = ForeignKeyField(Person)
    class Meta:
        datebase = db

if __name__ == "__main__":
    Person.create_table()
    Address.create_table()
    p = Person(name = "Sun")
    p.save()
    a = Address(address = "Here", person = p)
    a.save()

    person = Person.select().where(Person.name == "Sun").get()
    print("person:", person)
    print("person id: {}, person name: {}".format(person.id, person.name))
    address = Address.select().where(Address.person == person).get()
    print("address id: {}, address name: {}".format(address.id, address.address))