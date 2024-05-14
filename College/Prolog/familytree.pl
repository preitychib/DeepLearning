gender(a, male).
gender(b, female).
gender(c, male).
gender(d, female).
gender(e, male).
gender(f, female).
gender(g, male).
gender(h, female).

parent(a, c).
parent(b, c).
parent(a, d).
parent(b, d).
parent(c, e).
parent(d, e).
parent(c, f).
parent(d, f).
parent(e, g).
parent(f, h).

ancestor(Ancestor, Descendant) :- parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :- parent(Ancestor, Intermediate), ancestor(Intermediate, Descendant).

father(Father, Child) :- parent(Father, Child), gender(Father, male).
mother(Mother, Child) :- parent(Mother, Child), gender(Mother, female).

sibling(Child1, Child2) :- 
    parent(Parent, Child1), 
    parent(Parent, Child2),
    Child1 \= Child2.
