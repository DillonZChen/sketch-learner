;; blocks=1, percentage_new_tower=10, out_folder=., instance_id=16, seed=6

(define (problem blocksworld-16)
 (:domain blocksworld)
 (:objects b1 - object)
 (:init 
    (clear b1)
    (on-table b1))
 (:goal  (and 
    (clear b1)
    (on-table b1))))