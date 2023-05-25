eta_product11 = np.array([1,-2,-1,2,1,2,-2,0,-2,-2,1,-2,4,4,-1,-4,-2,4,0,2,2,-2,-1,0,-4,-8,5,-4,0,2,7,8,-1,4,-2,-4,3,0,-4,0,
                     -8,-4,-6,2,-2,2,8,4,-3,8,2,8,-6,-10,1,0,0,0,5,-2,12,-14,4,-8,4,2,-7,-4,1,4,-3,0,4,-6,4,0,-2,8,-10,
                     -4,1,16,-6,4,-2,12,0,0,15,4,-8,-2,-7,-16,0,-8,-7,6,2])
M = np.array([[4,1],[11,3]])
vplus = np.array([2,1])
vminus = np.array([0,1])
gamma = np.array([0,1])
expected_j = -1*2**(12)*11**(-5)*31**(3)
values = coeffs_calculator(eta_product11, M, vplus, vminus, gamma)
print('ω1=',values[3])
print('ω2=',values[4])
print('ω1/ω2=',values[3]/values[4])
print('g4=', values[0])
print('g6=', values[1])
c4 = 12*values[0]/((2*math.pi)**4)
c6 = -216*values[1]/((2*math.pi)**6)
c4guess = round(c4.real)
c6guess = round(c6.real)
print('c4guess=',c4guess)
print('c6guess=',c6guess)
u = u_calculator(c4guess, c6guess)
print('u=',u)
c4prime = c4guess/(u**4)
c6prime = c6guess/(u**6)
a = a_calculator(c4prime, c6prime)
print('coeffs:',a)
print('j=', values[2])
print('expected j=',expected_j)
print('error=',abs(expected_j-values[2]))
