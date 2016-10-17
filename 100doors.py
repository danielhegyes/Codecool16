
doorcond = ['Closed']*101
 #Ha szépen megkérem a pájtont, akkor megírja helyettem a programot?
for i in range( 1, 101 ) :

    for n in range(i,101,i) :

        if doorcond[n] == 'Closed':
            doorcond[n] = 'Opened'

        elif doorcond[n] == 'Opened' :
            doorcond[n] = 'Closed'

for x in range (1,101):
	if doorcond[x] == 'Opened':
		print (x, 'is opened')




