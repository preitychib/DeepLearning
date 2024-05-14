solution([]).
solution([X/Y|Others]) :- 
    solution(Others), 
    member(Y, [1, 2, 3, 4]), 
    noattack(X/Y, Others).

noattack(_, []).
noattack(X/Y, [X1/Y1|Others]) :- 
    Y \== Y1, 
    Y1-Y =\= X1-X, 
    Y1-Y =\= X-X1, 
    noattack(X/Y, Others).

member(X, [X|_]).
member(X, [_|L]) :- 
    member(X, L).



% ?- solution([1/Y1, 2/Y2, 3/Y3, 4/Y4]). 