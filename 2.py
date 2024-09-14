# Question 2: Do Django signals run in the same thread as the caller?
"""Answer:
Yes, Django signals run in the same thread as the caller by default. 
This means that both the code that emits the signal and the signal handlers execute within the same thread context.

Below is the code snippet to Prove the Stance:
"""

import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Model definition
class SampleModel(models.Model):
    title = models.CharField(max_length=100)


# Signal handler definition
@receiver(post_save, sender=SampleModel)
def handle_post_save(sender, instance, **kwargs):
    print(f"Handler's thread ID: {threading.get_ident()}")


# Function to create and save a model instance
def create_and_save_instance():
    print(f"Initiating thread ID: {threading.get_ident()}")
    new_instance = SampleModel(title="Example")
    new_instance.save()


# Call the function
create_and_save_instance()

# Expected Output:
"""
Initiating thread ID: [Thread ID]
Handler's thread ID: [Same Thread ID]
"""
