

(define (problem BW-rand-3)
(:domain blocksworld)
(:objects b1 b2 b3  - block)
(:init
(on b1 b2)
(on b2 b3)
(on-table b3)
(clear b1)
)
(:goal
(and
(on b3 b1)
(clear b2)
(clear b3))
)
)


