import os
import random
from sklearn.model_selection import train_test_split

# Function to load the Enron Spam/Ham dataset
def load_enron_dataset(ham_path, spam_path):
    ham_emails = [open(os.path.join(ham_path, file), encoding="latin-1").read() for file in os.listdir(ham_path)]
    spam_emails = [open(os.path.join(spam_path, file), encoding="latin-1").read() for file in os.listdir(spam_path)]

    ham_labels = [0] * len(ham_emails)
    spam_labels = [1] * len(spam_emails)

    emails = ham_emails + spam_emails
    labels = ham_labels + spam_labels

    return emails, labels

# Function to randomly fetch spam emails from ham dataset
def fetch_spam_from_ham(ham_path, num_spam_to_fetch):
    # Load the Enron Spam/Ham dataset
    emails, labels = load_enron_dataset(ham_path, spam_path)

    # Split the dataset into training and testing sets
    _, X_test, _, _ = train_test_split(emails, labels, test_size=0.2, random_state=42)

    # Randomly select a certain number of emails from the ham dataset to treat as spam
    spam_emails = random.sample(X_test, num_spam_to_fetch)

    return spam_emails

# Specify the paths to ham and spam folders
ham_path = r"C:\Users\muham\OneDrive\Documents\GitHub\Email-Classifier\archive\enron1\ham"
spam_path = r"archive\enron1\spam"

# Specify the number of ham emails to fetch as spam
num_spam_to_fetch = 10

# Fetch spam emails from the ham dataset
spam_emails_from_ham = fetch_spam_from_ham(ham_path, num_spam_to_fetch)

# Print the fetched spam emails
for i, email_content in enumerate(spam_emails_from_ham):
    print(f"Spam Email {i + 1}:\n{email_content}\n{'='*10}\n")
