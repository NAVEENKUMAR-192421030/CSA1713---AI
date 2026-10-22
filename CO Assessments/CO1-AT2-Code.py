
# Constraint-Based Exam Scheduling using CSP
# Methods: Plain Backtracking and Forward Checking

courses = ['A', 'B', 'C', 'D', 'E']
slots = ['Slot1', 'Slot2', 'Slot3']

conflicts = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('C', 'E'),
    ('D', 'E')
]

names = {
    'A': 'Artificial Intelligence',
    'B': 'Database Systems',
    'C': 'Computer Networks',
    'D': 'Operating Systems',
    'E': 'Software Engineering'
}


# Check whether assigning a slot causes a conflict
def is_consistent(course, slot, assignment):
    for c1, c2 in conflicts:
        if c1 == course and c2 in assignment:
            if assignment[c2] == slot:
                return False

        if c2 == course and c1 in assignment:
            if assignment[c1] == slot:
                return False

    return True


# Method 1: Plain Backtracking
def backtracking(assignment):
    if len(assignment) == len(courses):
        return assignment.copy()

    course = courses[len(assignment)]

    for slot in slots:
        print("Trying", course, "=", slot)

        if is_consistent(course, slot, assignment):
            assignment[course] = slot

            result = backtracking(assignment)

            if result is not None:
                return result

            print("Backtracking from", course, "=", slot)
            del assignment[course]

        else:
            print("Conflict detected!")

    return None


# Method 2: Backtracking with Forward Checking
def forward_checking(assignment, domains):
    if len(assignment) == len(courses):
        return assignment.copy()

    course = courses[len(assignment)]

    for slot in slots:
        if slot not in domains[course]:
            continue

        print("Trying", course, "=", slot)

        if not is_consistent(course, slot, assignment):
            print("Conflict detected!")
            continue

        assignment[course] = slot

        # Create a copy of all domains
        new_domains = {
            c: domains[c][:]
            for c in courses
        }

        failed = False

        # Remove the selected slot from conflicting courses
        for c1, c2 in conflicts:
            if c1 == course and c2 not in assignment:
                if slot in new_domains[c2]:
                    new_domains[c2].remove(slot)

            elif c2 == course and c1 not in assignment:
                if slot in new_domains[c1]:
                    new_domains[c1].remove(slot)

        print("Domains after assigning", course, "=", slot)

        # Check whether any unassigned course has an empty domain
        for c in courses:
            if c not in assignment:
                print(c, ":", new_domains[c])

                if len(new_domains[c]) == 0:
                    failed = True

        if not failed:
            result = forward_checking(assignment, new_domains)

            if result is not None:
                return result

        print("Backtracking from", course, "=", slot)
        del assignment[course]

    return None


# Display the final timetable
def display_timetable(solution):
    print("\nFinal Examination Timetable")
    print("-" * 50)
    print("{:<30} {}".format("Course", "Exam Slot"))
    print("-" * 50)

    for course in courses:
        print("{:<30} {}".format(
            names[course], solution[course]
        ))

    print("-" * 50)


# Main program
print("\nPLAIN BACKTRACKING SEARCH")
print("=" * 50)

solution1 = backtracking({})

if solution1 is not None:
    display_timetable(solution1)
else:
    print("No valid timetable found.")


print("\nBACKTRACKING WITH FORWARD CHECKING")
print("=" * 50)

initial_domains = {
    course: slots[:]
    for course in courses
}

solution2 = forward_checking({}, initial_domains)

if solution2 is not None:
    display_timetable(solution2)
else:
    print("No valid timetable found.")
