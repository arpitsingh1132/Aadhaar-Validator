# Aadhaar Validator (Tkinter)

The Aadhaar Validator is a desktop-based graphical application built using **Python** and its standard **Tkinter GUI library**.  
It is designed to validate **12-digit Indian Aadhaar numbers** using the **Verhoeff algorithm**, ensuring that the entered number follows the checksum rules mandated by UIDAI.  

This project is not just a small utility – it also demonstrates my Python programming, algorithmic, and GUI design skills. As part of my portfolio, it highlights my ability to combine **real-world problem solving** with a **user-friendly interface**.  

---

## 📌 Why Aadhaar Validation?
The Aadhaar number is a **unique identification number** issued to every resident of India by the **Unique Identification Authority of India (UIDAI)**. It is widely used in:  
- Government schemes and subsidies  
- Bank account opening and KYC processes  
- Income tax filing and PAN-Aadhaar linking  
- SIM card activation  
- Public distribution system (PDS) benefits  

Because Aadhaar numbers are critical, validating them before use helps prevent:  
- Typing mistakes while entering data  
- Fraudulent or fake Aadhaar usage  
- Incomplete or incorrect records in databases  

This project ensures that the **Aadhaar number is structurally valid** before it can be processed. It does not verify ownership against UIDAI servers, but it applies the **checksum algorithm** that real systems also use.

---

## ✨ Features (Explained in Detail)

1. **Aadhaar Validation with Verhoeff Algorithm**  
   - Every Aadhaar number has a checksum digit that can be validated mathematically.  
   - The application uses the Verhoeff algorithm to instantly check if a number is valid.  
   - Incorrect Aadhaar numbers are immediately flagged.  

2. **Light & Dark Theme Toggle**  
   - Users can switch between light and dark themes.  
   - This improves accessibility and makes the app comfortable to use in different lighting environments.  

3. **Aadhaar Card-Style Preview**  
   - When a valid number is entered, the app shows a card-style preview.  
   - For privacy, some digits are masked (e.g., `XXXX-XXXX-1234`).  
   - This simulates how Aadhaar numbers are displayed in real-world documents.  

4. **Validation History**  
   - The app keeps track of the last 4 Aadhaar numbers validated.  
   - This makes it easy to recheck previous inputs without retyping.  

5. **Cross-Platform Support**  
   - Works on **Windows, Linux, and macOS**, as long as Python with Tkinter is installed.  
   - The project is lightweight and does not depend on external libraries.  

6. **Error Handling & User Experience**  
   - If the input is not 12 digits or contains invalid characters, the app shows a clear error message.  
   - The interface is designed to look professional, simple, and easy to use even for non-technical users.  

---

## ⚙️ Installation (Step by Step, All OS)

Follow these detailed steps to set up and run the Aadhaar Validator on your computer.

### 1. Clone the Repository
If you have **Git** installed, open a terminal or Git Bash and run:
```bash
git clone https://github.com/arpitsingh1132/Aadhaar-Validator.git
cd Aadhaar-Validator



🖱️ Usage Guide

Launch the application by running the script.

Enter a 12-digit Aadhaar number in the input box.

Click on Validate.

The application will:

Show a green success message if the number is valid.

Show a red error message if invalid.

A card preview of the Aadhaar number (masked) will be shown.

The history panel will keep track of the last 4 validations.

Use the Theme Toggle button to switch between light and dark mode.

Use the Clear button to reset the input field.



🔮 Future Enhancements

While this is a functional project, several improvements can be added:

🔗 API Integration with UIDAI sandbox for real-time Aadhaar verification

📱 Mobile version using Kivy or Flutter

🌐 Web version using Django/Flask with the same logic

💾 Database support to log Aadhaar validations securely

🌍 Multi-language support (Hindi, Bengali, Tamil, etc.)

🧑‍💻 Contribution

Contributions are welcome!

To contribute:

Fork the repository

Create a new branch (feature-new)

Commit your changes

Push to your fork

Open a Pull Request



📦 Requirements

Python 3.8+

Tkinter library



👤 Author – Arpit Singh

Hello! I am Arpit Singh, a B.Tech IT student and aspiring full-stack developer.
This project is part of my portfolio and resume showcase, where I highlight my technical skills.

GitHub: arpitsingh1132

Skills: Python, Django, Full Stack Development, REST APIs, SQL, Git

Interests: Building real-world applications, system integration, and modern UI/UX design

I created this project not only as a practical Aadhaar Validator but also as a demonstration of my ability to:

Implement algorithms in real-world applications

Design user-friendly interfaces with Tkinter

Write clean, well-documented code

Share projects in a way that recruiters and collaborators can quickly understand
