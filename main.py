from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner(name="Jordan")

# Create pets
dog = Pet(name="Mochi", species="dog")
cat = Pet(name="Luna", species="cat")

# Add tasks to dog
dog.add_task(Task(description="Morning walk", time="08:00", frequency="daily"))
dog.add_task(Task(description="Feeding", time="07:00", frequency="daily"))
dog.add_task(Task(description="Medication", time="09:00", frequency="once"))

# Add tasks to cat
cat.add_task(Task(description="Feeding", time="07:00", frequency="daily"))
cat.add_task(Task(description="Playtime", time="06:00", frequency="daily"))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler(owner)

# Print today's schedule sorted by time
print("📅 Today's Schedule")
print("=" * 40)
for pet_name, task in scheduler.sort_by_time():
    status = "✅" if task.completed else "⬜"
    print(f"{status} {task.time} | {pet_name} | {task.description} ({task.frequency})")

# Test conflict detection
print("\n⚠️ Conflict Check")
print("=" * 40)
conflicts = scheduler.detect_conflicts()
if conflicts:
    for pet, task, other in conflicts:
        print(f"Conflict at {task.time}: {pet} - {task.description}")
else:
    print("No conflicts found.")