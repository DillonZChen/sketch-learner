;; blocks=3, percentage_new_tower=40, out_folder=., instance_id=115, seed=5

(define (problem blocksworld-115)
 (:domain blocksworld)
 (:objects b1 b2 b3 - object)
 (:init 
    (clear b3)
    (on b3 b2)
    (on b2 b1)
    (on-table b1))
 (:goal  (and 
    (clear b2)
    (on-table b2)
    (clear b1)
    (on b1 b3)
    (on-table b3))))