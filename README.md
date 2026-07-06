# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
📅 Today's Schedule
========================================
⬜ 06:00 | Luna | Playtime (daily)
⬜ 07:00 | Mochi | Feeding (daily)
⬜ 07:00 | Luna | Feeding (daily)
⬜ 08:00 | Mochi | Morning walk (daily)
⬜ 09:00 | Mochi | Medication (once)

⚠️ Conflict Check
========================================
Conflict at 07:00: Luna - Feeding 
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
========================================== test session starts ==========================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\vidus\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vidus\Downloads\CodePathAI\ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 8 items                                                                                        

tests/test_pawpal.py::test_mark_complete PASSED                                                    [ 12%]
tests/test_pawpal.py::test_add_task_increases_count PASSED                                         [ 25%]
tests/test_pawpal.py::test_sort_by_time PASSED                                                     [ 37%]
tests/test_pawpal.py::test_conflict_detection PASSED                                               [ 50%]
tests/test_pawpal.py::test_no_conflict_different_times PASSED                                      [ 62%]
tests/test_pawpal.py::test_filter_incomplete_tasks PASSED                                          [ 75%]
tests/test_pawpal.py::test_recurring_task_creates_new PASSED                                       [ 87%]
tests/test_pawpal.py::test_pet_with_no_tasks PASSED                                                [100%]

=========================================== 8 passed in 0.05s ===========================================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` |  Sorts all tasks by HH:MM time |
| Filtering |`Scheduler.filter_by_status()` |  Filters tasks by completion status|
| Conflict handling | `Scheduler.detect_conflicts()` |  Warns when two tasks share the same time slot  |
| Recurring tasks | `Scheduler.handle_recurring()` |  Creates a new task for next occurrence when a daily task is completed  |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
