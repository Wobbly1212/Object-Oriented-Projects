# Object-Oriented Python Projects

A collection of **Object-Oriented Programming (OOP)** examples in Python. Each subfolder contains a standalone project demonstrating core OOP concepts such as classes, inheritance, and encapsulation. These projects are suitable for beginners or anyone looking to practice Python OOP in a practical context.

---

## Table of Contents

1. [Gym Management System](#gym-management-system)
2. [Blackjack](#blackjack)
3. [Let's Make a Deal](#lets-make-a-deal)
4. [Course Management System](#course-management-system)
5. [How to Run](#how-to-run)
6. [Key Concepts](#key-concepts)
7. [License](#license)

---

## Gym Management System

**Folder**: `gym_management_system/`  
**Script**: `final_oop_project_script_gymnasium.py`

### Overview
- Models a gymnasium that offers different membership plans:
  - **Basic**: Includes weight room and swimming pool only.
  - **Three-Month**: Includes all rooms but requires an additional 10% fee for the climbing wall.
  - **Annual**: Includes all rooms with no additional fee.
- Manages customer data (addition/removal, subscription info).
- Returns a list of customers in alphabetical order.

### Features
- Demonstrates **inheritance** by having multiple membership classes that extend a base `Membership`.
- Incorporates **polymorphism** for room access cost logic.
- Maintains a central `Customer` archive with add/remove operations.

---

## Blackjack

**Folder**: `blackjack/`  
**Script**: `Blackjack_Game.py`

### Overview
- A console-based Blackjack game.
- Uses **classes** for `Card`, `Deck`, and `Hand`.
- Handles dealing, hitting, bust conditions, and comparing final totals.

### Features
- Demonstrates **composition** (a `Deck` composed of `Card` objects; a `Hand` composed of `Card` objects).
- Shows **encapsulation** by keeping card values, suits, and rank details behind methods.

---

## Let's Make a Deal

**Folder**: `lets_make_a_deal/`  
**Script**: `"Let's Make a Deal" game.py`

### Overview
- Python implementation of the classic Monty Hall problem.
- The player chooses one of three doors; the host reveals a goat door; the player can choose to switch or stay.
- Simulates probabilities and outcomes of the Monty Hall scenario.

### Features
- Demonstrates **object-oriented design** via a `Door` class to handle door states and prizes.
- Illustrates **game logic** flow in an OOP context.

---

## Course Management System

**Folder**: `course_management_system/`  
**Script**: `CourseManagementSystem.py`

### Overview
- Illustrates a simplified model of courses, students, or administrative functions (e.g., enrollment, grading, etc.).
- Demonstrates how OOP can structure academic records or similar business logic.

### Features
- Shows **class relationships** (e.g., a `Course` may contain many `Students`, or vice versa).
- Emphasizes **encapsulation** and **data management** within classes.

---

## How to Run

1. **Clone** the repository or **download** the ZIP:
   ```bash
   git clone https://github.com/YourUsername/object-oriented-projects.git
Install Python 3.x (if you haven’t already).
Navigate to the project folder you wish to run:
bash
Copy
cd object-oriented-projects/gym_management_system
python final_oop_project_script_gymnasium.py
Repeat similarly for the other folders:
blackjack/Blackjack_Game.py
lets_make_a_deal/"Let's Make a Deal" game.py
course_management_system/CourseManagementSystem.py
Key Concepts
Classes and Objects: Each project uses custom classes to encapsulate logic and data.
Inheritance: Projects like the Gym Management System show parent-child relationships (Membership → BasicMembership, ThreeMonthlyMembership, AnnualMembership).
Polymorphism: Different membership classes implement cost logic in varied ways.
Encapsulation: Data (like card values or customer details) is hidden within class attributes and accessed through methods.
Composition: The Blackjack game uses multiple Card objects to form a Deck, and multiple Card objects to form a Hand.
License
This repository is distributed for educational purposes. You can adapt the code for your own needs.
(Add a link to your chosen license if applicable, e.g., MIT or GPL.)
