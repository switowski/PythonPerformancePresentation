### I would like to talk about Python.
How many of you are programming in Python ?
Cool. How many of you have been programming in Python for more than 1 year ?
Great. And you many of you have been using Python 2 ? And Python 3 ?


Szkic:
Plan dzialania:
* Wprowadzenie - zapytac ile osob pisze w pythonie zeby nawiazac wiez z widownią
* Wspomnieć o ZEN pythona, gdzie jest napisane że powinna istniec jeden i tylko jeden sposob zrobienia czegos ale czasem nie do konca wiemy jak cos zrobic
* Powiedzieć, że czasem jak sobie programuję to nachodzi mnie mysl _a może to co teraz napisalem mozna napisac bardziej efektywnie ?_
* _Teraz chcialbym wam przedstawic kilka prostych przykladow, jak zastosowanie innej funkcji, innej struktury albo po prostu idiomatic python moze sie okazac szybszym rozwiazaniem. Oczywiscie, nie oczekujcie ze stosujac tych kilka prostych sztuczek wasz kod będzie smigal kilkukrotnie szybciej - ale jesli wybraliscie Python jako język programowania, to domyslam sie ze nie ze wzgledu na szybkosc :)_
* Zeby zobrazowac o ile wasz kod moze dzialac szybciej, w kazdym z przykladow pokażę benchmarki **(zarowno dla Pythona 2 jak i 3) / chyba jednak dla pythona 2 tylko**
* Slajdy:
1. Na początek cos prostego - roznica miedzy uzyciem funkcji len() a uzyciem wlasnorecznie napisanej funkcji do zliczania ilosci elementow: http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list
2. No a co jeśli chcemy przefiltrować jakąś dużą tablicę ? Porównanie własnoręcznie napisanej funkcji opartej o pętlę, wbudowanej funkcji filter() i list comprehension - list comprehension jest najbardziej czytelne i najszybsze
3. Finding a first element from array that matches the search criteria: użycie [for x in list if x == 2][0] vs generator expression: http://stackoverflow.com/questions/8534256/find-first-element-in-a-sequence-that-matches-a-predicate
4. Sprawdzenie czy element jest na liscie - porownanie dzialania loop i operatora "in" + zamiana list na set

5. Usuwanie duplikatów z listy przy użyciu funkcji set

6. each_with_index w pythonie (http://stackoverflow.com/questions/25569577/python-equivalent-of-rubys-each-with-index) - porównanie dzialania funkcji enumerate z wlasnorecznym pisaniem iteratora (poprzez uzycie czegos jak:
for element in array:
    index, element = array.index(element), element)
7. list vs tupple vs set: speed of membership checking: https://technobeans.wordpress.com/2012/04/09/performance-for-testing-memberships-list-vs-tuples-vs-sets/

Poszczególne tematy (ciekawsze są **pogrubione**):
* list vs tupple vs set: speed of membership checking: https://technobeans.wordpress.com/2012/04/09/performance-for-testing-memberships-list-vs-tuples-vs-sets/
* using dict() vs {} directly (maybe something similar for lists)
* Porównanie szybkosci tworzenia kopii listy: http://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list-in-python wraz z wyjasnieniem dlaczego niektore opcje sa szybsze ale mniej bezpieczene jesli bedziemy modifykowac liste
* Merging two dictionaries: http://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe
* lambda functions vs named functions, kiedy lambda będzie szybsza - nigdy, oba są tak samo szybkie, po co używać lambdy - bo wygląda fajnie jako one-liner + można jej użyc gry funkcja oczekuje obiektu (potrzebne zrodlo do tego)
* String concatenation
* don't write you own complicated data structures, most certainly there is a library for that: for example for queues, ...
* If you really need some universal speedup then try:
  * Cython - a superset of Python that allows you to write pieces of your code in C-like manner, thus making them faster
  * PyPy - a Python interpreter written in Python (Yo Dawg), which is just faster than the most commonly used CPython