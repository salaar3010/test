'''
% ----- Rules ----- prolog something 

hobby(Person, Activity) :- likes(Person, Activity), leisure(Activity).
works(Person, Company) :- employed(Person, Company), has_skill(Person, Skill), requires(Company, Skill).
knows(Person1, Person2) :- interacted_professionally(Person1, Person2).
knows(Person1, Person2) :- interacted_socially(Person1, Person2).
plays(Person, Sport) :- participates(Person, Sport).
parent(Person1, Person2) :- biological_parent(Person1, Person2).
parent(Person1, Person2) :- legal_parent(Person1, Person2).
mentors(Person1, Person2) :- works(Person1, Company), works(Person2, Company), professional_relation(Person1, Person2).
manages(Person, Team) :- works(Person, Company), leadership_role(Person, Team).

% ----- Facts -----

employed(alice, alphatech).
employed(bob, alphatech).
employed(charlie, betatech).
employed(dana, betatech).

has_skill(alice, programming).
has_skill(bob, management).
has_skill(charlie, research).
has_skill(dana, swimming).

requires(alphatech, programming).
requires(alphatech, management).
requires(betatech, research).
requires(betatech, swimming).

leisure(swimming).
leisure(painting).
leisure(tennis).
leisure(football).

likes(alice, tennis).
likes(bob, painting).
likes(charlie, swimming).
likes(dana, swimming).

participates(alice, tennis).
participates(charlie, football).

biological_parent(alice, charlie).
biological_parent(bob, charlie).

interacted_professionally(alice, bob).
interacted_socially(alice, charlie).
interacted_professionally(bob, dana).

% ----- Example Queries -----

% (a)
% ?- likes(Person, swimming), works(Person, alphatech).

% (b)
% ?- works(Person, Company), works(alice, Company), plays(Person, tennis).

% (c)
% ?- parent(AliceOrBob, Child), (AliceOrBob = alice; AliceOrBob = bob).

% (d)
% ?- likes(bob, Hobby), likes(Person, Hobby), Person \= bob.

% (e)
% ?- knows(Person, alice), knows(Person, charlie).
'''





''' WUMPUS PROBlEM
# wumpus code
grid_size(4,4).

pit(3, 3).
pit(1, 3).
pit(4, 4).
wumpus(1, 3).
gold(2, 3).

agent(1, 1).

:- dynamic(agent/2).
:- dynamic(wumpus/2).
:- dynamic(gold/2).


% ===================================================================
% PART 2: SENSE RULES (How the Agent Perceives the World)
% ===================================================================

% A square (X,Y) has a breeze if a pit (A,B) is adjacent to it.
breeze(X,Y) :-
    pit(A,B),
    adjacent((A,B), (X,Y)).

% A square (X,Y) has a stench if a wumpus (A,B) is adjacent to it.
stench(X,Y) :-
    wumpus(A,B),
    adjacent((A,B), (X,Y)).

% A square (X,Y) has a glitter if the gold is on that same square.
glitter(X,Y) :-
    gold(X,Y).


% ===================================================================
% PART 3: HELPER RULE (Adjacency Logic)
% ===================================================================

% Defines what it means for two squares to be adjacent (no diagonals).
% (X2,Y2) is adjacent to (X1,Y1) if:
adjacent((X1,Y1), (X2,Y2)) :-
    (X2 is X1 + 1, Y2 is Y1);  % One step right
    (X2 is X1 - 1, Y2 is Y1);  % One step left
    (X2 is X1, Y2 is Y1 + 1);  % One step up
    (X2 is X1, Y2 is Y1 - 1).  % One step down


% ===================================================================
% PART 4: ACTION RULES (How the Agent Interacts with the World)
% ===================================================================

% move(X,Y): Moves the agent to a new, adjacent, safe square.
move(X,Y) :-
    agent(A,B),             % 1. Get current agent location (A,B)
    adjacent((A,B),(X,Y)),  % 2. Check if new location (X,Y) is adjacent
    \+ pit(X,Y),            % 3. Check if there is NOT a pit at (X,Y)
    \+ wumpus(X,Y),         % 4. Check if there is NOT a wumpus at (X,Y)
    
    % If all checks pass, update the agent's position:
    retract(agent(A,B)),    % 5. Remove the old fact
    assert(agent(X,Y)),     % 6. Add the new fact
    
    write('Agent moved to '), write((X,Y)), nl. % 7. Print confirmation

% grab_gold: Picks up the gold if on the same square.
grab_gold :-
    agent(X,Y),             % 1. Get current agent location
    gold(X,Y),              
    write('*** Gold grabbed at '), write((X,Y)), write('! ***'), nl,
    retract(gold(X,Y)).    

% shoot: Kills the wumpus if it is in an adjacent square.
% (Note: This simple version assumes only one wumpus)
shoot :-
    agent(X,Y),                                 % 1. Get current agent location
    adjacent((X,Y),(WumpusX,WumpusY)),          % 2. Find an adjacent square (WumpusX, WumpusY)
    wumpus(WumpusX,WumpusY),                    % 3. Check if the wumpus is actually there
    write('>>> Wumpus shot at '), write((WumpusX,WumpusY)), write('! <<<'), nl,
    retract(wumpus(WumpusX,WumpusY)).            % 4. Remove the wumpus from the world

'''