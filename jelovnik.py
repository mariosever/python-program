#!/usr/bin/env python
# -*- coding: utf-8 -*-

#program za restaurant menu

print "Dobrodošli u MENU, što ćemo danas klopati?"

menu_dict = {}

while True:
    jelo = raw_input("Unesi novo jelo na meni: ")
    cijena = raw_input("Unesi cijenu za '%s' : " % jelo)
    print "Jelo je: " + jelo + " cijena: " + str(cijena)

    menu_dict[jelo] = cijena

    new = raw_input("Unesi novo jelo? (yes/no)")

    if new == "no":
        break

menu_file = open("menu.txt", "w+")

print "Današnji menu:"

for jelo in menu_dict:
    print "%s: %s kn" % (jelo, menu_dict[jelo])

with open("menu.txt", "w+") as menu_file:
    menu_file.write("Današnji menu:\n")
    for jelo in menu_dict:
        menu_file.write("%s: %s kn\n" % (jelo, menu_dict[jelo]))

print "Dobar tek!"












