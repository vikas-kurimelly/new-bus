from django.db import models



class Bus(models.Model):
    TELANGANA_CITIES = [
        ('Hyderabad', 'Hyderabad'),
        ('Warangal', 'Warangal'),
        ('Nizamabad', 'Nizamabad'),
        ('Khammam', 'Khammam'),
        ('Karimnagar', 'Karimnagar'),
        ('Ramagundam', 'Ramagundam'),
        ('Mahbubnagar', 'Mahbubnagar'),
        ('Nalgonda', 'Nalgonda'),
        ('Adilabad', 'Adilabad'),
        ('Suryapet', 'Suryapet'),
    ]

    id = models.BigAutoField(primary_key=True)
    BUS_NUMBERS = [(f'TG 76Z {str(i).zfill(4)}{" Express" if i in range(1, 6) else " Deluxe" if i in range(6, 11) else " Super Luxury" if i in range(11, 16) else " EV Bus" if i in range(15, 21) else ""}', f'TG 76Z {str(i).zfill(4)}{" Express" if i in range(1, 6) else " Deluxe" if i in range(6, 11) else " Super Luxury" if i in range(11, 16) else " EV Bus" if i in range(15, 21) else ""}') for i in range(1, 21)]
    bus_name = models.CharField(max_length=30, choices=BUS_NUMBERS)
    source = models.CharField(max_length=30,choices=TELANGANA_CITIES)
    dest = models.CharField(max_length=30, choices=TELANGANA_CITIES)
    SEAT_CHOICES = [
        (40, '40'),
        (50, '50'),
        (60, '60'),
    ]
    nos = models.IntegerField(choices=SEAT_CHOICES)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    
    class Meta:
        verbose_name_plural = "List of Busses"

    def __str__(self):
        return f"{self.bus_name} ({self.source} to {self.dest})"


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "List of Users"

    def __str__(self):
        return self.email
    



class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.CharField(max_length=10)  # Changed to CharField for dd/mm/yyyy format
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    class Meta:
        verbose_name_plural = "List of Books"
    def __str__(self):
        return self.email
