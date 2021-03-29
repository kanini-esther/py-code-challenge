def PassengerFlight(lof,movd):
    movies={}
    for i in movd:
        t=lof-i
        if i in movies.values():
            print(t,i)
            return True
            cd 
        movies[i]=lof-1

    return False