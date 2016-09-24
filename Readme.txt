	Se foloseste o baza de date cu parola "ionita", username root, configurabila
	din ./cfg/database_authentication.cfg
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
4.refresh button works
adauga fereastra principala intr-o fereastra, astfel incat la nevoie
sa o poti distruge si reconstrui din celelalte functii.
 Va aparea un fisier separat main.py in care se va "porni" practic
 programul. 
5.schedule afisat (adica o lista primita)
6.adauga buton refresh pentru fereastra top
7.arranged schedule to look nice, colors looks strange=better without
8.butonul de addTask adauga in baza de date:D
9.fixed the refresh button so that it refreshes properly, getting the
	new schedule list.
10.fixed the refresh button so that after refresh I can go the day
	after and the day before
11.butonul modify task modifica in baza de date
12.adauga in cfg file data de inceptu a facultatii, pentru a stii cum
	decurg partitatile

*adauga icon
*implementeaza buton view all tasks, view timetable
	(pe zilele saptamanii)
*fa click inainte in schedule, cu exceptile mentionate
*introdu fisier de cfg (eventual in folder separat)
	care sa contina date despre baza de date
*fa un shell script care sa instaleze mysql si sa configureze
	baza de date
*testeaza si pe windows, mai ales vezi cum faci cu baza de date
*adauga formatul orei ca instructiune pentru utilizator 
	ma refer la time_required
*vezi de ce nu merge refresh, de ce apar cacaturile vechi inca
*la final de tot, modifica milestone9 si main.py sa lucreze
	pe task, nu pe schedule
*notify bug. poate cu CGI
*fa reschedule button, ca dureaza prea mult de fiecare data
*fa totul (ne)resizable si adauga scrollbar
*optimizari. neaparat!
*modifica readmeul in md pe github
*fa coding style conform normelor
*MUST: o singura deschidere de baza de date/o singura data acces, ca moare!

STEPS:
# TO DO: I.INITIALIZAREA SCHEDULERULUI
#		 	1.in primul rand se citesc tasks si timetable 					[x]
#			1.1. se sterge tot ce e in schedule 							[x]
#			2.din timetable, se adauga in schedule, functie de zi fiecare
#				task, in fiecare zi din saptamana							[x]
#			3.din tasks se aleg taskurile cu
#				deadline de la cel mai apropiat la cel mai departat			[x]
#			4.pentru fiecare deadline care se gaseste in vreun task,
#			 	daca sunt mai multe taskuri cu acel deadline atunci
#				se alege prioritatea mai mare								[x]
#			  NOTE: 3 si 4 sa se efectueze intr-o sortare
#				i)daca taskul e first of day se adauga +1 ora dimineata
#				ii)daca taskul este last of day se adauga +1 ora seara
#				iii)daca dupa task urmeaza pauza se adauga +30 min
#					liber
#				iv)daca task=somn se adauga 30 de minute inainte libere
#			6.se cauta succesiv in schedule locuri libere
#				pentru a introduce taskurile.
#				Taskurile nu se pot faramita, a.i. ele trebuie deja
#				introduse faramitate.
#			7.se afiseaza in fereastra principala
# 		II.ADAUGA TASK 														[x]
#		III.REMOVE task: requires I
#				problema mare daca removez un task care este si in
#					timetable. cum il fac sa nu mai fie pus in schedule?
#				pune numele __no_timetable__, de exemplu.
#		IV.MODIFY TASK 														[x]
#		V.POSTPONE TASK: REQUIRES I
#		VI.ADD TASK IN SCHEDULE BY HAND:
#				pune numele by hand
#			fa clean inainte, in schedule, cu exceptile mentionate