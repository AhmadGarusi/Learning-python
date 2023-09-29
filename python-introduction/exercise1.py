# kg <--> lbs

weight = float( input( "weight: " ) )

quantity = input( "(K)g or (L)bs: " )

if quantity == "k" or quantity == "K":
    weight = weight * 2.204
    print( "kg to lbs: " + str( weight ) )
elif quantity.lower == "l":
    weight = weight * 0.453
    print( "lbs to kg: " + str(weight) )