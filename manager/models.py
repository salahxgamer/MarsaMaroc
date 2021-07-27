from django.db import models
from django.utils import timezone

SHIFTS_CHOICES = (
    (1, "One (1)"),
    (2, "Two (2)"),
    (3, "Three (3)"),
)

MERCHANDISE_CHOICES = (
    (1, "Conteneur"),
    (2, "Bois"),
    (3, "Blé"),
    (4, "Voiture"),
    (5, "Sucre"),
)
CRANE_CHOICES = (
    (1, "Crane #1"),
    (3, "Crane #3"),
    (4, "Crane #4"),
    (5, "Crane #5"),
    (6, "Crane #6"),
    (7, "Crane #7"),
    (8, "Crane #8"),
    (9, "Crane #9"),
    (10, "Crane #10"),
)

TRACTOR_CHOICES = (
    (1, "Tractor #1"),
    (3, "Tractor #3"),
    (4, "Tractor #4"),
    (5, "Tractor #5"),
    (6, "Tractor #6"),
    (7, "Tractor #7"),
    (8, "Tractor #8"),
    (9, "Tractor #9"),
    (10, "Tractor #10"),
)

ELEVATOR_CHOICES = (
    (1, "Elevator #1"),
    (3, "Elevator #3"),
    (4, "Elevator #4"),
    (5, "Elevator #5"),
    (6, "Elevator #6"),
    (7, "Elevator #7"),
    (8, "Elevator #8"),
    (9, "Elevator #9"),
    (10, "Elevator #10"),
)


class Resource(models.Model):

    name = models.CharField("Name", max_length=20, help_text="Resource name")
    description = models.TextField(
        "Description", blank=True, help_text="Resource description"
    )

    created_at = models.DateTimeField("Creation date", auto_now_add=True)
    modified_at = models.DateTimeField("Modification date", auto_now=True)
    arrived_at = models.DateTimeField("Arriving date", default=timezone.now)
    assigned_at = models.DateTimeField("Assigning date", default=timezone.now)

    shift = models.IntegerField("Shift", choices=SHIFTS_CHOICES)
    merchandise = models.IntegerField("Merchandise", choices=MERCHANDISE_CHOICES)

    crane = models.IntegerField("Crane", choices=CRANE_CHOICES, null=True)
    tractor = models.IntegerField("Tractor", choices=TRACTOR_CHOICES, null=True)
    elevator = models.IntegerField("Elevator", choices=ELEVATOR_CHOICES, null=True)

    # Metadata
    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.name
