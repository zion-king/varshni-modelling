clear all
clc

function  dN = zion10(t,N)
dN = zeros(1,1);
a = 0.15;
alpha = 0.15;
r = 2.4;
dN(1) = (a-N(1))*(alpha+(1/r)) 
