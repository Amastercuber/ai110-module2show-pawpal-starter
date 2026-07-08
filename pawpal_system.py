"""Core logic layer for PawPal+: Owner, Pet, Task, and Scheduler classes."""

from dataclasses import dataclass, field


@dataclass
class Task:
    """Represents one pet care task, such as a feeding, walk, or medication."""

    description: str
    time: str
    pet_name: str = ""
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet and the tasks scheduled for it."""

    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def list_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents the person who owns and manages one or more pets."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return tasks for all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.list_tasks())
        return all_tasks


class Scheduler:
    """The algorithmic layer that organizes tasks across an owner's pets."""

    def __init__(self, owner):
        self.owner = owner

    def sort_by_time(self):
        """Return all tasks sorted chronologically by their due time."""
        return sorted(self.owner.get_all_tasks(), key=lambda task: task.time)

    def detect_conflicts(self):
        """Return readable warnings for tasks scheduled at the same time."""
        tasks_by_time = {}
        for task in self.owner.get_all_tasks():
            tasks_by_time.setdefault(task.time, []).append(task)

        warnings = []
        for time, tasks in tasks_by_time.items():
            if len(tasks) > 1:
                descriptions = " and ".join(task.description for task in tasks)
                warnings.append(f"Conflict at {time}: {descriptions}")
        return warnings

    def filter_by_status(self, completed):
        """Return all tasks filtered by their completion status."""
        return [task for task in self.owner.get_all_tasks() if task.completed == completed]
