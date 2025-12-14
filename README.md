# FitPlanHub – Django Backend

FitPlanHub is a RESTful backend API built using **Django** and **Django REST Framework**.  
It enables certified trainers to create fitness plans and users to subscribe, follow trainers, and receive AI-based diet recommendations.
The system uses a rule-based AI engine to suggest diet plans based on:
Fitness plan goal (Fat Loss, Muscle Gain, Beginner, etc.)
Plan duration
This architecture is designed to be easily extendable to a Machine Learning model in the future.

# Features

- User & Trainer authentication using JWT
- Role-based access control (Trainer vs User)
- Trainers can create, update, and delete fitness plans
- Users can subscribe to fitness plans (simulated payment)
- Follow / Unfollow trainers
- Personalized feed based on followed trainers

# Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (SimpleJWT)
- **Database**: SQLite (default)
- **Language**: Python
