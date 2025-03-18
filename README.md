# ProQR

![ProQR Logo](assets/app_image.png)

## Overview

ProQR is a simple, fast, and responsive web application that generates QR codes from URLs. 
Built with Python and Flask, this lightweight tool offers an intuitive interface for creating QR codes that can be instantly downloaded and shared.

## ✅ Features

- **Instant QR Code Generation** - Quickly convert any URL into a scannable QR code
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **User-Friendly Interface** - Clean, minimalist design focused on usability
- **No Registration Required** - Generate QR codes without creating an account
- **Free to Use** - No hidden fees or premium features

## 🚀 Demo

The application is live and deployed on Heroku: [Visit ProQR](https://pro-qr.app/)

## 💻 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Deployment**: Heroku
- **QR Generation**: qrcode Python Library, io, base64


## 📱 Usage

1. Visit the ProQR website
2. Enter the URL you want to convert into a QR code in the input field
3. Click the "Generate QR" button
4. Your QR code will appear instantly
5. Scan the QR code with any QR reader app to visit the website

## 🛠️ Local Development

### Prerequisites

- Python 3.6+
- pip Package Manager
- flask Package
- qrcode Package

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/proqr.git
   cd proqr
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python main.py or python.exe .\main.py
   ```

5. Open your browser and navigate to:
   ```
   a link will be created after you run the application
   ```

## 📋 Project Structure

```
proqr/
├── main.py                  # Main Flask application
├── templates/
│   └── index.html          # Main HTML template
├── requirements.txt        # Project dependencies
└── Procfile               # Heroku deployment configuration (Not Used Locally)
```

## 🔄 Future Improvements

- Add option to download the generated QR code
- Implement custom QR code styles and colors
- Add QR code history for returning users
- Integrate with social media for direct sharing

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing


1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 📞 Contact

If you have any questions or suggestions, please open an issue or contact the project maintainer.

---

Made with ❤️ by Alexandru Bogdan.
