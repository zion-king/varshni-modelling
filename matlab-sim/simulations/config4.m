% Configuration 4 Simulation

t = 0:1:14
[t    Y] = ode45(@zion10,  [t], [2.5],'reltol=0.001')
[t    Y1] = ode45(@zion14,  [t], [2.5],'reltol=0.001')
E1 = [(Y1-Y)./Y]*100
ANS = [t       Y       Y1          E1]
K=Y - Y1
