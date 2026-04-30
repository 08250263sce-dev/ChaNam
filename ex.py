# STEP 1: Generate Unique Value

# Given student IDs (numbers of two students)
student1_id = 8250277      # First student ID (removed leading 0 because Python doesn't allow it)
student2_id = 8250263      # Second student ID

# Extract last two digits of each ID using modulus operator
last_two_1 = student1_id % 100   # Gets last 2 digits of student 1 ID
last_two_2 = student2_id % 100   # Gets last 2 digits of student 2 ID

# Add both last digits and take modulus 10 to get a single digit value
unique_value = (last_two_1 + last_two_2) % 10   # Final unique quiz value

# Display the generated unique value
print("Unique Value Generated:", unique_value)


# STEP 2: Input Student Names

students = {}   # Create an empty dictionary to store student names and scores

# Loop to take multiple student names
while True:
    name = input("Enter student name (type 'exit' to stop): ")  # Ask for name
    
    if name == "exit":   # If user types 'exit', stop the loop
        break
    
    if name == "":   # Check if input is empty
        print("Warning: Name cannot be empty. Skipping...")  # Show warning
        continue   # Skip and ask again
    
    students[name] = 0   # Add student to dictionary with initial score 0


# Display all entered student names
print("List of Students:")
for name in students:   # Loop through dictionary keys
    print(name)   # Print each student name
