function [ tc, amp ] = fitTimeConst( time, T )

faktor0 = 1;
decayExp0 = 1;

erry = 0.1+0.*T;
Parameter = [faktor0 decayExp0]; % Startwert angeben


decayFun = @(param,ti) param(1).*exp(-ti.*param(2));

Parameter = fastaos(decayFun, Parameter, time, T, 0.*time, erry);

amp = Parameter(1);
tc = 1./Parameter(2);

end