clear; clc;close all;

h_A = 10;
h_f = 64;
h_P = 0.5;
K = 90;
m_A = 0.15;
m_f = 0.11;
p = 7;
b = 0;
r_m = 0.3;
r_P = 1;

expansionrate = @(P)  P./(h_P + P).*r_m;
dTdt = @(P,T,deforest) expansionrate(P).*T.*(1-T./K)-m_A.*T.*h_A/(T + h_A) - m_f.*T.*h_f.^p/(h_f.^p + T.^p) - deforest;
dPdt = @(P,T) r_P.*((P + b.*T./K) - P); % Not used for now

defolength = 2;
defoValues = linspace(-1.9,-0.4,defolength);
acValues = defoValues.*0;
variValues = defoValues.*0;
Tconv = defoValues.*0;

meanP = 1.5;
variP = 0.1;

TimeStep = 1;
preRun = 1e5;
runTime = 1e4;


for defocounter = 1:defolength
defocounter

pValues = meanP + variP.*(2*rand(1,runTime)-1);

T = pValues.*0;
T(1) = 90;
Time = pValues.*0;

for ts=1:preRun
    T(1) = T(1) + TimeStep*dTdt(pValues(1),T(1),defoValues(defocounter));
end

for ts=1:length(pValues)-1
    T(ts+1) = T(ts) + TimeStep*dTdt(pValues(ts),T(ts),defoValues(defocounter));
    Time(ts+1) = Time(ts)+TimeStep; 
end

figure
plot(Time(1000:3000),T(1000:3000),'-k','LineWidth',2)
axis([1000 2000 38.8 39.8])
xlabel('Time (yr)');
ylabel('Tree cover (%)');
set(gca,'FontSize',25,'LineWidth',3.0);
r = 200; % pixels per inch
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 3600 1000]/r);
print(gcf,'-dpng',sprintf('-r%d',r), 'plot.png');

Tconv(defocounter) = T(end);

T = T - mean(T);

maxac = 100;
autocorr = zeros(1,maxac+1);
autocorrf = 1:maxac+1;
autocorrf = autocorrf-1;
for ac = 0:maxac
    acs = ac+1;
    ace = ac+runTime-maxac;
    autocorr(ac+1) = sum(T(1:runTime-maxac).*T(acs:ace));
end

autocorr = autocorr/autocorr(1);

% plot(autocorrf,autocorr,'-k','LineWidth',3)
% hold on
% plot((linspace(0,100)),0*linspace(0,1), '-k','LineWidth',1.5)
% axis([0 100 -0.2 1])
% xlabel('\Delta T (yr)');
% ylabel('ACF');
% set(gca,'FontSize',25,'LineWidth',3.0);
% r = 200; % pixels per inch
% set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 3600 1000]/r);
% print(gcf,'-dpng',sprintf('-r%d',r), 'plot.png');

acValues(defocounter) = (1-autocorr(2));

variValues(defocounter) = sum(T.^2)/runTime;

end
% figure
% plot(defoValues, acValues);
% figure
% plot(defoValues, variValues);

%save('RandomDynamicResults_1.5_0.1v.mat','defoValues','acValues','variValues','Tconv');

















