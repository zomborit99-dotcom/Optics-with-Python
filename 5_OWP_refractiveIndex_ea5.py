import numpy as np
import matplotlib.pyplot as plt
plt.close('all')






"""(11)_<<<<<<<<<<<<<_REFRACTIVE INDEX - SELLMEIER POLYNOMIAL>>>>>>>>>>_(11)"""
#Describes how much slower the speed of light is in a medium compared to its
#speed in vacuum: 
#v = c/n(om), where om = 2*pi*c/lambda, or om = 2*pi*v/lambda_medium
#lambda_medium = lambda/n

#One way to describe the refractive index is with the empirically determined
#Sellmeier-polynomial:
#n(lambda)**2 = 1 + sum_i(   (B_i*lambda**2) / (lambda**2 - C_i)   )
#Here lambda is the wavelength in vacuum. Usually 'i' ranges from 1 to 3. This
#formula is based on the Lorentz model of atoms. 

#Numerous materials' Sellmeier polynomial can be found on:
#https://refractiveindex.info/. Here one must give lambda in micrometers!



"""Let's test the polynomial for a BK7 glass medium!"""
def n(x, n_type):
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



def plot(lamdaStart, lamdaEnd, lamdaStep, n_type, xlabel='Wavelength [nm]',
         style='r-', title='Refractive index'):
    #Here the wavelengths are given in nanometers!
    lamda = np.arange(lamdaStart, lamdaEnd, lamdaStep)/1000 
    #Conversion: nm --> um
    fig, ax = plt.subplots()
    ax.plot(lamda*1000, n(lamda, n_type), style, label=n_type)
    ax.grid(axis='both')
    ax.set_ylabel(n_type + ' [-]')
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    return ax
    
ax1=plot(400, 1000, 1, 'n_BK7') #Typing plot(...) is enough in itself for the
                                #plot to show! The ax1=plot(...) formalism will
                                #be made use of later in the program.



"""Now do the same for fused silica!"""
ax2=plot(400, 1000, 1, 'n_FS', style='b-')



"""Now let's concatenate the plots in order to compare them!"""
line2 = ax2.lines[0]    #ax2 has a list of curves (referred to as 'lines').
line1 = ax1.lines[0]    #In this case, the list has 1 element.
fig, ax3 = plt.subplots()

ax3.plot(  line2.get_xdata(), line2.get_ydata(), label=line2.get_label(),
           color=line2.get_color(), linestyle=line2.get_linestyle()  )
#Using the method of 'lines', we can call upon the previous plots' contents!
#We can also use ax2.lines[0].get_xdata()!

ax3.plot(  line1.get_xdata(), line1.get_ydata(), label=line1.get_label(),
           color=line1.get_color(), linestyle=line1.get_linestyle()  )

ax3.legend(loc='upper right')
ax3.set_xlabel('Wavelength [nm]')
ax3.set_ylabel('n [-]')
ax3.grid()






"""(12)_<<<<<<<<<<<<<<<_REFRACTIVE INDEX + SNELL'S LAW>>>>>>>>>>>>>>>>>_(12)"""





















































