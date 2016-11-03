# -*- coding: utf-8 -*-
import random

while True:
    stevilka=list(range(int(raw_input("Vnesite stevilko: "))))
    random.shuffle(stevilka)
    print (stevilka)

    odgovor = raw_input("Zelite novo serijo stevilk? da/ne ")

    if odgovor == "da":
        continue
    else:
        print "Hvala"
        break

