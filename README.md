# 🎟️ EventHub API

A backend REST API built using **Django** and **Django REST Framework (DRF)** for a simplified event ticketing platform. The application allows users to browse events, reserve seats, cancel reservations, and prevents overbooking by validating seat availability.

---

# 📌 Features

- Create, update, retrieve, and delete events
- Reserve seats for an event
- Automatically deduct available seats after a successful reservation
- Prevent overbooking
- Cancel reservations and restore available seats
- Filter events by status and venue
- Filter reservations by event
- Request logging using custom middleware

---

# 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite3
- Django ORM

---

# 📂 Project Structure

```
eventhub/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── eventhub/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── events/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── middleware.py
│   ├── admin.py
│   └── urls.py
│
└── README.md
```

---

# 🚀 How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
cd eventhub
```

---

## Step 2: Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

### Activate

```bash
venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If the requirements file is not available:

```bash
pip install django djangorestframework
```

---

## Step 4: Apply Database Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Step 5: Start the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to

```
http://127.0.0.1:8000/
```

---

# 📡 API Endpoints

## Event Endpoints

### 1. Create Event

**POST**

```
/api/events/
```

Creates a new event.

---

### 2. List All Events

**GET**

```
/api/events/
```

Returns all available events.

---

### 3. Retrieve an Event

**GET**

```
/api/events/{id}/
```

Returns details of a specific event.

---

### 4. Update an Event

**PUT / PATCH**

```
/api/events/{id}/
```

Updates an existing event.

---

### 5. Delete an Event

**DELETE**

```
/api/events/{id}/
```

Deletes an event.

---

### 6. Filter Events by Status

**GET**

```
/api/events/?status=upcoming
```

Returns events based on their status.

Supported values:

- upcoming
- ongoing
- completed
- cancelled

---

### 7. Filter Events by Venue

**GET**

```
/api/events/?venue=bangalore
```

Returns events whose venue matches the given search text.

---

# Reservation Endpoints

### 1. Create Reservation

**POST**

```
/api/reservations/
```

Creates a reservation for an event.

During reservation:

- Checks event status
- Checks seat availability
- Deducts available seats automatically
- Returns reservation details

---

### 2. List Reservations

**GET**

```
/api/reservations/
```

Returns all reservations.

---

### 3. Retrieve Reservation

**GET**

```
/api/reservations/{id}/
```

Returns details of a reservation.

---

### 4. Update Reservation

**PUT / PATCH**

```
/api/reservations/{id}/
```

Updates reservation details.

---

### 5. Delete Reservation

**DELETE**

```
/api/reservations/{id}/
```

Deletes a reservation.

---

### 6. Filter Reservations by Event

**GET**

```
/api/reservations/?event_id=1
```

Returns reservations belonging to a specific event.

---

### 7. Cancel Reservation

**POST**

```
/api/reservations/{id}/cancel/
```

Cancels an existing reservation.

The API automatically:

- Changes reservation status to **Cancelled**
- Restores seats back to the event
- Returns the updated reservation

---

# ✅ Request Validation

The application validates the following:

- Available seats cannot exceed total seats.
- At least one seat must be reserved.
- Reservations are allowed only for Upcoming or Ongoing events.
- Overbooking is prevented.
- Already cancelled reservations cannot be cancelled again.

---

# 📋 Design Decision

## Waitlist for Fully Booked Events

A key design consideration for this project is the introduction of a **Waitlist System** as a future enhancement.

Currently, when all seats for an event are reserved, the API returns a **400 Bad Request** indicating that no seats are available. While this prevents overbooking and maintains data integrity, it also means interested users lose the opportunity to attend if seats become available later.

To improve the user experience, a waitlist mechanism can be introduced. Instead of rejecting requests outright, users could opt to join a waitlist when an event is fully booked. If an existing reservation is cancelled, the system could automatically allocate the newly available seats to users on the waitlist in the order they joined.

This approach offers several benefits:

- Improves user satisfaction by providing another chance to attend the event.
- Maximizes event occupancy by quickly filling cancelled seats.
- Creates a scalable foundation for future features such as email notifications and automatic reservation confirmation.

---

# 📸 API Screenshots

## 1. Successful Reservation (201 Created)
<img width="1571" height="872" alt="image" src="https://github.com/user-attachments/assets/563ba030-cf7a-426a-91c7-38e0ab604536" />


---

## 5. Overbooking Error (400 Bad Request)
<img width="1555" height="732" alt="image" src="https://github.com/user-attachments/assets/e02ee326-71dc-4195-bda5-6ccc01aa3573" />


---

## 6. Cancel Reservation
<img width="1576" height="872" alt="image" src="https://github.com/user-attachments/assets/e2b9415b-5cc7-481c-9069-f37331ff5b2a" />


---
# 👨‍💻 Author

**Kothandaramar Sivakumar**
