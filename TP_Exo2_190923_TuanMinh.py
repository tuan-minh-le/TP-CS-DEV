def bissextile(year):
    if str(year).isdigit():
        if year % 100 != 0 and year % 4 == 0 :
            return True
        elif year % 400 == 0 :
            return True
        else :
            return False


def months(month, year):
    if str(month).isdigit() == True and month <= 12 :
        if month == 2 and bissextile(year) == True :
            return 29
        elif month == 2 and bissextile(year) == False :
            return 28
        elif (month <= 7 and month % 2 != 0) or (month >= 8 and month %2 == 0 )  :
            return 31
        elif  (month <= 6 and month %2 == 0) or (month >= 9 and month %2 != 0 ) :
            return 30
        
def valid(date, month, year) :
    maxnb = months(month,year)
    if date <= maxnb :
        return True
    else :
        return False

def calendar():
    date = int(input("Veuillez saisir la date : "))
    month = int(input("Veuillez saisir le mois : "))
    year = int(input("Veuillez saisir l'annee : "))
    if valid(date, month, year) == True : 
        print("Date valide")
    else :
        print("Date non valide")

