from art import tprint
import random
import time

tprint("Welcome", "rnd-xlarge")


def monetka() -> str:
    print("Подкидываю монетку")
    Orel = """
                  ooo OOO OOO ooo
               oOO                 OOo
           oOO                         OOo
        oOO                               OOo
      oOO                                   OOo
    oOO                                       OOo
   oOO                                         OOo
  oOO                  ____     _____           OOo
 oOO                 /  \  _.-'_.-'              OOo
 oOO                 \  _\/   _/                  OOo
 oOO               ___)/   __<                    OOo
 oOO             <'-;:\_  _\                      OOo
 oOO                 '; \_\                      OOo
  oOO                 >/-,\                     OOo
   oOO              ""`  |_\                   OOo
    oOO                                       OOo
      oOO                                   OOo
        oO                                OOo
           oOO                         OOo
               oOO                 OOo
                   ooo OOO OOO ooo

               Вам выпал Орёл!!!!!!!!"""

    Reshka = """                   ooo OOO OOO ooo
               oOO                 OOo
           oOO                         OOo
        oOO                               OOo
      oOO                                   OOo
    oOO                                       OOo
   oOO                                         OOo
  oOO                  _$$$$$$                  OOo
 oOO                   _$$____                   OOo
 oOO                   _$$____                   OOo
 oOO                   _$$$$$_                   OOo
 oOO                   _$$__$$                   OOo
 oOO                   _____$$                   OOo
  oOO                  _____$$                  OOo
   oOO                 _$$__$$                 OOo
    oOO                __$$$$_                OOo
      oOO                                   OOo
        oO                                OOo
           oOO                         OOo
               oOO                 OOo
                   ooo OOO OOO ooo

                Вам выпала Решка!!!!!"""
    if random.randint(0, 1) == 1:
        return Orel
    else:
        return Reshka


input("Подбросим монетку? Жми ENTER!  ")
for i in range(5):
    print("")
    time.sleep(1)
print(monetka())
