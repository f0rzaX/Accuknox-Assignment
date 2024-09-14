# Question 3: By default, do Django signals run in the same database transaction as the caller?
"""Answer:
Yes, by default, Django signals run within the same database transaction as the caller. 
If the transaction is rolled back, both the changes made in the caller and the signal handlers will be rolled back together.

Below is the code snippet to Prove the Stance:
"""

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


# Model definitions
class PrimaryModel(models.Model):
    title = models.CharField(max_length=100)


class SecondaryModel(models.Model):
    primary_model = models.ForeignKey(PrimaryModel, on_delete=models.CASCADE)
    extra_info = models.CharField(max_length=100)


# Signal handler for creating a SecondaryModel instance after PrimaryModel is saved
@receiver(post_save, sender=PrimaryModel)
def handle_post_save(sender, instance, **kwargs):
    SecondaryModel.objects.create(primary_model=instance, extra_info="Data from signal")
    print("Post-save signal handler has run")


# Function to attempt saving a PrimaryModel instance within a transaction block
def attempt_save_instance():
    try:
        with transaction.atomic():
            new_instance = PrimaryModel(title="Example")
            new_instance.save()
            print("PrimaryModel instance has been saved")
            # Triggering a rollback
            raise Exception("Triggered a rollback")
    except Exception as error:
        print(f"Error encountered: {error}")


# Call save attempt
attempt_save_instance()

# Verifying the existence of SecondaryModel instances
secondary_instances_count = SecondaryModel.objects.count()
print(f"Count of SecondaryModel instances: {secondary_instances_count}")

# Expected output:
"""
PrimaryModel instance has been saved
Post-save signal handler has run
Error encountered: Triggered a rollback
Count of SecondaryModel instances: 0
"""
