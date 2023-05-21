Celem zadania czwartego jest stworzenia programu implementującego dwie metody całkowania:
 - złożoną kwadraturę Newtona-Cotesa opartą na trzech węzłach (wzór Simpsona)
 - wariant Gaussa 
	- całkowanie na przedziale (-inf, +int) x wagą e^(-x^2) (wielomiany Hermite'a) całek postaci 
	całka -inf + inf e^(-x^2)f(x)dx
	
	

- Kwadratury złożone Newtona-Cotesa obliczane są z dokładkością podaną przez użytkownika.
- Odbywa się to w sposób iteracyjny.
- W każdej iteracji ilość podprzedziałów na które podzielony jest przedział całkowania jest zwiększana (można zwiększać dwukrotnie lub o jeden), a otrzymany wynik całkowania porównywany jest z wynikiem z poprzedniej iteracji.
- Jeśli wynik zmienił się o mniej niż dokładność podana przez użytkownika, oznacza to że dokładność całki na podanym przedziale została obliczona z zadaną dokładnością.


- Konieczne jest dodatkowo obliczanie granicy. Bez tego wyniki uzyskane obiema metodami nie byłyby porównywalne.
- Przy obliczaniu całki na przedziale [0,+∞) stosuje się następujące podejście:
	- rozpoczyna się od obliczenia całki na przedziale [0,a), gdzie a>0.
	- Następnie obliczana jest całka na przedziale [a,a+δ), gdzie δ>0.
	- Jeśli wartość całki na tym przedziale jest większa od zakładanej dokładności, to otrzymany wynik dodawany jest do wcześniejszego wyniku, przyjmuje się a:=a+δ, po czym operacja jest powtarzana.
	- Jeśli wartość całki na przedziale [a,a+δ) jest mniejsza od zadanej dokładności uznaje się, że policzyło się granicę dążącą do +∞.
	- Analogicznie postępuje się obliczając wartość całki na przedziale (−∞,0].
	- W przypadku obliczania granicy dążącej do ±1 postępuje się w sposób podobny, przy czym najpierw liczy się wartość całki na przedziale [0,12), potem dolicza się wartość na przedziale [12,12+12⋅12), następnie na przedziale [34,34+14⋅12), potem [78,78+18⋅12) itd.
	
	- Kwadratury Gaussa obliczane są dla 2, 3, 4 i 5 węzłów.
	- Można wykorzystać znane z literatury wartości miejsc zerowych wielomianów oraz współczynniki kwadratur Gaussa. 
	- W przypadku wariantu 4 konieczne jest przeskalowanie funkcji i granic całkowania na przedział [−1,1).
	
	
	# SPRAWOZDANIE
	- W sprawozdaniu należy porównać wyniki uzyskane za pomocą obu metod całkowania (program ma posiadać kilka różnych funkcji do wyboru). 
	- Należy pamiętać, że funkcje całkowane w wariantach 1-3 są postaci w(x)*f(x), gdzie w(x) to funkcja wagowa, przy czym w kwadraturach Gaussa funkcja wagowa jest od razu uwzględniona w metodzie.
	- Przy obliczaniu kwadratur Newtona-Cotesa trzeba więc dodać funkcję wagową.