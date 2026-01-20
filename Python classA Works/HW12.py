"""You are building a simple customer feedback system for a local restaurant. The system should ask users to enter their name and feedback. Your task is to:
Ask the user to enter their name and feedback.
If the user leaves the name or feedback empty, display an error message using exception handling.
If all inputs are valid, print a thank-you message along with the user's name and feedback.
Use the try, except, and finally blocks to structure your code safely.

"""
try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()

   
    if not name or not feedback:
        raise ValueError("Name and feedback cannot be empty.")

except ValueError as e:
    print("Error:", e)

else:
    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

finally:
    print("\n--- Feedback process completed ---")
