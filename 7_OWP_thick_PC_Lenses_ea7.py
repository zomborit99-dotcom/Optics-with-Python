import numpy as np
import matplotlib.pyplot as plt
plt.close('all')



def n(x, n_type):
    x = x/1000
    if n_type=='n_BK7' and np.all(0.3<=x) and np.all(x<=2.5):
        return (1+1.03961212/(1-0.00600069867/x**2)+0.231792344/
            (1-0.0200179144/x**2)+1.01046945/(1-103.560653/x**2))**.5
    #Conditions: 
    #Temperature = 293 °K
    #Wavelength range: 0.3um - 2.5um
    
    elif n_type=='n_FS' and np.all(0.21<=x) and np.all(x<=6.7):
        return (1+0.6961663/(1-(0.0684043/x)**2)+0.4079426/
        (1-(0.1162414/x)**2)+0.8974794/(1-(9.896161/x)**2))**.5
    #Conditions: 
    #Temperature = 293 °K
    #Wavelength range: 0.21um - 6.7um
    
    else:
        return 'Invalid input'



def plot(*lines, title='', xlabel='', ylabel='', legend=0, legLoc='upper right'):
    fig, ax = plt.subplots()
    for x, y, style, label in lines:    
        ax.plot(x, y, style, label=label)
        if legend==1:
            ax.legend(loc=legLoc)
        
    ax.grid()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    
    return ax






"""(14)_<<<<<<<<<<<<<<<<<<<<<<<_THIN LENSES_>>>>>>>>>>>>>>>>>>>>>>>>>>>_(14)"""
#Here, the thickness of the lenses is non-negligible, which changes some of the
#already showed formulae. 
#Furthermore, the concept of princal points and planes emerge, which are the
#externally outgoing and incoming rays' elongated crossing points/planes. 

#The below principal plane distances (h1, h2) will be measured from the 
#central, most external point of the surface of the lense. Note that the 
#(effective) focal lengths (EFL) are measured relative to the principal points.
#A visual demonstration can be seen on 7_OWP_thickLenseInkscape_PICTURE_1.

#As an excercise, let's have a look at the following lense and calculate its
#characteristic lengths:
#https://www.edmundoptics.com/p/250mm-dia-x-1000mm-fl-uncoated-plano-convex-lens/2366/

#material: N-BK7
CT = 4.3#mm Center Thickness
R1 = 51.68#mm
R2 = np.inf
wl_r = 587.6#nm reference wavelength



#The princal lengths then are:
h1 = (R1*CT)   /   (   
    n(wl_r, 'n_BK7')*(R1-R2) - (n(wl_r, 'n_BK7')-1)*CT   )
print(h1)#0, as expected from R2=np.inf and the formula.



h2 = (-R2*CT)  /  (
    n(wl_r, 'n_BK7')*(R1-R2) - (n(wl_r, 'n_BK7')-1)*CT  )   
print(h2)#This is nan, because np.inf/np.inf=nan, but by simplifying:
h2 = CT / n(wl_r, 'n_BK7')
print(h2)



#The EFL:
EFL = 1/(    (n(wl_r, 'n_BK7')-1)   *   (1/R1 - 1/R2 + 
    CT*(  n(wl_r, 'n_BK7')-1)  /  (n(wl_r, 'n_BK7')*R1*R2)  )  )
#after simplifying: f = R1  /  (n(wl_r/1000, 'n_BK7')-1)



#The back focal length:
BFL = EFL - h2
print(BFL)






"""(15)_<<<<<<<<<<<<<<<<_PLANOCONVEX LENSES' LSA & TSA_>>>>>>>>>>>>>>>>_(15)"""
#Let's have alook at the LSA and TSA of a planoconvex lense, where the light 
#rays are first incident on the plane part of the lens!
#For a visual demonstration, see: 7_OWP_planoConvex_PICTURE_2.
R2_PC = -R1        #Keep in mind that for this task we flipped the lense!


z0 = 0
y0 = np.arange(0, 12+0.5, 0.5)


y1 = y0         #This must be defined before z1!
z1 = np.sqrt(R2_PC**2-y1**2)


phi = np.arcsin(  y1/(-R2_PC)  )
beta = np.arcsin(    n(wl_r,'n_BK7')*np.sin(phi)    )


m = np.tan(   phi-beta   )
b = y1  -  m*z1
z2 = -b/m


BFL_PC = EFL       
z3 = -R2_PC+BFL_PC
y3 = m*z3+b


LSA_PC = z2 - z3
TSA_PC = y3


plot(      (y0, LSA_PC, 'r-', 'LSA'), (y0, TSA_PC, 'b-', 'TSA'),
     title='LSA_PC & TSA_PC', xlabel='y0 [mm]', ylabel='Aberration [mm]',
     legend=1, legLoc='lower left'              )



#Now let's do the same, but this time let the incident rays meet with convex 
#part of the lense first! Visual demo: 7_OWP_CPSetup_PICTURE_2.
R1_CP = R1


z0 = 0
y0 = np.arange(0, 12+0.5, 0.5)


y1 = y0
z1 = R1_CP - np.sqrt(R1_CP**2 - y1**2)


phi = np.arcsin(   y0/R1_CP   ) #alpha1
beta1 = np.arcsin(   np.sin(phi) / n(wl_r,'n_BK7')   )
m1 = -1*np.tan(phi - beta1)
b1 = y1 - m1*z1


z2 = CT
y2 = m1*z2 + b1


alpha2 = phi - beta1
beta2 = np.arcsin(   n(wl_r,'n_BK7') * np.sin(alpha2)   )
m2 = -np.tan(beta2)
b2 = y2 - m2*z2


y3 = 0
z3 = -b2 / m2


z4 = CT + BFL
y4 = m2*z4 + b2
TSA_CP = y4
LSA_CP = z3 - z4


plot(      (y0, LSA_CP, 'r-', 'LSA'), (y0, TSA_CP, 'b-', 'TSA'),
     title='LSA_CP & TSA_CP', xlabel='y0 [mm]', ylabel='Aberration [mm]',
     legend=1, legLoc='lower left'              )
#Notice how this setup has SIGNIFICANTLY less aberrations for parallel rays!
#Often times, the closer the deviations (delta angle) caused by the 2 surfaces
#are to each other in value, the smaller the aberrations will be, meaning that
#if instead of perpendicularly incoming parallel rays we were emitting light
#from the focal points and leading them towards the lense, then the PC setup
#would perform better.
































