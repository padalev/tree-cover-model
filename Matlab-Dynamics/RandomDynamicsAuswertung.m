clear; clc;
close all;
load('RandomDynamicResults_1.5_0.1v.mat');

zeropoint = -0.4878899;

defoValues = defoValues - zeropoint;

plot(defoValues,acValues.^2)
hold on;
plot(-3.3:1e-3:0,0.019*(abs(-3.3:1e-3:0)).^0.9);

figure
semilogy(defoValues,variValues)
