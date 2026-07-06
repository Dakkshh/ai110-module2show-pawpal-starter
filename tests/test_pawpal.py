from pawpal_system import Owner, Pet, Task, Scheduler

def test_mark_complete():
    task = Task(description="Walk", time="08:00", frequency="daily")
    task.mark_complete()
    assert task.completed == True

def test_add_task_increases_count():
    pet = Pet(name="Mochi", species="dog")
    task = Task(description="Feeding", time="07:00", frequency="daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1

def test_sort_by_time():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    pet.add_task(Task(description="Walk", time="09:00", frequency="daily"))
    pet.add_task(Task(description="Feeding", time="07:00", frequency="daily"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    assert sorted_tasks[0][1].time == "07:00"

def test_conflict_detection():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    pet.add_task(Task(description="Walk", time="08:00", frequency="daily"))
    pet.add_task(Task(description="Feeding", time="08:00", frequency="daily"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) > 0

def test_no_conflict_different_times():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    pet.add_task(Task(description="Walk", time="08:00", frequency="daily"))
    pet.add_task(Task(description="Feeding", time="09:00", frequency="daily"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 0

def test_filter_incomplete_tasks():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    pet.add_task(Task(description="Walk", time="08:00", frequency="daily"))
    pet.add_task(Task(description="Feeding", time="07:00", frequency="daily", completed=True))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    incomplete = scheduler.filter_by_status(completed=False)
    assert len(incomplete) == 1

def test_recurring_task_creates_new():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    task = Task(description="Walk", time="08:00", frequency="daily")
    task.mark_complete()
    pet.add_task(task)
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    scheduler.handle_recurring()
    incomplete = scheduler.filter_by_status(completed=False)
    assert len(incomplete) == 1

def test_pet_with_no_tasks():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    assert len(sorted_tasks) == 0