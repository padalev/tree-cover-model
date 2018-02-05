clear; clc;
close all;
load('RandomDynamicResults_1.5_0.1v.mat');

zeropoint = -0.4878899;

defoValues = -defoValues + zeropoint;

plot(defoValues,acValues,'-k','LineWidth',2)
hold on;
axis([0 1.4 0 0.18])
%plot(-3.3:1e-3:0,0.019*(abs(-3.3:1e-3:0)).^0.9);
xlabel('\Delta deforestation (%/yr)');
ylabel('AC measure');
set(gca,'FontSize',25,'LineWidth',3.0);

r = 100; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 1800 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'randTimeConst.png');