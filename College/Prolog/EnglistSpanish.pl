english_spanish("One", "Uno").
english_spanish("Two", "Dos").
english_spanish("Three", "Tres").
english_spanish("Four", "Cuatro").
english_spanish("Five", "Cinco").
english_spanish("Six", "Seis").
english_spanish("Seven", "Siete").
english_spanish("Eight", "Ocho").
english_spanish("Nine", "Nueve").
english_spanish("Ten", "Diez").

translate_td([], []).
translate_td([English|EnglishList], [Spanish|SpanishList]) :-
english_spanish(English, Spanish), translate_td(EnglishList, SpanishList).


% ?-translate_td(["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
"Nine", "Ten"], S).

% ?- translate_td(E, ["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho",
"Nueve", "Diez"])