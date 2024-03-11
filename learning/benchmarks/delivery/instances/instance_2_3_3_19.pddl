
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Instance file automatically generated by the Tarski FSTRIPS writer
;;; 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (problem delivery-2x3-3)
    (:domain delivery)

    (:objects
        c_0_0 c_0_1 c_0_2 c_1_0 c_1_1 c_1_2 - cell
        p1 p2 p3 - package
        t1 - truck
    )

    (:init
        (adjacent c_1_2 c_0_2)
        (adjacent c_1_0 c_0_0)
        (adjacent c_0_1 c_0_2)
        (adjacent c_0_2 c_1_2)
        (adjacent c_0_0 c_0_1)
        (adjacent c_0_2 c_0_1)
        (adjacent c_1_2 c_1_1)
        (adjacent c_0_1 c_1_1)
        (adjacent c_0_0 c_1_0)
        (adjacent c_0_1 c_0_0)
        (adjacent c_1_1 c_0_1)
        (adjacent c_1_1 c_1_2)
        (adjacent c_1_0 c_1_1)
        (adjacent c_1_1 c_1_0)
        (at p1 c_1_0)
        (at p2 c_0_1)
        (at t1 c_0_1)
        (at p3 c_1_2)
        (empty t1)
    )

    (:goal
        (and (at p1 c_1_1) (at p2 c_1_1) (at p3 c_1_1))
    )

    
    
    
)
