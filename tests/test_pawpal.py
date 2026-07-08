"""Pytest suite for the PawPal+ core system. Run with: python -m pytest"""

from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete():
    task = Task("Feed Luna", "09:00")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_count():
    pet = Pet("Luna", "Dog")
    assert len(pet.list_tasks()) == 0
    pet.add_task(Task("Feed Luna", "09:00"))
    assert len(pet.list_tasks()) == 1


def test_sort_by_time():
    owner = Owner("Dhruva")
    pet = Pet("Luna", "Dog")
    owner.add_pet(pet)
    pet.add_task(Task("Give medicine", "14:00"))
    pet.add_task(Task("Feed Luna", "09:00"))
    pet.add_task(Task("Walk Luna", "11:30"))

    scheduler = Scheduler(owner)
    sorted_times = [task.time for task in scheduler.sort_by_time()]
    assert sorted_times == ["09:00", "11:30", "14:00"]


def test_detect_conflicts():
    owner = Owner("Dhruva")
    luna = Pet("Luna", "Dog")
    max_ = Pet("Max", "Dog")
    owner.add_pet(luna)
    owner.add_pet(max_)

    luna.add_task(Task("Feed Luna", "09:00", pet_name="Luna"))
    max_.add_task(Task("Walk Max", "09:00", pet_name="Max"))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1
    assert "09:00" in conflicts[0]


def test_no_conflicts_when_times_differ():
    owner = Owner("Dhruva")
    pet = Pet("Luna", "Dog")
    owner.add_pet(pet)
    pet.add_task(Task("Feed Luna", "09:00"))
    pet.add_task(Task("Walk Luna", "10:00"))

    scheduler = Scheduler(owner)
    assert scheduler.detect_conflicts() == []
