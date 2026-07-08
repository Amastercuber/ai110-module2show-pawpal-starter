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

## Classes

PawPal+'s backend (`pawpal_system.py`) is built around four classes:

- **`Task`** — a single pet care activity: a description, a due `time` (HH:MM), which pet it belongs to, a `frequency` (once/daily/weekly), and a `completed` flag. `mark_complete()` marks it done.
- **`Pet`** — a pet's name, species, and the list of tasks scheduled for it. `add_task()` and `list_tasks()` manage that list.
- **`Owner`** — a pet owner and the list of pets they manage. `add_pet()` adds a pet, and `get_all_tasks()` flattens tasks across every pet the owner has.
- **`Scheduler`** — the algorithmic layer. It reads all of an `Owner`'s tasks (across every pet) and can sort them by time, detect scheduling conflicts, and filter by completion status.

This project is intentionally CLI-first: `main.py` is the verified demo of the backend logic. The Streamlit shell in `app.py` is provided as a starter but wiring it up is outside this project's required scope.

## 🖥️ Sample Output

Output from running `python main.py`:

```
Today's Schedule (unsorted)
  14:00 - Give medicine (Luna) [pending]
  09:00 - Feed Luna (Luna) [pending]
  09:30 - Walk Max (Max) [pending]
  08:00 - Feed Max (Max) [pending]
  09:00 - Walk Max (Max) [pending]

Today's Schedule (sorted by time)
  08:00 - Feed Max (Max) [pending]
  09:00 - Feed Luna (Luna) [pending]
  09:00 - Walk Max (Max) [pending]
  09:30 - Walk Max (Max) [pending]
  14:00 - Give medicine (Luna) [pending]

Conflict Warnings
  Conflict at 09:00: Feed Luna and Walk Max

Completed Tasks
  14:00 - Give medicine (Luna) [done]

Pending Tasks
  09:00 - Feed Luna (Luna) [pending]
  09:30 - Walk Max (Max) [pending]
  08:00 - Feed Max (Max) [pending]
  09:00 - Walk Max (Max) [pending]
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest
```

The suite in `tests/test_pawpal.py` covers:
- Marking a task complete updates its status
- Adding a task to a pet increases that pet's task count
- `Scheduler.sort_by_time()` returns tasks in chronological order
- `Scheduler.detect_conflicts()` flags tasks scheduled at the same time (and stays quiet when there's no conflict)

Sample test output:

```
============================= test session starts =============================
platform win32 -- Python 3.13.1, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\documents\Codepath\AI\week5\ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 5 items

tests\test_pawpal.py .....                                               [100%]

============================== 5 passed in 0.04s ==============================
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts all of an owner's tasks chronologically by their `HH:MM` time string |
| Filtering | `Scheduler.filter_by_status(completed)` | Returns tasks filtered by completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Flags tasks scheduled at the exact same time across any of the owner's pets; does not check overlapping durations |
| Recurring tasks | *(not implemented)* | `Task.frequency` exists as a field, but automatic recurrence generation is out of scope for this project's required deliverables |

## 📸 Demo Walkthrough

This project follows a CLI-first workflow — `main.py` is the verified demo of the backend logic:

1. Run `python main.py`.
2. An `Owner` named "Dhruva" is created, along with two `Pet`s, "Luna" and "Max".
3. Several `Task`s are added to each pet out of chronological order, including two tasks that share the same 09:00 time slot.
4. The unsorted task list prints first, showing tasks in the order they were added.
5. `Scheduler.sort_by_time()` prints the same tasks back in chronological order.
6. `Scheduler.detect_conflicts()` prints a warning for the two tasks sharing the 09:00 slot.
7. One task is marked complete, then `Scheduler.filter_by_status()` prints the completed and pending tasks separately.

See the [Sample Output](#️-sample-output) section above for the actual output of this run.

**Screenshot or video** *(optional)*: not included — this project's required demo evidence is the CLI output above.
