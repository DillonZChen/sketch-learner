

(define (problem BW-rand-5)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5  - block)
(:init
(on-table b1)
(on b2 b1)
(on b3 b2)
(on-table b4)
(on-table b5)
(clear b3)
(clear b4)
(clear b5)
)
(:goal
(and
(on b2 b5)
(on b3 b2)
(on b4 b1)
(clear b3)
(clear b4))
)
)


