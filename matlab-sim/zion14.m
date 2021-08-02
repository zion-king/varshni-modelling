clear all
clc

function  dN=zion14(t,N)
dN=zeros(1,1);
a=0.15;
alpha=0.15+0.4*rand(1);
r=2.4;
dN(1)=(a-N(1))*(alpha+(1/r))
