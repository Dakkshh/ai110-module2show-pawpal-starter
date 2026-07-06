# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
I designed four classes for the system:
- **Task**: holds a single care activity with a description, time, frequency, and completion status.
- **Pet**: stores a pet's name and species, and holds a list of Task objects.
- **Owner**: manages multiple pets and can retrieve all tasks across them.
- **Scheduler**: the brain of the system — takes an Owner and handles sorting, filtering, and conflict detection.

- What classes did you include, and what responsibilities did you assign to each?
Three core actions a user should be able to perform:
1. Add a pet to their profile
2. Schedule a task (feeding, walk, medication) for a pet
3. View today's schedule sorted by time

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
After reviewing the skeleton, one potential bottleneck was that the Scheduler had no way to know which pet a task belonged to after sorting — it would just return a flat list of tasks. To fix this, the get_all_tasks method in Owner was changed to return tuples of (pet_name, task) instead of just tasks, so the Scheduler always knows which pet each task belongs to.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
The scheduler considers time as the main constraint, sorting all tasks by their HH:MM time slot. Time was the most important constraint because pet care tasks like feeding and medication need to happen at specific times of day.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
The scheduler only checks for exact time matches when detecting conflicts, not overlapping durations. This is reasonable for a simple pet care app where most tasks have a clear start time and owners just need a quick warning.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used Claude to help design the class structure, generate the skeleton code, write pytest tests, and debug issues. The most helpful prompts were specific ones like "add a recurring task method to the Scheduler class" rather than vague ones.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
Claude initially suggested the check_guess hints fix by only swapping the message strings, but I realized the outcome labels also feed into other logic. I rejected that suggestion and fixed the full condition instead, then verified by running the tests.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested task completion, task addition, sorting by time, conflict detection, filtering by status, recurring task creation, and edge cases like a pet with no tasks. These were important because they cover all the core scheduler behaviors.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am confident the core features work correctly since all 8 tests pass. Edge cases I would test next include adding tasks with invalid time formats and handling an owner with no pets.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The modular class design worked really well. Having Owner, Pet, Task, and Scheduler as separate classes made it easy to test each piece independently and connect them to the UI cleanly.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would add a priority field to tasks so the scheduler could sort by both time and priority, giving more important tasks preference when there are conflicts.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
AI is a powerful tool for generating code, and giving answers, but you always need to verify its suggestions by running the code yourself. The human has to stay in control of the overall design.
