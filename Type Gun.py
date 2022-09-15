class Gun:
    def __init__(self,name,size,caliber,ammo):
        self.name = name
        self.size = size
        self.caliber = caliber
        self.ammo = ammo

KIMBER1 = Gun('KIMBER K6 Classic Engraved',.357,2,6)
KIMBER2 = Gun('KIMBER K6S Stainless',.357,3,6)
KIMBER3 = Gun('KIMBER K6S (DASA)',357,2,6)

print(KIMBER3.name)
