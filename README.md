# Portfolio Website with Contact Form

![Portfolio Screenshot](images/2.png)

A modern portfolio website built with Python and Streamlit to showcase projects and skills, featuring a functional contact form that sends emails directly to your inbox.

## Features

- **Professional Profile Display**: Clean two-column layout showcasing your bio and photo
- **Project Gallery**: Responsive grid displaying your projects with:
  - Descriptive titles
  - Detailed descriptions 
  - Project screenshots
  - Direct links to source code
- **Functional Contact Form**:
  - Email validation
  - Message submission
  - SMTP email delivery
  - User feedback notifications
- **Responsive Design**: Adapts to all screen sizes

## Technologies Used

- ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
- ![Streamlit](https://img.shields.io/badge/Streamlit-1.32.2-FF4B4B?logo=streamlit)
- ![Pandas](https://img.shields.io/badge/Pandas-2.1.4-150458?logo=pandas)
- SMTP/Email integration
- Environment variables for security

## Project Structure
    portfolio-website/
    ├── main.py # Main application
    ├── pages/
    │ └── Contact Us.py # Contact form page
    ├── Send_Email.py # Email handling
    ├── data.csv # Project metadata
    ├── images/ # All visual assets
    │ ├── 1.png # Project screenshots
    │ ├── 2.png
    │ └── photo.jpeg # Profile photo
    ├── .env.example # Environment template
    └── requirements.txt # Dependencies


## Setup Instructions
### Clone the repository:
```bash
   git clone https://github.com/yourusername/portfolio-website.git
   cd portfolio-website
   pip install -r requirements.txt
   Install dependencies:
```
```bash
   pip install -r requirements.txt
```
### Configure email:
    <br>Create .env file:<br>
    <br>EMAIL_USER=your@gmail.com<br>
    <br>EMAIL_PASSWORD=your_app_password<br>
    <br>EMAIL_RECEIVER=your@gmail.com<br>
    <br>Enable Gmail SMTP access<br>
### Run the application:
```bash
    streamlit run main.py
    Live Demo
    The portfolio is deployed on Streamlit Cloud: https://app2portfolio-fbvzmenkuga3dbwxzfphvk.streamlit.app/
```