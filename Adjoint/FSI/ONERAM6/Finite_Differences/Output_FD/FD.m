clear;clc;
% FD based sensitivities for ONERA M6 FSI run
E = 40000000000

%%
DeltaE = 5.0e-05;

Cd_p =  0.007411834967287955;
Cl_p =  0.22032618149223016;

Cd_m = 0.007411547958200902;
Cl_m = 0.22032134909866305;

cd_prime = (Cd_p - Cd_m)/(2*DeltaE*E);
cl_prime = (Cl_p - Cl_m)/(2*DeltaE*E);

fprintf("DeltaE = %f9. cd_prime = %.9e \n",DeltaE,cd_prime)
fprintf("\n")
fprintf("DeltaE = %f9. cl_prime = %.9e \n",DeltaE,cl_prime)
fprintf("\n")
fprintf("Dh = %f.\n",2*DeltaE*E)
fprintf("\n")
fprintf("\n")


%%
DeltaE = 1.0e-05;

Cd_p =  0.0074117201658760005;
Cl_p =  0.22032424861148953;

Cd_m = 0.007411662761501192;
Cl_m = 0.2203232821015398;

cd_prime = (Cd_p - Cd_m)/(2*DeltaE*E);
cl_prime = (Cl_p - Cl_m)/(2*DeltaE*E);

fprintf("DeltaE = %f9. cd_prime = %.9e \n",DeltaE,cd_prime)
fprintf("\n")
fprintf("DeltaE = %f9. cl_prime = %.9e \n",DeltaE,cl_prime)
fprintf("\n")
fprintf("Dh = %f.\n",2*DeltaE*E)
fprintf("\n")
fprintf("\n")