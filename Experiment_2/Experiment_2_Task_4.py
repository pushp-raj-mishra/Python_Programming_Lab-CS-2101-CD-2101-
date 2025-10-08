# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 2: Task 4: Create a complex, nested dictionary representing IIIT Ranchi’s organizational structure.
# (Visit:https://iiitranchi.ac.in/organizational_structure.aspx).
# Write a Python program that accepts the name of an Assistant Professor and iterates through the dictionary to search for that professor. 
# If the name is found, print the department they belong to. 
# If the name is not found at the current level, continue to the next level of the dictionary. 
# If the name is not found in the entire structure, display a message indicating that the Assistant Professor was not found.



iiit_ranchi = {
    "Visitor": {
        "Board of Governors": {
            "Director": {
                "Professor": ["Prof. Rajeev Srivastava"]  
            }
        }
    },
    "Departments": {
        "Computer Science & Engineering": {
            "Professor": [],
            "Associate Professor": [],
            "Assistant Professor": [
                "Dr. Dhananjoy Bhakta",
                "Dr. Jayadeep Pati",
                "Dr. Roshan Singh",
                "Dr. Rashmi Panda",
                "Dr. Bharat Singh",
                "Dr. Priyank Khare",
                "Dr. Kirti Kumari",
                "Dr. Amit Kumar Singh",
                "Dr. Abhinav Kumar",
                "Dr. Ankita Kumari",
                "Dr. Ranjan Kumar Behera",
                "Dr. Rajesh Dwivedi",
                "Dr. Dhiran Kumar Mahto",
                "Dr. Nitika Nigam",
                "Dr. Tarun Biswas",
                "Dr. N Kishore Babu"
            ]
        },
        "Electronics & Communication Engineering": {
            "Professor": [],
            "Associate Professor": [],
            "Assistant Professor": [
                "Dr. Santosh Kumar Mahto",
                "Dr. Shashi Kant Sharma",
                "Dr. Jitendra Kumar Mishra",
                "Dr. Sandhir Kumar Singh",
                "Dr. Rajiv Kumar",
                "Dr. Nishit Malviya",
                "Dr. Priyabrat Garanayak",
                "Dr. Gaurav Sundaram",
                "Dr. Akash Srivastava",
                "Dr. Chandra Prakash Singh"
            ]
        },
        "Sciences (Maths / Physics / Materials etc.)": {
            "Professor": [],
            "Associate Professor": [],
            "Assistant Professor": [
                "Dr. Shashi Kant",
                "Dr. Rohit Kandulna",
                "Dr. Rishikesh Dutta Tiwary",
                "Dr. Puja Ghosh",
                "Dr. Anuj Singh",
                "Dr. Ravi Shanker"
            ]
        },
        "Humanities & Management": {
            "Professor": [],
            "Associate Professor": [],
            "Assistant Professor": [
                "Dr. Noopur"
            ]
        }
    }
}


search_name = input("Enter the faculty name to search: ")

found = False
# 1) check Director/Professor node
for bkey, bval in iiit_ranchi.get("Visitor", {}).items():
    if isinstance(bval, dict):
        for desig, names in bval.items():
            if isinstance(names, list) and search_name in names:
                print(f"{search_name} is a {desig} under {bkey}.")
                found = True

# 2) check departments
if not found:
    for dept, levels in iiit_ranchi["Departments"].items():
        for desig, names in levels.items():
            if isinstance(names, list) and search_name in names:
                print(f"{search_name} is an {desig} in the {dept} department.")
                found = True
                break
        if found:
            break

if not found:
    # fallback message
    print(f"Faculty member '{search_name}' not found in the current structure.")


# Sample Input: Dr. Dhananjoy Bhakta
# Sample Output: Dr. Dhananjoy Bhakta is an Assistant Professor in the Computer Science & Engineering department.