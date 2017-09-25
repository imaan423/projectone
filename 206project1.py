import os
import filecmp
import csv


def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

        list = []
        with open(file) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                        list.append(row)
                return list
        
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

    new_list = sorted(data, key=lambda k: k[col])
    firstName = new_list[0]["First"]
    lastName = new_list[0]["Last"]
    full_name = firstName + " " + lastName
    return full_name

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

        freshman = 0
        sophomore = 0
        junior = 0
        senior = 0
        for person in data:
                if person['Class'] == 'Freshman':
                        freshman += 1
                elif person['Class'] == 'Sophomore':
                        sophomore += 1
                elif person['Class'] == 'Junior':
                        junior += 1
                elif person['Class'] == 'Senior':
                        senior += 1
        fresh_t = ('Freshman', freshman)
        soph_t = ('Sophomore', sophomore)
        juni_t = ('Junior', junior)
        senior_t = ('Senior', senior)
        new_class = [senior_t, juni_t, soph_t, fresh_t]
        return sorted(new_class, key = lambda x:x[1], reverse = True) 


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DO

        month = [0]*32
        max = 0
        for person in a:
                day = person['DOB'].split("/")[1]
                day_int = int(day)
                month[day_int]+= 1
        for i in range(len(month)):
                if month[i] > max:
                        max = month[i]
                        maxIndex = i
        return maxIndex

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

        sum = 0
        for person in a:
                year = person["DOB"].split("/")[2]
                age = 2017 - int(year)
                sum += age
        average = sum / len(a)
        return round(average)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

    write_file =  open(fileName, 'w')
    new_list = sorted(a, key=lambda x:x[col])
    for person in new_list:
        write_file.write(person["First"])
        write_file.write(",")
        write_file.write(person["Last"])
        write_file.write(",")
        write_file.write(person["Email"])
        write_file.write(",")
        write_file.write(person["Class"])
        write_file.write(",")
        write_file.write(person["DOB"])
        write_file.write("\n")
    write_file.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

