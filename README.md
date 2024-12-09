# **ZeroSpamAI - Spam Email Classification Web APP**

## **Project Overview**
ZeroSpam-AI is a web application that uses machine learning algorithms to classify emails as spam or not spam. Built with **Django**, **React**, **MySQL**, and **Naive Bayes (MultinomialNB) machine learning** models, the app allows users to input email text, get predictions, and view results in a responsive, user-friendly interface.

This project aims to provide an easy-to-use system that can detect unwanted emails, enhancing user experience and productivity.

---

## **Features**
- **Email Classification**: Classifies emails into **Spam** or **Not Spam** based on the text provided.
- **Responsive UI**: Built with React, the app is fully responsive and provides a seamless experience across devices.
- **Machine Learning Integration**: The backend uses a trained machine learning model to classify email content.
- **Real-time Prediction**: Provides immediate feedback on the email's status as spam or not when users submit the content.

---


## 📊 Screenshots and Demo Video
 ### **Screenshots**

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=11BzbepXBSGG8bAhaRxf-aKSskHqz_I75" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1nLNypCZk7C83pg3Lpg47a2nkvfasgnHU" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1c8o5_-SF5BVmc0sHRL6byUdGVpuBj88P" alt="img" width="160" style="margin: 5px;">
</p>

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1zcAtKWXy1Uc3kPkw1C1DmPqKzMFJTfNl" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1EragUXTMt3EvtHUQ6o6NFrbT_hJEFJeB" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1QI2Ji02CsIucGOPe7lsu9gSGSFeRdnFF" alt="img" width="160" style="margin: 5px;">
</p>

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1V9tn-6vKAEC4zvM9G0CLeKo0soa5d5-g" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1mVjfVYCGOjeIHUwpsc86rL18x7aP0X50" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1657WdbHQcSD0-KEhsZusb2vtGOHEuK1a" alt="img" width="310" style="margin: 5px;">
</p>

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1fX4e65lJRQaTzb_TN2sTYX9zOHnFjRTH" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1LMYtm-MsMVr2zJbLQzsrG7TsVYSp8Dat" alt="img" width="310" style="margin: 5px;">
  <img src="https://drive.google.com/uc?export=view&id=1cpd5_N3BOMQbZi86voo8pzHvbxUWyw0P" alt="img" width="310" style="margin: 5px;">
</p>

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1LmDWMzdZS_EJ6TDXgAW0yW4BpyOuTuqZ" alt="img" width="310" style="margin: 5px;">
</p>

 ### **Video**
**Project Video**

Click the image below to watch the project video

[![Watch the video](https://drive.google.com/uc?export=view&id=11BzbepXBSGG8bAhaRxf-aKSskHqz_I75)](https://drive.google.com/file/d/1ogBxu9EQsf8ZXFuQ0SmHYSM4n5LH30Gc/view?usp=drive_link)


---

## **Technologies Used**
- **Frontend**:
  - React.js for building interactive UIs
  - Axios for API requests to the Django backend
- **Backend**:
  - Django for backend development and API creation
  - Python for implementing the machine learning model (Spam classification)
  - MySQL for storing email data and results
- **Machine Learning**:
  - Scikit-learn Machine Learning library
  - Naive Bayes (MultinomialNB) algorithm for classification of spam email
---

## **Installation**

### **1. Clone the Repository**
- To get started, clone the repository to your local machine:
  ```bash
      git clone https://github.com/your-username/ZeroSpamAI.git
   cd ZeroSpamAI

### **2. Setup Backend (Django + MySQL)**
- **Install the necessary packages for Django**
  ```bash
  cd zerospamai_backend
  pip install -r requirements.txt

- **Setup MySQL**
    - Create a MySQL database (e.g., zero_spam_ai_db).
    - Configure the MySQL connection in backend/settings.py.

- **Apply database migrations**
  ```bash
  python manage.py migrate

- **Start the Django server**
  ```bash
  python manage.py runserver


### **3. Setup Frontend (React)**
    cd zerospamai_frontend
    npm install
    npm start

-Your application should now be running at http://localhost:3000.


---

## **Usage**
- **Email Input**:
  - In the main UI, users can type or paste email content into the provided textarea and click the "Analyze" button.
- **Results**:
  - Upon submission, the email's spam classification will be shown below the input field, with a message indicating whether the email is Spam or Not Spam.
- **Responsive UI**:
  - The design adapts to different screen sizes, ensuring that the app is accessible on mobile devices, tablets, and desktops.

    
---

## **Testing the Application**
- Enter various email texts in the input box.
- Check the displayed result to verify if the model accurately classifies spam and non-spam emails.
    
---


## **Contribution**
**Contributions are welcome! If you'd like to improve or fix any part of the project, feel free Contribute.**
- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request
    
---


## **Contact**

- [LinkedIn](https://www.linkedin.com/in/sambhaji-shinde-1679ab309/)
- [Instagram](https://www.instagram.com/sambhaji_26/)
