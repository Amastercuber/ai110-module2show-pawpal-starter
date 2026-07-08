# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I designed around the four classes the project scenario calls for: `Task` (a single care activity — description, due time, pet name, frequency, completed flag), `Pet` (a pet's identity plus the list of `Task`s scheduled for it), `Owner` (a person plus the list of `Pet`s they manage), and `Scheduler` (a separate algorithmic layer that reads across *all* of an owner's pets rather than living inside `Pet` or `Owner`). I kept `Task` and `Pet`/`Owner` as dataclasses since they're simple data containers, and made `Scheduler` a plain class since its job is behavior (sorting, conflict detection), not data storage.

**b. Design changes**

The main design decision I had to make wasn't about the classes themselves but about two file-naming conventions: `CLAUDE.md` (my own build spec) said to create `diagrams/uml_final.mmd`, but I found that the repo's actual git history had a commit from course staff explicitly renaming `uml_draft.mmd` to `uml.mmd` "to match grading expectation." I changed my plan to write to `diagrams/uml.mmd` instead, trusting the real grading-scaffold commit over my own spec's generic phrasing. Similarly, I kept the README's existing section headers (Sample Output, Testing PawPal+, Smarter Scheduling, Demo Walkthrough) instead of restructuring to a more generic list, since those headers were added by the same course-staff "AI grading scaffold" commit.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers only one constraint: the task's due `time`, stored as an `HH:MM` string. It sorts on that string directly (Python string comparison works correctly for zero-padded 24-hour times) and groups tasks by exact time match to find conflicts. I deliberately left out priority, duration, and preference-based scheduling — the required deliverables only ask for sorting and conflict detection (plus an optional filter), and adding more constraints would have added complexity without improving the two required algorithmic features.

**b. Tradeoffs**

The clearest tradeoff is in `detect_conflicts()`: it only flags tasks with the *exact same* time string, not overlapping durations. A 09:00 walk and a 09:15 feeding that might realistically overlap wouldn't be flagged. This is reasonable for this project's scope — the spec explicitly says to keep conflict detection simple and check exact duplicate times rather than overlapping-duration logic, since durations aren't part of the required `Task` data model anyway.

---

## 3. AI Collaboration

**a. How you used AI**

I used Claude Code in agent mode for the whole build: exploring the starter repo to see what already existed, scaffolding the four classes in `pawpal_system.py`, writing the CLI demo in `main.py`, drafting the pytest suite, and filling in the UML diagram, README, and this reflection. The most useful prompting pattern was asking it to inventory the repo first (via a read-only Explore agent) before writing any code, so it didn't guess at file structure or overwrite anything unexpected.

**b. Judgment and verification**

The clearest case of not accepting things at face value was the UML filename question. My own build instructions (`CLAUDE.md`) said to create `diagrams/uml_final.mmd`, but before trusting that, I had Claude check the actual git log of this repo and found a course-staff commit that had renamed a similarly-named file specifically "to match grading expectation." I overrode my own spec's instruction in favor of that real evidence. I verified everything else by actually running the code: `python main.py` to confirm the schedule, sorting, and conflict output looked right, and `python -m pytest` to confirm all tests passed, rather than trusting that generated code was correct just because it looked plausible.

---

## 4. Testing and Verification

**a. What you tested**

The pytest suite covers: (1) that `mark_complete()` actually flips a task's `completed` flag, (2) that adding a task to a `Pet` increases its task count, (3) that `Scheduler.sort_by_time()` returns tasks in chronological order when they were added out of order, and (4) that `Scheduler.detect_conflicts()` correctly flags two tasks (across different pets) sharing a time, and stays quiet when times don't collide. These were the behaviors most likely to have off-by-one or ordering bugs, and they're also exactly what the project rubric asks to verify.

**b. Confidence**

★★★★☆ (4/5). All 5 tests pass, and running `main.py` produces output that matches what I expected by hand. I'm confident in the sorting and conflict logic for the cases it's designed to handle. I'd drop a star because there's no test for an owner with zero pets/tasks (an empty-schedule edge case), and no test confirming conflicts are still detected when the two conflicting tasks belong to the *same* pet rather than different pets — both would be quick to add with more time.

---

## 5. Reflection

**a. What went well**

The `Scheduler` class working across all of an owner's pets (not just one) came together cleanly, mostly because `Owner.get_all_tasks()` gave `Scheduler` one simple flattened list to operate on instead of needing to know about pets directly. That single seam made both `sort_by_time()` and `detect_conflicts()` trivial to write.

**b. What you would improve**

I'd add the two missing edge-case tests noted above (empty owner, same-pet conflicts) before considering the test suite done. I'd also reconsider whether `Task.frequency` should exist at all in this pass — it's stored but never used, since recurring-task automation was out of scope, and an unused field is a small design smell.

**c. Key takeaway**

Being the "lead architect" with AI doing the typing meant my most valuable moments weren't writing code — they were catching a conflict between my own build instructions and the project's actual grading history, and insisting on running the real code instead of trusting that it looked correct. AI is good at producing plausible-looking classes and tests quickly; the human judgment is in deciding which source of truth to trust and verifying the result actually runs.
