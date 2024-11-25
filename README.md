# Train Ticket Booking System 🚂🎟️

A Python-based console application that simulates a train ticket booking system. It allows users to book tickets interactively while keeping track of the available seats.

## Features
- Dynamic seat selection by the user.
- Real-time seat availability updates.
- User-friendly booking interface with error handling for invalid inputs.

## How It Works
1. The train starts with a fixed number of available seats (default: 400).
2. Users can book a specified number of seats.
3. The system confirms the booking and updates the available seats.
4. If no seats are left, the system informs the user.

## Example Interaction
```plaintext
Do you want to book a seat? (Y/N): Y
Available seats: 400
Enter the number of seats to book: 4
Booking of 4 seat(s) is confirmed!
Do you want to book a seat? (Y/N): N
Thank you for visiting. Have a great day!
