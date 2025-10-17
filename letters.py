"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle

from polygon import circle, arc

# LEVEL 0 PRIMITIVES 
# fd, bk, lt, rt, pu, pd

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()


# LEVEL 1 PRIMITIVES are simple combinations of Level 0 primitives.
# They have no pre- or post-conditions.

def fdlt(t, n, angle=90):
    """forward and left"""
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    """forward and back, ending at the original position"""
    fd(t, n)
    bk(t, n)

def skip(t, n):
    """lift the pen and move"""
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    """Makes a vertical line and leave the turtle at the top, facing right"""
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    """move the turtle vertically and leave it at the top, facing right"""
    lt(t)
    skip(t, n)
    rt(t)


# LEVEL 2 PRIMITIVES use primitives from Levels 0 and 1
# to draw posts (vertical elements) and beams (horizontal elements)
# Level 2 primitives ALWAYS return the turtle to the original
# location and direction.

def post(t, n):
    """Makes a vertical line and return to the original position"""
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Makes a horizontal line at the given height and return."""
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def hangman(t, n, height):
    """Makes a vertical line to the given height and a horizontal line
    at the given height and then return.
    This is efficient to implement, and turns out to be useful, but
    it's not so semantically clean."""
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t, x, y):
    """Makes a diagonal line to the given x, y offsets and return"""
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """Makes a bump with radius n at height*n 
    """
    stump(t, n*height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)


"""
The letter-drawing functions all have the precondition
that the turtle is in the lower-left corner of the letter,
and postcondition that the turtle is in the lower-right
corner, facing in the direction it started in.

They all take a turtle as the first argument and a size (n)
as the second.  Most letters are (n) units wide and (2n) units
high.

"""

def draw_upper_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_lower_a(t, n):
    lt(t)
    skip(t, 3*n/4)
    arc(t, n/4, -180)
    fd(t, n/2)
    arc(t, n/4, -360)
    fd(t, n/4)
    lt(t)
    pass

def draw_upper_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_upper_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_upper_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_upper_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_upper_e(t, n):
    draw_upper_ef(t, n)
    fd(t, n)

def draw_lower_e(t, n): 
    lt(t)
    skip(t, n*3/8)
    rt(t)
    fdlt(t, n*3/4)
    arc(t, n*3/8, 315)
    pu(t)
    arc(t, n*3/8, 45)
    rt(t)
    pd(t)
    rt(t)
    skip(t, n*3/8)
    lt(t)
    pass

def draw_upper_f(t, n):
    draw_upper_ef(t, n)
    skip(t, n)

def draw_upper_g(t, n):
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_upper_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_upper_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_upper_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    fd(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_upper_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_upper_l(t, n):
    post(t, 2*n)
    fd(t, n)

def draw_upper_m(t, n):
    post(t, 2*n)
    draw_upper_v(t, n)
    post(t, 2*n)

def draw_lower_m(t, n):
    # TODO: smooth the peaks
    draw_upper_m(t, n/2)

def draw_upper_n(t, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_upper_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_upper_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_upper_q(t, n):
    draw_upper_o(t, n)
    diagonal(t, -n/2, n)

def draw_upper_r(t, n):
    draw_upper_p(t, n)
    diagonal(t, -n/2, n)

def draw_upper_s(t, n):
    fd(t, n/2)
    arc(t, n/2, 180)
    arc(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_lower_s(t, n):
    draw_upper_s(t, n/2)

def draw_upper_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_upper_u(t, n):
    post(t, 2*n)
    fd(t, n)
    post(t, 2*n)

def draw_upper_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_upper_w(t, n):
    draw_upper_v(t, n)
    draw_upper_v(t, n)

def draw_upper_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_upper_v(t, n):
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_upper_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_upper_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def draw_(t, n):
    # draw a space
    skip(t, n)

TURTLE_UPPERCASE = {
    'A': draw_upper_a,
    'B': draw_upper_b,
    'C': draw_upper_c,
    'D': draw_upper_d,
    'E': draw_upper_e,
    # 'EF': draw_upper_ef, 
    'F': draw_upper_f,
    'G': draw_upper_g,
    'H': draw_upper_h,
    'I': draw_upper_i,
    'J': draw_upper_j,
    'K': draw_upper_k,
    'L': draw_upper_l,
    'M': draw_upper_m,
    'N': draw_upper_n,
    'O': draw_upper_o,
    'P': draw_upper_p,
    'Q': draw_upper_q,
    'R': draw_upper_r,
    'S': draw_upper_s,
    'T': draw_upper_t,
    'U': draw_upper_u,
    'V': draw_upper_v,
    'W': draw_upper_w,
    'X': draw_upper_x,
    'Y': draw_upper_y,
    'Z': draw_upper_z,
}

TURTLE_LOWERCASE = {
    'a': draw_lower_a,
    # 'b': draw_lower_b,
    # 'c': draw_lower_c,
    # 'd': draw_lower_d,
    'e': draw_lower_e,
    # 'ef': draw_lower_ef,
    # 'f': draw_lower_f,
    # 'g': draw_lower_g,
    # 'h': draw_lower_h,
    # 'i': draw_lower_i,
    # 'j': draw_lower_j,
    # 'k': draw_lower_k,
    # 'l': draw_lower_l,
    'm': draw_lower_m,
    # 'n': draw_lower_n,
    # 'o': draw_lower_o,
    # 'p': draw_lower_p,
    # 'q': draw_lower_q,
    # 'r': draw_lower_r,
    's': draw_lower_s,
    # 't': draw_lower_t,
    # 'u': draw_lower_u,
    # 'v': draw_lower_v,
    # 'w': draw_lower_w,
    # 'x': draw_lower_x,
    # 'y': draw_lower_y,
    # 'z': draw_lower_z,
}

TURTLE_ALPHABET = { ' ': draw_ }
TURTLE_ALPHABET.update(TURTLE_LOWERCASE)
TURTLE_ALPHABET.update(TURTLE_UPPERCASE)

def draw_str(str, turtle, size):
    for chr in str:
        TURTLE_ALPHABET[chr](turtle, size)
        skip(turtle, size)

if __name__ == '__main__':

    # create and position the turtle
    size = 20
    bob = turtle.Turtle()

    draw_str("James", bob, size)
    # draw_str('ee', bob, size)
    # draw_str('aa', bob, 20)
    

    # draw_str(TURTLE_ALPHABET.keys(), bob, size)
    # draw_str("JAMES", bob, size)
    # draw_upper_hello = [draw_upper_h, draw_upper_e, draw_upper_l, draw_upper_l, draw_upper_o]
    # draw_e_ef_f = [draw_upper_e, draw_upper_ef, draw_upper_f]
    # draw_e_f = [draw_upper_e, draw_upper_f]
    # draw_ef = [draw_upper_ef]
    # draw = draw_ef
    # for f in draw:
    #     f(bob, size)
    #     skip(bob, size)
    # draw_str("HELLO", bob, size)



    turtle.mainloop()
