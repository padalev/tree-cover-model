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

P = 3;

ConvergenceLength = 1e2;
TimeStep = 3e-1;
C0 = zeros(ConvergenceLength,1);

defoValues = [linspace(-2,5,1000),linspace(5,-2,1000),linspace(-2,1/2,1000),linspace(1/2,-2,1000)];
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

plot(defoValues,convergedT,'.k')
plot(defo,T,'.k')
plot(Time,T,'.k')
