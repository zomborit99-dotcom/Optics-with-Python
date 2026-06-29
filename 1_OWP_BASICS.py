""" TASK: write a script that calculates and prints the distance of 
    an image created by a convex lens!
        *** f = 5 cm, t = -6 cm
            
        ==>   1/im - 1/ob = 1/f   ==>   1/im = 1/f + 1/ob   ==>
        im = (f*ob) / (ob+f)
"""
f, ob = 5, -6
im = (f*ob) / (ob+f)
print("Image distance: {0:.2f}".format(im))







"""(1)_<<<<<<<<<<<<<<<<<<<<<<<_WHILE AND FOR LOOP_>>>>>>>>>>>>>>>>>>>>>>>>>>"""
t = 0
while t<5:
    t=t+1
    print(t)


name = 'Python'
i = 0
while i < len(name):
    print(name[i])
    i+=1
    
    
"""for loop"""
name = 'Python'
for i in name:
    print(i)
    






"""(2)_<<<<<<<<<<<<<<<<<<<<<<<<_INPUT FUNCTION_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
a = input('Wavelength: ')
print(a)
print(type(a))


a = float(input('Wavelength: '))
print(a)
print(type(a))







"""(3)_<<<<<<<<<<<<<<<<<<<<<<<<<<<_FUNCTIONS_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
def cube(x):
    #return the cube of a number
    return x**3


def volume(x):
    #calculates the volume of a sphere
    return 4 * 3.1415 * cube(x) / 3


r = input('Radius of sphere: ')
r = float(r)
V = volume(r)
print('The volume of the sphere: {0:.2f}.'.format(V))




































