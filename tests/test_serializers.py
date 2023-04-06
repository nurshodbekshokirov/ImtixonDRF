from unittest import TestCase
from asosiy.serializers import *

class SUVTESTSerializer(TestCase):
    def test_suv(self):
        suvlar = {
            "id": 1,
            "brend": "Pepsi",
            "narx": 15000,
            "litr": "1.5 litr",
            "batafsil": "Pepsi 1.5 litr suvi"
        }
        serializer = SuvSerializers(data=suvlar)
        assert serializer.is_valid() == True
    def test_mijoz(self):
        mijoz = {
            "id": 1,
            "ism": "Nurshodbek",
            "tel": "901512367",
            "manzil": "Qo'qon",
            "qarz": 0,
            "user": 1
        }
        serializer = MijozSerializers(data=mijoz)
        assert serializer.is_valid() == True

