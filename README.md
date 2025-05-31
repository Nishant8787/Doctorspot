# DoctorSpot - AI-Powered Medical Prediction Platform

DoctorSpot is a comprehensive Django-based web application that provides AI-powered predictions for various health conditions. The platform allows users to input their health parameters and receive instant predictions for conditions such as blood pressure issues, cancer risk, thyroid conditions, and more.

## Features

- **User Authentication**: Secure signup and login system
- **Multiple Disease Predictions**: 
  - Blood Pressure prediction
  - Cancer risk assessment
  - Thyroid condition prediction
  - Asthma prediction
  - Lung disease prediction
  - Diabetes prediction
  - Kidney stone prediction
  - Liver disease prediction
- **Prediction History**: Users can view their past predictions
- **User Profiles**: Update profile information and profile pictures
- **Responsive Design**: Works on all device sizes

## Technology Stack

- **Backend**: Django (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **AI/ML**: scikit-learn (simplified models for demonstration)

## Setup Instructions

### Prerequisites
- Python 3.8+
- MySQL
- pip (Python package manager)

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/doctorspot.git
cd doctorspot
```

2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```

4. Set up your MySQL database and update the `.env` file with your credentials

5. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```
python manage.py createsuperuser
```

7. Run the development server:
```
python manage.py runserver
```

8. Visit `http://127.0.0.1:8000/` in your browser

## Project Structure

- `doctorspot/`: Main project settings
- `users/`: User authentication and profiles
- `predictions/`: Disease prediction models and views
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)
- `media/`: User-uploaded files
- for review just visit this link - https://doctorspot-1.onrender.com

## Design and Images
![Image](https://github.com/user-attachments/assets/d5d6720b-8561-4d31-a186-409c4a7089b4)
![Image](https://github.com/user-attachments/assets/5baf6497-cbe9-4589-9edd-0feaba57f849)
![Image](https://github.com/user-attachments/assets/e842c731-a189-4364-a097-b7624591bfcd)
![Image](https://github.com/user-attachments/assets/c6d7cc3e-f0b1-463f-b4d8-f76b4e2fe096)
![Image](https://github.com/user-attachments/assets/d3b7786f-9d9f-4aaf-a23c-06764d5fa14d)
![Image](https://github.com/user-attachments/assets/c8aa0a30-f406-4de0-8387-419b5da43e5c)




## Important Note

This application is for educational and demonstration purposes only. The prediction models used are simplified and not meant for actual medical diagnosis. Always consult with a qualified healthcare provider for proper diagnosis and treatment of medical conditions. And I dont have any database for hosting im unable to give you link to check my website in working condition properly but you can clone and check in your local system and for website UI and functionality you can visit my render.com profile link which ive mentioned(https://doctorspot-1.onrender.com).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
