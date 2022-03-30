(define (problem BLOCKS-5-0)
(:domain blocksworld-atomic)
(:objects a b c d)

(:init
    (on d table)
    (on a b)
    (on b c)
    (on c table)
    (clear table)
    (clear a)
    (clear d)

;; import itertools
;; _ = [print(f"(diff {b1} {b2})") for b1, b2 in itertools.permutations(['table'] + 'a b c d'.split(), 2)]
    (diff table a)
    (diff table b)
    (diff table c)
    (diff table d)
    (diff a table)
    (diff a b)
    (diff a c)
    (diff a d)
    (diff b table)
    (diff b a)
    (diff b c)
    (diff b d)
    (diff c table)
    (diff c a)
    (diff c b)
    (diff c d)
    (diff d table)
    (diff d a)
    (diff d b)
    (diff d c)
)

; unstack tower and directly build reversed tower on another block
(:goal (and
	(on a d)
    (on b a)
    (on c b)
    (on d table)
))






)