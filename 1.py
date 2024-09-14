# Question 1: By default are Django signals executed synchronously or asynchronously?

""" Answer:
By default, Django signals are executed synchronously. 
This means that when a signal is sent, the execution of the code that 
emitted the signal will wait until all the connected signal handlers have been executed.

Below is the code snippet to Prove the Stance:
"""

import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Model definition
class SampleModel(models.Model):
    title = models.CharField(max_length=100)


# Signal handler for the post_save signal
@receiver(post_save, sender=SampleModel)
def handler_for_post_save(sender, instance, **kwargs):
    print("Beginning of signal handler")
    # Emulating a task that takes time
    time.sleep(5)
    print("End of signal handler")


# Function to create and save a model instance
def create_and_save_instance():
    print("Starting the save process")
    new_instance = SampleModel(title="Example")
    new_instance.save()
    print("Save process completed")


# Call the function
create_and_save_instance()

# Output:
"""
Before saving model instance
Signal handler started
[Waits for 5 seconds]
Signal handler finished
After saving model instance
"""
