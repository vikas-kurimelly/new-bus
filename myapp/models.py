from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User

class Bus(models.Model):
    TELANGANA_CITIES = [
        ('Hyderabad', 'Hyderabad'),
        ('Warangal', 'Warangal'),
        ('Nizamabad', 'Nizamabad'),
        ('Khammam', 'Khammam'),
        ('Karimnagar', 'Karimnagar'),
        ('Ramagundam', 'Ramagundam'),
        ('Medak', 'Medak'),
        ('Nalgonda', 'Nalgonda'),
        ('Adilabad', 'Adilabad'),
        ('Sircilla', 'Sircilla'),
    ]

    id = models.BigAutoField(primary_key=True)
    BUS_NUMBERS = [(f'TG 76Z {str(i).zfill(4)}{" Express" if i in range(1, 11) else " Deluxe" if i in range(11, 21) else " Super Luxury" if i in range(21, 31) else " EV Bus" if i in range(31, 41) else ""}', f'TG 76Z {str(i).zfill(4)}{" Express" if i in range(1, 11) else " Deluxe" if i in range(11, 21) else " Super Luxury" if i in range(21, 31) else " EV Bus" if i in range(31, 41) else ""}') for i in range(1, 41)]; express_buses = [bus for bus in BUS_NUMBERS if "Express" in bus[0]][:10]; deluxe_buses = [bus for bus in BUS_NUMBERS if "Deluxe" in bus[0]][:10]; super_luxury_buses = [bus for bus in BUS_NUMBERS if "Super Luxury" in bus[0]][:10]; ev_buses = [bus for bus in BUS_NUMBERS if "EV Bus" in bus[0]][:10]; all_buses = express_buses + deluxe_buses + super_luxury_buses + ev_buses
    bus_name = models.CharField(max_length=30, choices=BUS_NUMBERS)
    source = models.CharField(max_length=30, choices=TELANGANA_CITIES)
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
        verbose_name_plural = "List of Buses"

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
    BOOKED = 'BOOKED'
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'

    TICKET_STATUSES = (
        (BOOKED, 'BOOKED'),
        (CONFIRMED, 'CONFIRMED'),
        (CANCELLED, 'CANCELLED'),
    )

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid = models.DecimalField(decimal_places=0, max_digits=4)
    busid = models.DecimalField(decimal_places=0, max_digits=4)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.CharField(max_length=10)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=10)

    class Meta:
        verbose_name_plural = "List of Books"

    def __str__(self):
        return self.email

    def status_as_button(self):
        """Renders the ticket status as traffic light buttons."""
        if self.status == self.BOOKED:
            color = "yellow"
        elif self.status == self.CONFIRMED:
            color = "green"
        elif self.status == self.CANCELLED:
            color = "red"
        else:
            color = "grey"

        return format_html(
            f'<button style="background-color: {color}; color: white; padding: 5px 10px; border: none; border-radius: 5px;">{self.get_status_display()}</button>'
        )


class ContactMessage(models.Model):
    email = models.EmailField()
    issue = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.email} - {self.issue[:50]}"
