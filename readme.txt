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
4.refresh button works
adauga fereastra principala intr-o fereastra, astfel incat la nevoie
sa o poti distruge si reconstrui din celelalte functii.
 Va aparea un fisier separat main.py in care se va "porni" practic
 programul. 
5.schedule afisat (adica o lista primita)
6.adauga buton refresh pentru fereastra top

7.arranged schedule to look nice, colors looks strange=better without
<<<<<<< HEAD:Readme.txt

*dupa refresh nu mai merg zilele inainte si inapoi
*adauga icon
*implementeaza buton view all tasks, view timetable
	(pe zilele saptamanii)

STEPS:
# TO DO: I.INITIALIZAREA SCHEDULERULUI
#		 	1.in primul rand se citesc tasks si timetable
#			2.din timetable, se adauga in schedule, functie de zi fiecare
#				task, in fiecare zi din saptamana
#			3.din tasks se aleg taskurile cu
#				deadline de la cel mai apropiat la cel mai departat
#			4.pentru fiecare deadline care se gaseste in vreun task,
#			 	daca sunt mai multe taskuri cu acel deadline atunci
#				se alege prioritatea mai mare
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
# 		II.ADAUGA TASK
#		III.REMOVE TASK
				problema mare daca removez un task care este si in
					timetable. cum il fac sa nu mai fie pus in schedule?
#		IV.MODIFY TASK
#		V.POSTPONE TASK
=======
>>>>>>> d01f7a41d9f69ccff8801616724399c3fb4bb322:readme.txt
