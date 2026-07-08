# CLI demo script for PawPal+. Run with: python main.py

from pawpal_system import Owner, Pet, Task, Scheduler


def print_tasks(title, tasks):
    print(f"\n{title}")
    if not tasks:
        print("  (no tasks)")
        return
    for task in tasks:
        status = "done" if task.completed else "pending"
        print(f"  {task.time} - {task.description} ({task.pet_name}) [{status}]")


def main():
    owner = Owner("Dhruva")

    luna = Pet("Luna", "Dog")
    max_ = Pet("Max", "Dog")
    owner.add_pet(luna)
    owner.add_pet(max_)

    # Tasks are added out of chronological order on purpose.
    luna.add_task(Task("Give medicine", "14:00", pet_name="Luna"))
    luna.add_task(Task("Feed Luna", "09:00", pet_name="Luna"))
    max_.add_task(Task("Walk Max", "09:30", pet_name="Max"))
    max_.add_task(Task("Feed Max", "08:00", pet_name="Max"))
    # Same time as "Feed Luna" above, to demonstrate conflict detection.
    max_.add_task(Task("Walk Max", "09:00", pet_name="Max"))

    print_tasks("Today's Schedule (unsorted)", owner.get_all_tasks())

    scheduler = Scheduler(owner)

    print_tasks("Today's Schedule (sorted by time)", scheduler.sort_by_time())

    print("\nConflict Warnings")
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            print(f"  {warning}")
    else:
        print("  (no conflicts)")

    # Mark one task complete and show filtering in action.
    owner.get_all_tasks()[0].mark_complete()
    print_tasks("Completed Tasks", scheduler.filter_by_status(completed=True))
    print_tasks("Pending Tasks", scheduler.filter_by_status(completed=False))


if __name__ == "__main__":
    main()
