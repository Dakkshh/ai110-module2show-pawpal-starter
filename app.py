import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# Initialize owner in session state so it persists between reruns
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="")

# Owner setup
st.subheader("👤 Owner Info")
owner_name = st.text_input("Your name", value=st.session_state.owner.name)
if owner_name:
    st.session_state.owner.name = owner_name

# Add a pet
st.subheader("🐶 Add a Pet")
col1, col2 = st.columns(2)
with col1:
    pet_name = st.text_input("Pet name")
with col2:
    species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    if pet_name:
        st.session_state.owner.add_pet(Pet(name=pet_name, species=species))
        st.success(f"Added {pet_name} the {species}!")
    else:
        st.warning("Please enter a pet name.")

# Show current pets
if st.session_state.owner.pets:
    st.subheader("📋 Schedule a Task")
    pet_options = [p.name for p in st.session_state.owner.pets]
    selected_pet = st.selectbox("Select pet", pet_options)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_desc = st.text_input("Task description")
    with col2:
        task_time = st.text_input("Time (HH:MM)", value="08:00")
    with col3:
        frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])

    if st.button("Add Task"):
        if task_desc:
            for pet in st.session_state.owner.pets:
                if pet.name == selected_pet:
                    pet.add_task(Task(
                        description=task_desc,
                        time=task_time,
                        frequency=frequency
                    ))
                    st.success(f"Added '{task_desc}' for {selected_pet}!")
        else:
            st.warning("Please enter a task description.")

    # Show schedule
    st.subheader("📅 Today's Schedule")
    scheduler = Scheduler(st.session_state.owner)
    sorted_tasks = scheduler.sort_by_time()

    if sorted_tasks:
        for pet_name, task in sorted_tasks:
            status = "✅" if task.completed else "⬜"
            st.write(f"{status} {task.time} | **{pet_name}** | {task.description} ({task.frequency})")

        # Conflict warnings
        conflicts = scheduler.detect_conflicts()
        if conflicts:
            st.subheader("⚠️ Conflicts Detected")
            for pet, task, other in conflicts:
                st.warning(f"Conflict at {task.time}: {pet} - {task.description}")
    else:
        st.info("No tasks scheduled yet.")
else:
    st.info("Add a pet above to get started!")