from django.db import models


class Volunteer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    skills = models.TextField(blank=True, help_text="List your skills (separate multiple skills with commas, or just one is fine)")
    availability = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g., Weekends, Evenings, Flexible"
    )
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def skill_list(self):
        return [skill.strip() for skill in self.skills.split(',') if skill.strip()]
