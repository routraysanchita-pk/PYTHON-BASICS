#WRITE A PROGRAM TO ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN A DICTIONAARY.START WITH AN EMPTY DICTIONARY AND ONE BY ONE.USE SUBJECT NAME AS KEY AND MARK AS VALUE

mark={}

mark1=float(input("Enter the mark scored in Mathematics:"))
mark.update({"Maths":mark1})
mark2=float(input("Enter the mark scored in Science:"))
mark.update({"Science":mark2})
mark3=float(input("Enter the mark scored in Social Science:"))
mark.update({"Social Science":mark3})

print(mark)
