principle = 1000; num_yeaes = 5; year = 1; rate = .05

while year<=num_yeaes:
    principle = principle*(1+rate)
    #print(year,principle)
    # Two print statements below is for the formatinf in a certain way
    #print("%3d %0.2f" % (year, principle))
    #print(format(year,"3d"),format(principle,"0.2f"))
    print("{0:3d} {1:0.2f}".format(year,principle))
    year+=1