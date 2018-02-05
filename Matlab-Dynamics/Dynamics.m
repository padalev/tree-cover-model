clear; clc;

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

P = 1.5; %1.5 nice for visibility, 5.0 for forest state analysis
endpoint1 = -0.4878899;

ConvergenceLength = 1e4;
TimeStep = 5e0; %5e-1; % for safe iteration 
C0 = zeros(ConvergenceLength,1);

pointDensity = 1e2;

%defoValues = [linspace(-2,3,pointDensity),linspace(3,-2,pointDensity),linspace(-2,1/2,pointDensity),linspace(1/2,-2,pointDensity)];
defoValues = endpoint1 - logspace(-2,-5,pointDensity);
defo = [];

for i = 1:length(defoValues)
    nv = defoValues(i)+C0;
    defo = [defo; nv];
end

T = defo.*0;
T(1) = 90;
convergedT = defoValues.*0;
convergedcounter = 1;
Time = defo.*0;

for ts=1:length(defo)-1
    T(ts+1) = T(ts) + TimeStep*dTdt(P,T(ts),defo(ts));
    Time(ts+1) = Time(ts)+TimeStep;
        
    if (defo(ts+1) ~= defo(ts))
        convergedT(convergedcounter) = T(ts);
        convergedcounter = convergedcounter +1;
    end
end

%plot(defoValues,convergedT,'.k')
%plot(defo,T,'.k')
%plot(Time,T,'.k')
defoConstTime = reshape(Time,[ConvergenceLength,length(defoValues)]);
defoConstT = reshape(T,[ConvergenceLength,length(defoValues)]);

for i= 1:length(defoValues)
   defoConstTime(:,i) =  defoConstTime(:,i) - defoConstTime(1,i);
   defoConstT(:,i) =  defoConstT(:,i) - defoConstT(end,i);
end

%plot(defoConstTime(:,3700:3800),defoConstT(:,3700:3800))

timeConstants = defoValues.*0;
amplitudes = defoValues.*0;

for i = 1:length(defoValues)
    i
   [tcn,an] = fitTimeConst(defoConstTime(:,i),defoConstT(:,i));
   timeConstants(i) = tcn;
   amplitudes(i) = an;
end
%  
% plot(timeConstants)



save('DynamicResults1.5zoom2.mat','T','Time','amplitudes','convergedT','defo','defoConstT','defoConstTime','defoValues','timeConstants');

















