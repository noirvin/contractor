from pymongo import MongoClient
from bson.objectid import ObjectId

guitar1 = {
    "name": "Ibanez Classic 8 String Electric",
    "picture": "/static/Ibanez8string.jpg",
}

guitar2 = {
    "name": "Fender Jazz bass",
    "picture": "/static/fender-jazz-bass.jpg"

}

guitar3 = {
    "name": "Fender Stratocaster Electric"
    "picture": "/static/fenderStratElectric.jpg"

}

guitar4 = {
    "name": "Francisco Navarro Flamenco Guitar"
    "picture": "/static/FranciscoNavarroFlamenco.webp"

}

guitar5 = {
    "name": "Gibson Hummingbird 12 String Acoustic Electric"
    "picture": "/static/GibsonHumming12.jpg"

}

guitar6 = {
    "name": "Fender Jimi Hendrix Stratocaster Electric"

}

guitars_list = [
    guitar1,
    guitar2,
    guitar3,
    guitar4,
    guitar5,
    guitar6

]
class Slap_Store():
    def __init__(self, guitars):
        self.guitars = guitars

    def show_inventory(self):
        self.guitars.delete_many({})

        self.guitars.insert_many(guitars_list)

        for i in self.guitars.find():
            print(guitars_list)
