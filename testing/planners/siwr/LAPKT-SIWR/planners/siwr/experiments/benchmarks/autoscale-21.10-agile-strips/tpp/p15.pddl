; Domain designed by Alfonso Gerevini and Alessandro Saetti
; This file has been automatically generated by the generator available from
; http://zeus.ing.unibs.it/ipc-5/generators/index.html

(define (problem TPP)
(:domain TPP-Propositional)
(:objects
	goods1 goods2 goods3 goods4 goods5 goods6 goods7 goods8 goods9 goods10 goods11 goods12 goods13 goods14 goods15 goods16 - goods
	truck1 truck2 truck3 truck4 truck5 truck6 truck7 - truck
	market1 market2 market3 - market
	depot1 depot2 depot3 depot4 depot5 depot6 depot7 depot8 depot9 depot10 depot11 depot12 depot13 depot14 depot15 depot16 depot17 depot18 depot19 depot20 depot21 depot22 depot23 depot24 depot25 depot26 depot27 depot28 depot29 depot30 depot31 - depot
	level0 level1 level2 level3 level4 level5 level6 level7 level8 level9 - level)

(:init
	(next level1 level0)
	(next level2 level1)
	(next level3 level2)
	(next level4 level3)
	(next level5 level4)
	(next level6 level5)
	(next level7 level6)
	(next level8 level7)
	(next level9 level8)
	(ready-to-load goods1 market1 level0)
	(ready-to-load goods1 market2 level0)
	(ready-to-load goods1 market3 level0)
	(ready-to-load goods2 market1 level0)
	(ready-to-load goods2 market2 level0)
	(ready-to-load goods2 market3 level0)
	(ready-to-load goods3 market1 level0)
	(ready-to-load goods3 market2 level0)
	(ready-to-load goods3 market3 level0)
	(ready-to-load goods4 market1 level0)
	(ready-to-load goods4 market2 level0)
	(ready-to-load goods4 market3 level0)
	(ready-to-load goods5 market1 level0)
	(ready-to-load goods5 market2 level0)
	(ready-to-load goods5 market3 level0)
	(ready-to-load goods6 market1 level0)
	(ready-to-load goods6 market2 level0)
	(ready-to-load goods6 market3 level0)
	(ready-to-load goods7 market1 level0)
	(ready-to-load goods7 market2 level0)
	(ready-to-load goods7 market3 level0)
	(ready-to-load goods8 market1 level0)
	(ready-to-load goods8 market2 level0)
	(ready-to-load goods8 market3 level0)
	(ready-to-load goods9 market1 level0)
	(ready-to-load goods9 market2 level0)
	(ready-to-load goods9 market3 level0)
	(ready-to-load goods10 market1 level0)
	(ready-to-load goods10 market2 level0)
	(ready-to-load goods10 market3 level0)
	(ready-to-load goods11 market1 level0)
	(ready-to-load goods11 market2 level0)
	(ready-to-load goods11 market3 level0)
	(ready-to-load goods12 market1 level0)
	(ready-to-load goods12 market2 level0)
	(ready-to-load goods12 market3 level0)
	(ready-to-load goods13 market1 level0)
	(ready-to-load goods13 market2 level0)
	(ready-to-load goods13 market3 level0)
	(ready-to-load goods14 market1 level0)
	(ready-to-load goods14 market2 level0)
	(ready-to-load goods14 market3 level0)
	(ready-to-load goods15 market1 level0)
	(ready-to-load goods15 market2 level0)
	(ready-to-load goods15 market3 level0)
	(ready-to-load goods16 market1 level0)
	(ready-to-load goods16 market2 level0)
	(ready-to-load goods16 market3 level0)
	(stored goods1 level0)
	(stored goods2 level0)
	(stored goods3 level0)
	(stored goods4 level0)
	(stored goods5 level0)
	(stored goods6 level0)
	(stored goods7 level0)
	(stored goods8 level0)
	(stored goods9 level0)
	(stored goods10 level0)
	(stored goods11 level0)
	(stored goods12 level0)
	(stored goods13 level0)
	(stored goods14 level0)
	(stored goods15 level0)
	(stored goods16 level0)
	(loaded goods1 truck1 level0)
	(loaded goods1 truck2 level0)
	(loaded goods1 truck3 level0)
	(loaded goods1 truck4 level0)
	(loaded goods1 truck5 level0)
	(loaded goods1 truck6 level0)
	(loaded goods1 truck7 level0)
	(loaded goods2 truck1 level0)
	(loaded goods2 truck2 level0)
	(loaded goods2 truck3 level0)
	(loaded goods2 truck4 level0)
	(loaded goods2 truck5 level0)
	(loaded goods2 truck6 level0)
	(loaded goods2 truck7 level0)
	(loaded goods3 truck1 level0)
	(loaded goods3 truck2 level0)
	(loaded goods3 truck3 level0)
	(loaded goods3 truck4 level0)
	(loaded goods3 truck5 level0)
	(loaded goods3 truck6 level0)
	(loaded goods3 truck7 level0)
	(loaded goods4 truck1 level0)
	(loaded goods4 truck2 level0)
	(loaded goods4 truck3 level0)
	(loaded goods4 truck4 level0)
	(loaded goods4 truck5 level0)
	(loaded goods4 truck6 level0)
	(loaded goods4 truck7 level0)
	(loaded goods5 truck1 level0)
	(loaded goods5 truck2 level0)
	(loaded goods5 truck3 level0)
	(loaded goods5 truck4 level0)
	(loaded goods5 truck5 level0)
	(loaded goods5 truck6 level0)
	(loaded goods5 truck7 level0)
	(loaded goods6 truck1 level0)
	(loaded goods6 truck2 level0)
	(loaded goods6 truck3 level0)
	(loaded goods6 truck4 level0)
	(loaded goods6 truck5 level0)
	(loaded goods6 truck6 level0)
	(loaded goods6 truck7 level0)
	(loaded goods7 truck1 level0)
	(loaded goods7 truck2 level0)
	(loaded goods7 truck3 level0)
	(loaded goods7 truck4 level0)
	(loaded goods7 truck5 level0)
	(loaded goods7 truck6 level0)
	(loaded goods7 truck7 level0)
	(loaded goods8 truck1 level0)
	(loaded goods8 truck2 level0)
	(loaded goods8 truck3 level0)
	(loaded goods8 truck4 level0)
	(loaded goods8 truck5 level0)
	(loaded goods8 truck6 level0)
	(loaded goods8 truck7 level0)
	(loaded goods9 truck1 level0)
	(loaded goods9 truck2 level0)
	(loaded goods9 truck3 level0)
	(loaded goods9 truck4 level0)
	(loaded goods9 truck5 level0)
	(loaded goods9 truck6 level0)
	(loaded goods9 truck7 level0)
	(loaded goods10 truck1 level0)
	(loaded goods10 truck2 level0)
	(loaded goods10 truck3 level0)
	(loaded goods10 truck4 level0)
	(loaded goods10 truck5 level0)
	(loaded goods10 truck6 level0)
	(loaded goods10 truck7 level0)
	(loaded goods11 truck1 level0)
	(loaded goods11 truck2 level0)
	(loaded goods11 truck3 level0)
	(loaded goods11 truck4 level0)
	(loaded goods11 truck5 level0)
	(loaded goods11 truck6 level0)
	(loaded goods11 truck7 level0)
	(loaded goods12 truck1 level0)
	(loaded goods12 truck2 level0)
	(loaded goods12 truck3 level0)
	(loaded goods12 truck4 level0)
	(loaded goods12 truck5 level0)
	(loaded goods12 truck6 level0)
	(loaded goods12 truck7 level0)
	(loaded goods13 truck1 level0)
	(loaded goods13 truck2 level0)
	(loaded goods13 truck3 level0)
	(loaded goods13 truck4 level0)
	(loaded goods13 truck5 level0)
	(loaded goods13 truck6 level0)
	(loaded goods13 truck7 level0)
	(loaded goods14 truck1 level0)
	(loaded goods14 truck2 level0)
	(loaded goods14 truck3 level0)
	(loaded goods14 truck4 level0)
	(loaded goods14 truck5 level0)
	(loaded goods14 truck6 level0)
	(loaded goods14 truck7 level0)
	(loaded goods15 truck1 level0)
	(loaded goods15 truck2 level0)
	(loaded goods15 truck3 level0)
	(loaded goods15 truck4 level0)
	(loaded goods15 truck5 level0)
	(loaded goods15 truck6 level0)
	(loaded goods15 truck7 level0)
	(loaded goods16 truck1 level0)
	(loaded goods16 truck2 level0)
	(loaded goods16 truck3 level0)
	(loaded goods16 truck4 level0)
	(loaded goods16 truck5 level0)
	(loaded goods16 truck6 level0)
	(loaded goods16 truck7 level0)
	(connected market1 market3)
	(connected market2 market3)
	(connected market3 market1)
	(connected market3 market2)
	(connected depot1 market3)
	(connected market3 depot1)
	(connected depot2 market3)
	(connected market3 depot2)
	(connected depot3 market1)
	(connected market1 depot3)
	(connected depot4 market2)
	(connected market2 depot4)
	(connected depot5 market3)
	(connected market3 depot5)
	(connected depot6 market3)
	(connected market3 depot6)
	(connected depot7 market2)
	(connected market2 depot7)
	(connected depot8 market1)
	(connected market1 depot8)
	(connected depot9 market3)
	(connected market3 depot9)
	(connected depot10 market1)
	(connected market1 depot10)
	(connected depot11 market3)
	(connected market3 depot11)
	(connected depot12 market3)
	(connected market3 depot12)
	(connected depot13 market1)
	(connected market1 depot13)
	(connected depot14 market2)
	(connected market2 depot14)
	(connected depot15 market3)
	(connected market3 depot15)
	(connected depot16 market2)
	(connected market2 depot16)
	(connected depot17 market1)
	(connected market1 depot17)
	(connected depot18 market2)
	(connected market2 depot18)
	(connected depot19 market1)
	(connected market1 depot19)
	(connected depot20 market3)
	(connected market3 depot20)
	(connected depot21 market2)
	(connected market2 depot21)
	(connected depot22 market2)
	(connected market2 depot22)
	(connected depot23 market1)
	(connected market1 depot23)
	(connected depot24 market1)
	(connected market1 depot24)
	(connected depot25 market1)
	(connected market1 depot25)
	(connected depot26 market3)
	(connected market3 depot26)
	(connected depot27 market2)
	(connected market2 depot27)
	(connected depot28 market2)
	(connected market2 depot28)
	(connected depot29 market3)
	(connected market3 depot29)
	(connected depot30 market3)
	(connected market3 depot30)
	(connected depot31 market2)
	(connected market2 depot31)
	(on-sale goods1 market1 level6)
	(on-sale goods2 market1 level7)
	(on-sale goods3 market1 level7)
	(on-sale goods4 market1 level8)
	(on-sale goods5 market1 level0)
	(on-sale goods6 market1 level5)
	(on-sale goods7 market1 level0)
	(on-sale goods8 market1 level0)
	(on-sale goods9 market1 level0)
	(on-sale goods10 market1 level0)
	(on-sale goods11 market1 level0)
	(on-sale goods12 market1 level0)
	(on-sale goods13 market1 level7)
	(on-sale goods14 market1 level5)
	(on-sale goods15 market1 level0)
	(on-sale goods16 market1 level4)
	(on-sale goods1 market2 level0)
	(on-sale goods2 market2 level0)
	(on-sale goods3 market2 level0)
	(on-sale goods4 market2 level0)
	(on-sale goods5 market2 level1)
	(on-sale goods6 market2 level4)
	(on-sale goods7 market2 level5)
	(on-sale goods8 market2 level0)
	(on-sale goods9 market2 level0)
	(on-sale goods10 market2 level0)
	(on-sale goods11 market2 level8)
	(on-sale goods12 market2 level0)
	(on-sale goods13 market2 level2)
	(on-sale goods14 market2 level4)
	(on-sale goods15 market2 level2)
	(on-sale goods16 market2 level0)
	(on-sale goods1 market3 level3)
	(on-sale goods2 market3 level2)
	(on-sale goods3 market3 level2)
	(on-sale goods4 market3 level1)
	(on-sale goods5 market3 level6)
	(on-sale goods6 market3 level0)
	(on-sale goods7 market3 level4)
	(on-sale goods8 market3 level2)
	(on-sale goods9 market3 level8)
	(on-sale goods10 market3 level7)
	(on-sale goods11 market3 level1)
	(on-sale goods12 market3 level8)
	(on-sale goods13 market3 level0)
	(on-sale goods14 market3 level0)
	(on-sale goods15 market3 level2)
	(on-sale goods16 market3 level1)
	(at truck1 depot7)
	(at truck2 depot15)
	(at truck3 depot7)
	(at truck4 depot18)
	(at truck5 depot23)
	(at truck6 depot18)
	(at truck7 depot15))

(:goal (and
	(stored goods1 level3)
	(stored goods2 level6)
	(stored goods3 level6)
	(stored goods4 level4)
	(stored goods5 level3)
	(stored goods6 level5)
	(stored goods7 level5)
	(stored goods8 level1)
	(stored goods9 level1)
	(stored goods10 level3)
	(stored goods11 level2)
	(stored goods12 level8)
	(stored goods13 level9)
	(stored goods14 level4)
	(stored goods15 level1)
	(stored goods16 level2)))

)