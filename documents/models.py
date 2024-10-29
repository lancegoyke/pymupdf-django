from django.db import models


class Document(models.Model):
    """Document model."""

    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="documents")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Save the document."""
        if not self.name and self.file:
            self.name = self.file.name
        super().save(*args, **kwargs)
