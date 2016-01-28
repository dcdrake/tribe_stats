print '\n'
print '\n'
print '\n'
print '\n'
print '###############################################################'
print 'Tribe Basketball Stats Database'
print '###############################################################\n'


while(True):

	print '========================================================'
	print "1) Display career stat totals for a player"
	print "2) Display stats for player in a specific game"
	print "3) Display team stats for a specfic game\n"
	print "** Type 'q' to quit **"
	print '========================================================'
 	
 	selection = raw_input("Enter selection: ")

 	print '\n'

 	if (selection == '1'):
 		print '-----------------------------------------------------'
 		print '----- Display career stat totals for a player  ------'
 		print '-----------------------------------------------------'
 		print "1) Enter a player's name"
		print "2) Show a list of all players"
		print "** Type 'b' to go back to main menu **"

		selection = raw_input("Enter selection: ")

 	elif (selection == '2'):
 		print "2"
 	elif (selection == '3'):
 		print "3"
 	elif (selection.lower() == 'q'):
 		break
 	else:
 		print "-- That is not a valid selection, choose again --"

	print '\n'	
 		