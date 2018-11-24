def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count #PRITNS(for user?) the cheeses count, but why %d??? what is that "%d?" Find OUT!
    print "You have %d boxes of crakers!" % boxes_of_crackers # Prints the number of crakers... bur why %d?
    print "Man that's enough for party!" # Just a tekst
    print "Get a blanket.\n" #what did \n do? Something about escaping(which is a thing as well :F)?

 
print "We can just give the function numbers directly:" #Just printing a text
cheese_and_crackers(raw_input, raw_input) #Giving the function numbers directly.


print "OR, we can use variables from our script:" #just a text
amount_of_cheese = (raw_input) # Giving that %d a number? 
amount_of_crackers = (raw_input) # Giving that %d a number?

cheese_and_crackers(amount_of_cheese, amount_of_crackers)#???Using variables???Still I DONT KNOW, yet...


print "We can even do math inside too:" #Priting just the text
#cheese_and_crackers( 10 + 20, 5 + 6) # Actually doing math inside too...(I guess need to start doing math :D) 


print "And we can combine the two, variables and math:"#Printing text 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #Combining math and variables. I guess I got it, Woohoo!
print "DO THAT STUDY DRILL - 3(71). To understand more, just for practice porpuse!"