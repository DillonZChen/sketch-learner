;; blocks=25, percentage_new_tower=0, out_folder=., instance_id=5, seed=0

(define (problem blocksworld-05)
 (:domain blocksworld)
 (:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 b25 - object)
 (:init 
    (clear b4)
    (on b4 b9)
    (on b9 b18)
    (on b18 b20)
    (on b20 b23)
    (on b23 b11)
    (on b11 b3)
    (on b3 b21)
    (on b21 b2)
    (on b2 b1)
    (on b1 b24)
    (on b24 b10)
    (on b10 b8)
    (on b8 b22)
    (on b22 b15)
    (on b15 b12)
    (on b12 b16)
    (on b16 b17)
    (on b17 b6)
    (on b6 b25)
    (on b25 b14)
    (on b14 b19)
    (on b19 b13)
    (on b13 b7)
    (on b7 b5)
    (on-table b5))
 (:goal  (and 
    (clear b12)
    (on b12 b15)
    (on b15 b9)
    (on b9 b21)
    (on b21 b7)
    (on b7 b23)
    (on b23 b14)
    (on b14 b18)
    (on b18 b8)
    (on b8 b19)
    (on b19 b6)
    (on b6 b1)
    (on b1 b2)
    (on b2 b4)
    (on b4 b17)
    (on b17 b22)
    (on b22 b20)
    (on b20 b11)
    (on b11 b25)
    (on b25 b24)
    (on b24 b16)
    (on b16 b3)
    (on b3 b10)
    (on b10 b13)
    (on b13 b5)
    (on-table b5))))