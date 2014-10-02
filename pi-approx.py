# Pi approximation, by Sabastian Mugazambi
pi_approx = 0.0
num_terms = 50000 # Entering the number of terms I would like to use for the approximation of pi.            
 
# Creating a loop that estimates pi 

for i in range(num_terms):
	if i%2 == 0:
		pi_approx = pi_approx + (4/float(1+i*2))
	if i%2 == 1:
		pi_approx = pi_approx - (4/float(1+i*2))
	
 		
	
print "After", num_terms, "terms, my approximation of pi is", pi_approx


# For num_terms = 50000, this gets the first 5 digits of pi correct and gives the 7th to the 11th correct as well.  