gender(a,male).
gender(b,female).
gender(c,male).
gender(d,female).
gender(e,male).
gender(f,female).
gender(h,male).
gender(g,female).
gender(i,male).
gender(j,female).
gender(k,male).
gender(l,female).
gender(mm,male).
gender(n,female).
gender(o,female).
gender(p,male).


father(a,e). 
father(c,f). 
father(e,g). 
father(h,j). 
father(h,k).
father(i,mm). 
father(i,n).
father(k,o). 
father(k,p).
mother(b,e).
mother(d,f).
mother(f,g).
mother(g,j). 
mother(g,k).
mother(j,mm). 
mother(j,n).
mother(l,o). 
mother(l,p).


parent(Par,Child) :- mother(Par,Child); father(Par,Child).
sibiling(Child1,Child2) :- parent(Par,Child1), parent(Par,Child2), Child1\=Child2.

son(Son,Parent) :- parent(Parent,Son), gender(Son,male).
daughter(Daughter,Parent) :- parent(Parent,Daughter), gender(Daughter,female).

brother(Bro,Sibling) :- parent(Parent,Bro),parent(Parent,Sibling), gender(Bro,male),Bro\=Sibiling.
sister(Sister,Sibling) :- parent(Parent,Sister),parent(Parent,Sibling), gender(Sister,female),Sister\=Sibiling.

ancestor(Ancestor,Desc) :- parent(Ancestor,Desc).
ancestor(Ancestor,Desc) :- parent(Ancestor,Intermid), ancestor(Intermid,Desc).

cousin(Child1,Child2) :- 
    parent(Parent1, Child1), 
    parent(Parent2,Child2),
    sibiling(Parent1,Parent2).

uncle(Uncle,Child) :-
    father(Father, Child), 
    sibiling(Father,Uncle),
    gender(Uncle,male).

aunt(Aunt,Child) :-
    mother(Mother, Child), 
    sibiling(Mother,Aunt),
    gender(Aunt,female).
