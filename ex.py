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
# STEP 3: Quiz Section

# Loop through each student to conduct quiz
for name in students:
    print(f"Quiz for {name}")   # Show whose quiz it is
    score = 0   # Start score from 0

    # Question 1
    ans1 = int(input(f"Q1: {unique_value} + 2 = "))   # Take answer
    if ans1 == unique_value + 2:   # Check correct answer
        score += 1   # Increase score if correct

    # Question 2
    ans2 = int(input(f"Q2: {unique_value} * 3 = "))   # Take answer
    if ans2 == unique_value * 3:   # Check correct answer
        score += 1   # Increase score if correct

    # Question 3
    ans3 = int(input(f"Q3: {unique_value} + 5 = "))   # Take answer
    if ans3 == unique_value + 5:   # Check correct answer
        score += 1   # Increase score if correct

    students[name] = score   # Store final score of the student


# STEP 4: Performance Analysis

print("Results")   # Display result heading

# Loop through each student and their score
for name, score in students.items():
    print(f"{name}'s Score:", score)   # Show student score

    # Warning if score is 0
    if score == 0:
        print("Warning: Very low performance!")   # Show warning

    # Performance Level based on score
    if score == 3:
        print("Performance: Excellent")
    elif score == 2:
        print("Performance: Good")
    elif score == 1:
        print("Performance: Average")
    else:
        print("Performance: Poor")

    # Check if student is eligible for certificate
    if score >= 2:
        print("Certificate: Eligible")
    else:
        print("Certificate: Not Eligible")

    # STEP 5: Star Pattern

    print("Star Pattern:")   # Display star pattern heading
    
    if score == 0:
        print("")   # Print blank if no score
    else:
        print("*" * score)   # Print stars equal to score
