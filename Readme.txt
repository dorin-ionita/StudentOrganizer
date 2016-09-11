	Se foloseste o baza de date cu parola "ionita", username root.
	Baza de date se numeste studentorganizer si este localhost.
	
baza de date contine:
1.tabela tasks
	contine taskurile neschedulite
	0. ID int
	1. NAME char
	2. PRIORITY int
	3. TIME_REQ float
	4. DEADLINE datetime.date
2.tabela timetable
	contine orarul si taskurile repetitive
	(de genul somn)
	0. ID int
	1. DAY char
	2. START_HOUR ?
	3. END_HOUR ?
	4. NAME char
	5. PARITY int
3.tabela schedule
	contine programul asa cum a fost facut de programul
	de aici voi pune in GUI
	0. ID int
	1. DATE datetime.date
	2. START_HOUR Time/datetime.timedelta
	3. END_HOUR Time/datetime.timedelta
	4. NAME char
	5. POSTPON int


Milestones
1.butonul addTask functioneaza in felul in care am dorit
2.butonul removeTask functioneaza in felul in care am dorit
3.butonul postponeTask functioneaza in felul in care am dorit
4.butonul modifyTask functioneaza in felul in care am dorit

show schedule