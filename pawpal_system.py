from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional

@dataclass
class Task:
    """Represents a single pet care task."""
    description: str
    time: str  # format "HH:MM"
    frequency: str  # "daily", "weekly", or "once"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet with a list of tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)


@dataclass
class Owner:
    """Represents a pet owner who manages multiple pets."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks


class Scheduler:
    """Organizes and manages tasks across all pets."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self):
        """Return all tasks sorted by time."""
        all_tasks = self.owner.get_all_tasks()
        return sorted(all_tasks, key=lambda x: x[1].time)

    def filter_by_status(self, completed: bool):
        """Filter tasks by completion status."""
        return [(pet, task) for pet, task in self.owner.get_all_tasks()
                if task.completed == completed]

    def detect_conflicts(self):
        """Return list of tasks that share the same time slot."""
        all_tasks = self.owner.get_all_tasks()
        times = {}
        conflicts = []
        for pet, task in all_tasks:
            if task.time in times:
                conflicts.append((pet, task, times[task.time]))
            else:
                times[task.time] = (pet, task)
        return conflicts
    
    def handle_recurring(self):
        """Create a new task for the next day if a daily task is completed."""
        from datetime import date, timedelta
        new_tasks = []
        for pet in self.owner.pets:
            for task in pet.tasks:
                if task.completed and task.frequency == "daily":
                    next_task = Task(
                        description=task.description,
                        time=task.time,
                        frequency=task.frequency,
                        completed=False
                    )
                    new_tasks.append((pet, next_task))
        for pet, task in new_tasks:
            pet.add_task(task)
        return new_tasks