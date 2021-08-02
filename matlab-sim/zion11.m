clear all
clc

function  dN=zion11(t,N)
dN = zeros(1,1);
a = 0.15+0.01*rand(1);
alpha = 0.15;
r = 2.4;
dN(1)=(a-N(1))*(alpha+(1/r)) 
