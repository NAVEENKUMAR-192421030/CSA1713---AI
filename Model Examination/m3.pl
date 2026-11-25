
% Automobile Fault Diagnosis Expert System

diagnose :-
    write('Enter symptom: '),
    read(Symptom),
    fault(Symptom, Result),
    write('Possible Fault: '),
    write(Result),
    nl.

fault(engine_not_starting, engine_problem).
fault(battery_low, battery_problem).
fault(no_fuel, fuel_problem).
fault(flat_tyre, tyre_puncture).
