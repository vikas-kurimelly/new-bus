# Bus Reservation System

A web-based bus reservation system built using Django. This project allows users to book bus tickets online, view available buses,cancel the tickets and manage reservations.

## Features

- User authentication and authorization
- Search for Buses
- Online bus ticket booking
- Ticket Management
- Admin dashboard for managing buses and reservations
- Responsive design for mobile and desktop
- Ticket Cancellation

## Technology Used

- Python
- Django
- Bootstarp

## Execution

1. **Install dependencies**:

    pip install -r requirements.txt

2. **Apply migrations**:

    python manage.py migrate

3. **Create a superuser**:

    python manage.py createsuperuser

4. **Run the development server**:

    python manage.py runserver

## Usage

- **User Registration and Login**: Users can register for an account and log in to book tickets.
- **Bus Search**: Users can search for available buses based on routes and dates.
- **Booking Tickets**: Logged-in users can book tickets for their selected routes.
- **View Bookings**: Users can view their booked tickets and reservation history.
- **Ticket Cancellation**: Users can cancel the tickets booked by them.
- **Admin Dashboard**: Admins can manage buses, routes, and reservations through the Django admin interface.
