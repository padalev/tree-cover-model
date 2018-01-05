clear; clc;
close all;
load('DynamicResults1.5zoom.mat');

zeropoint = -0.48755;

defoValues = defoValues - zeropoint;

% plot(defoValues,convergedT,'.k')
% xlabel('Deforestation');
% ylabel('Tree Cover');
% title('Converged Tree Cover')
% r = 100; % pixels per inch
% set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
% print(gcf,'-dpng',sprintf('-r%d',r), 'Tconv.png');
% 
% figure;
% plot(defo,T,'.k')
% xlabel('Deforestation');
% ylabel('Tree Cover');
% title('All Tree Cover Values')
% r = 100; % pixels per inch
% set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
% print(gcf,'-dpng',sprintf('-r%d',r), 'allT.png');
% 
% 
% figure;
% plot(Time,T,'.k')
% xlabel('Time Point');
% ylabel('Tree Cover');
% title('Time Series')
% r = 100; % pixels per inch
% set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
% print(gcf,'-dpng',sprintf('-r%d',r), 'timeSeries.png');


figure;
loglog(-defoValues,timeConstants,'ok')
hold on
plot(1e-4:1e-4:1,6.5.*(1e-4:1e-4:1).^(-0.53),'-r')
xlabel('Deforestation');
ylabel('Time Constant of Convergence');
title('Time Constant of Convergence')
r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 2200 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'timeConstants.png');






