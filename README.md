# Consultancy project - Firm management system

This is the desktop application for the firm management system. This project is developed using python Tkinter and used MongoDB for database. Python is used for backend as well. 

# Installation:
	The project can run in Python 3.6 and above.
	
# Clone the repository
```
git clone https://github.com/prathishbv/Firm-Management-System.git
```

# Navigate to the dist folder by giving
```
cd FirmManagementSystem/figma/dist/main.exe
```

# Install the requirements if you need to  execute them as python files for reference:
```
pip install requirements.txt
```

# File Structure and explanation 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We have used Figma to design all the pages used in this application. This application requires a username and password to log in. By verifying in the database the user will be either logged in as auditor or article assistant based on their credentials given on the login page. If you need to log in as an Auditor you are required to enter the OTP send it to the registered mobile number of the Auditor. You can't log in as an auditor without verifying the OTP. We have used API to generate an OTP message to an Auditor. This file has 9 modules(which includes Login and sign up) in it which perform different tasks that are useful to a firm. This project is focused on an accountancy firm. With the help of this application, the user can update their work that will store in the backend database(ie: MongoDB). And that can be seen by the auditor. So that auditor has the full vision of his article assistant's work. If the article assistant completes their work they can update this application and can receive new work from the auditor. Article assistants can also request the travel allowance from the auditor. Then Auditor can check for the requested amount and add it to the article assistant's salary. Then Article assistant can view their salary of them with the travel allowance allocated by the Auditor.


# Points to note:
- This might not be a full-fledged project.
- It can be extendable if needed.
- Since we have converted this into an exe file, this can be used without having the python interpreter.
- If you need to know about how every sector works in this application, you might need a python interpreter and the required modules.
