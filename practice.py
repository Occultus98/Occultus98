print("\n\tONLINE SCHOLARSHIP UNDERGRADUATE SCHEME\n\nPlease enter details below to apply;\n")
first_name = input("\nFirst Name: ")
second_name = input("\nLast Name: ")
sex = input("\nGender: ")
print("\n\"Please be notified: Applicant must be aged (18 - 21) years!\"")
birth_year = int(input("Please enter birth year: "))
current_year = 2024
age = current_year - birth_year
if age < 18 or age > 21:
    SystemExit
    print("\n\t\"Sorry, you are NOT ELIGIBLE for this scholarhip. \n\t\tYou are out of the age bracket!\"\n")
else:
    course = input("\nDesired course: ")
    contact = input("\nPhone number: ")
    residence = input("\nCity: ")
    nationality = input("\nCountry: ")
    next_of_kin = input("\nNext of kin: ")
    print("\nPlease press ENTER to submit your details... ")
    submission = input()

    print("\n\t\t\"Thank you for applying, request submitted!\"\n")