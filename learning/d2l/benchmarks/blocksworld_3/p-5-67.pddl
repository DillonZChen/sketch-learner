

(define (problem BW-rand-5)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5  - block)
(:init
(on-table b1)
(on b2 b3)
(on b3 b5)
(on b4 b2)
(on-table b5)
(clear b1)
(clear b4)
)
(:goal
(and
(on b1 b2)
(on b2 b3)
(on b3 b4)
(on b5 b1))
)
)


