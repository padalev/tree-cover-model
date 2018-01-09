clear; clc;
close all;
load('DynamicResults1.5zoom.mat');

zeropoint = -0.4878899;

defoValues = defoValues - zeropoint;

plot(defoValues,convergedT,'.k')
xlabel('Deforestation');
ylabel('Tree Cover');
title('Converged Tree Cover')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'Tconv.png');

figure;
plot(defo,T,'.k')
xlabel('Deforestation');
ylabel('Tree Cover');
title('All Tree Cover Values')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'allT.png');


figure;
plot(Time,T,'.k')
xlabel('Time Point');
ylabel('Tree Cover');
title('Time Series')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'timeSeries.png');


figure;
%plot(-defoValues,timeConstants,'ok')
loglog(-defoValues,timeConstants,'ok')
hold on
plot(1e-4:1e-4:1,6.5.*(1e-4:1e-4:1).^(-0.53),'-r')
xlabel('Deforestation');
ylabel('Time Constant of Convergence');
title('Time Constant of Convergence')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'timeConstants.png');


convSpeed = 1./timeConstants;
dconvSpeed = (convSpeed(2:end)-convSpeed(1:end-1))./(defoValues(2:end)-defoValues(1:end-1));
dconvSpeed = [1, dconvSpeed];

figure;
%plot(-defoValues,timeConstants,'ok')
plot(-defoValues,convSpeed,'ok')
%hold on
%plot(1e-4:1e-4:1,6.5.*(1e-4:1e-4:1).^(-0.53),'-r')
xlabel('Deforestation');
ylabel('Time Constant of Convergence');
title('Time Constant of Convergence')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'timeConstants.png');

figure;
%plot(-defoValues,timeConstants,'ok')
plot(-defoValues,-1/2*convSpeed./dconvSpeed,'ok')
hold on
plot(0:1e-4:1,(0:1e-4:1),'-r')
xlabel('Deforestation');
ylabel('Time Constant of Convergence');
title('Time Constant of Convergence')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'dtimeConstants.png');
