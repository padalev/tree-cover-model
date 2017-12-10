clear; clc;
close all;
load('DynamicResults.mat');

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
semilogy(defoValues,timeConstants,'.k')
xlabel('Deforestation');
ylabel('Time Constant of Convergence');
title('Time Constant of Convergence')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'timeConstants.png');






