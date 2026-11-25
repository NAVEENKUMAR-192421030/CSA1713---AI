
% Employee and Department Database

% Employee facts
employee(arun).
employee(ravi).
employee(kumar).
employee(priya).
employee(john).

% Department facts
department(arun, hr).
department(ravi, hr).
department(kumar, it).
department(priya, it).
department(john, it).

% Manager facts
manager(arun).
manager(priya).

% Manager of each employee
manages(arun, ravi).
manages(priya, kumar).
manages(priya, john).

% Find manager
is_manager(X) :-
    manager(X).

% Find department
get_department(X, D) :-
    department(X, D).

% Find employees working under a manager
works_under(E, M) :-
    manages(M, E).
