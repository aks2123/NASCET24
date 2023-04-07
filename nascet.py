def nascet (X,Y):
    Z= (((Y-X)/Y)*100)
    return round (Z,2)


X= float(input('Enter maximum stenosis: '))
Y= float(input ('Enter normal diameter: '))

print (f"Stenosis per NASCET criteria is {nascet (X,Y)} percent")
