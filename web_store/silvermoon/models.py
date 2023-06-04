from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
    
class Subgenre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
    
class Visual(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
    
class Theme(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
    
class Feature(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
    
class PlayersType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    releaseDate = models.DateField()
    score = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    description = models.TextField(max_length=5000)
    developer = models.CharField(max_length=500)
    image = models.ImageField(blank=True)
    
    
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL, related_name="games")
    subgenre = models.ForeignKey(Subgenre, null=True, blank=True, on_delete=models.SET_NULL, related_name="games")
    visual = models.ForeignKey(Visual, null=True, blank=True, on_delete=models.SET_NULL, related_name="games")
    theme = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.SET_NULL, related_name="games")
    feature = models.ForeignKey(Feature, null=True, blank=True, on_delete=models.SET_NULL, related_name="games")
    playersType = models.ForeignKey(PlayersType, null=True, blank=True, on_delete=models.SET_NULL, related_name="games")

    def __str__(self):
        return f"{self.title}"
    
class Order(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    ORDERED = "O"
    READY = "R"
    COMPLETED = "C"
    STATUS_OPTIONS = [
        (ORDERED, "Ordered"),
        (READY, "Ready"),
        (COMPLETED, "Completed"),
    ]
    
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS,default=ORDERED)
    games = models.ManyToManyField(Game, through="OrderGame")

    def __str__(self):
        return f"{self.id}"
    
class OrderGame(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.order.id} {self.game.title}"
    
    class Meta:
        unique_together = [['order', 'game']]
