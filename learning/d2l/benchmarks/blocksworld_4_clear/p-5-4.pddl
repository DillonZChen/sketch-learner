

(define (problem BW-rand-5)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5 )
(:init
(arm-empty)
(on-table b1)
(on-table b2)
(on b3 b2)
(on b4 b3)
(on b5 b1)
(clear b4)
(clear b5)
)
(:goal
(and
(clear b1))
)
)


