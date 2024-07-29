from django.db import models
from django.contrib.auth.models import User
from lesson_4.models import User, Product


# task 7

class CustomerReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reviews/images/', null=True, blank=True)
    email = models.EmailField()
    description = models.TextField()
    rating = models.IntegerField(choices=[(0, "Good"), (1, "Normal"), (2, "Bad")])
    feedback_type = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')])
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product} by {self.user}"
