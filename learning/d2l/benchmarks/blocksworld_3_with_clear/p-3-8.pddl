

(define (problem BW-rand-3)
(:domain blocksworld)
(:objects b1 b2 b3  - block)
(:init
(on-table b1)
(on b2 b3)
(on b3 b1)
(clear b2)
)
(:goal
(and
(on b1 b2)
(on b3 b1)
(clear b3))
)
)


