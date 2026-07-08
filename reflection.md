# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I went with four classes: Task, Pet, Owner, and Scheduler. Task holds one care activity: a description, a due time, which pet it belongs to, a frequency, and a completed flag. Pet holds a name, a species, and its own list of tasks. Owner holds a name and a list of pets. Scheduler is separate from the other three. Its whole job is to look across all of an owner's pets and do things like sorting and conflict checks. I made Task, Pet, and Owner dataclasses since they just hold data. Scheduler is a plain class since it does work instead of storing data.

**b. Design changes**

The biggest change was not really about the classes. It was about file names. My build notes (CLAUDE.md) told me to create diagrams/uml_final.mmd. Before doing that I checked the actual git history for this repo and found a commit from course staff that renamed a similar file to uml.mmd "to match grading expectation." So I switched my plan and used diagrams/uml.mmd instead, since that matched what the real grading setup expected. I also kept the README's existing section headers (like Sample Output and Smarter Scheduling) instead of replacing them, since those were added by that same course staff commit too.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler really only looks at one thing: the time each task is due, written as HH:MM. It sorts tasks using that string directly, and it groups tasks by exact time match to find conflicts. I left out priority, duration, and preferences on purpose. The required features only ask for sorting and conflict detection (plus an optional filter), so adding more constraints would have added extra work without helping those two features.

**b. Tradeoffs**

The main tradeoff is in detect_conflicts(). It only flags two tasks if they share the exact same time. It does not check for overlapping durations. So a walk at 09:00 and a feeding at 09:15 that might realistically overlap would not get flagged. This felt like a reasonable tradeoff since the project spec says to keep conflict detection simple and just check exact duplicate times, and Task does not even store a duration.

---

## 3. AI Collaboration

**a. How you used AI**

I used Claude Code in agent mode for the whole build. It explored the starter repo first to see what already existed, then wrote the four classes in pawpal_system.py, the CLI demo in main.py, the pytest suite, and filled in the UML diagram, README, and this reflection. The most helpful thing was having it check the repo and read files before writing any code, so it did not guess at the file structure or overwrite something I did not expect.

**b. Judgment and verification**

The clearest moment where I did not just accept something as is was the UML file name question. My own instructions said to make diagrams/uml_final.mmd, but instead of trusting that blindly, I had Claude check the real git log first. That is how I found the course staff commit that renamed things to match actual grading. I went with that instead of my own spec. For everything else, I verified it by actually running the code. I ran python main.py to check the schedule, sorting, and conflict output looked right, and I ran python -m pytest to make sure every test passed, instead of just assuming the generated code worked because it looked correct.

---

## 4. Testing and Verification

**a. What you tested**

The tests check four things: that mark_complete() actually flips a task to completed, that adding a task to a Pet increases its task count, that sort_by_time() returns tasks in the right order even when they were added out of order, and that detect_conflicts() correctly flags two tasks at the same time across different pets, and stays quiet when nothing conflicts. These felt like the spots most likely to have small bugs, and they also match what the project asks me to test.

**b. Confidence**

I would give this 4 out of 5 stars. All 5 tests pass, and running main.py gives output that matches what I expected by hand. I feel good about the sorting and conflict logic for the cases it is built to handle. I am dropping a star because there is no test for an owner with zero pets or tasks, and no test checking a conflict between two tasks on the same pet instead of two different pets. Both would be easy to add with more time.

---

## 5. Reflection

**a. What went well**

The Scheduler working across every pet, not just one, came together really cleanly. That is mostly because Owner.get_all_tasks() gives Scheduler one flat list to work with, so it never has to think about pets directly. That one connection made sort_by_time() and detect_conflicts() simple to write.

**b. What you would improve**

I would add the two missing edge case tests I mentioned above before calling the test suite finished. I would also think again about whether Task.frequency should even exist right now. It gets stored but never actually used, since I left recurring tasks out of scope, and an unused field is a small smell in the design.

**c. Key takeaway**

Being the one directing the AI meant my most useful moments were not writing code myself. They were catching a conflict between my own build instructions and what the project actually needed for grading, and making sure I ran the real code instead of trusting that it looked fine. AI is good at producing classes and tests that look right very fast. The human part is deciding which source to trust and checking that the result actually works.
