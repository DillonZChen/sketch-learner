

(define (problem BW-rand-4)
(:domain blocksworld)
(:objects b1 b2 b3 b4  - block)
(:init
(on b1 b4)
(on b2 b3)
(on b3 b1)
(on-table b4)
(clear b2)
)
(:goal
(and
(on b2 b4)
(on b3 b2)
(clear b1)
(clear b3))
)
)


