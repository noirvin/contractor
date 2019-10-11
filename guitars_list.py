from pymongo import MongoClient
from bson.objectid import ObjectId

guitar1 = {
    "name": "Ibanez Classic 8 String Electric",
    "picture": "https://d1aeri3ty3izns.cloudfront.net/media/9/97596/1200/preview.jpg"
}

guitar2 = {
    "name": "Fender Jazz bass",
    "picture": "https://c1.zzounds.com/media/productmedia/fit,2018by3200/quality,85/1_Full_Straight_Front_NA-ebe33aaa84cb4977b95d8564d26e6873.jpg"

}

guitar3 = {
    "name": "Fender Stratocaster Electric",
    "picture": "https://c1.zzounds.com/media/productmedia/fit,2018by3200/quality,85/1_Full_Straight_Front_NA-1acd70721653c936c044a6bfd12b2049.jpg"

}

guitar4 = {
    "name": "Francisco Navarro Flamenco Guitar",
    "picture": "https://www.guitarsalon.com/productimages/resized/1568ecea3c84cde36dc91fad5f01abd2-1318439971-large.jpg"

}

guitar5 = {
    "name": "Gibson Hummingbird 12 String Acoustic Electric",
    "picture": "https://c1.zzounds.com/media/productmedia/fit,2018by3200/quality,85/1_Full_Straight_Front_37974-01d3f57efa753ae2f5721cec5c055ff2.jpg"

}

guitar6 = {
    "name": "Fender Jimi Hendrix Stratocaster Electric",
    "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0KxMlwUx2rJFXocWmY1E4syx7_uF01ELBEDt6dynr8-lCKLJKBw"

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

    def show_guitars(self):
        self.guitars.delete_many({})

        self.guitars.insert_many(guitars_list)

        for i in self.guitars.find():
            print(guitars_list)
