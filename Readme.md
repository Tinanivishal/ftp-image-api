# 🖼️ Python FTP Image Server with HTTP & HTTPS Support

This project sets up a simple Python-based HTTP/HTTPS server to **serve images** stored in a local FTP directory. It supports:

- 📂 Serving static images from a specified folder
- 🔐 Secure HTTPS access using SSL certificates
- 🔁 HTTP to HTTPS redirection
- 🔧 Threaded server for handling multiple requests

---

## 📁 Directory Structure

```bash
.
├── server.py              # Main server script
├── .env                   # (Optional) Stores environment variables for SSL paths
└── /upload                # Folder where your FTP server stores uploaded images
🚀 How to Run
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/python-ftp-image-server.git
cd python-ftp-image-server
2️⃣ Set Environment Variables for SSL
🔐 Never hardcode your certificate paths! Use environment variables or a .env file.

Option 1: Export in terminal

bash
Copy
Edit
export SSL_CERT_FILE=/etc/letsencrypt/live/yourdomain.com/fullchain.pem
export SSL_KEY_FILE=/etc/letsencrypt/live/yourdomain.com/privkey.pem
Option 2: Create a .env file

env
Copy
Edit
SSL_CERT_FILE=/etc/letsencrypt/live/yourdomain.com/fullchain.pem
SSL_KEY_FILE=/etc/letsencrypt/live/yourdomain.com/privkey.pem
(Install python-dotenv if you want to load .env automatically in your script.)

3️⃣ Run the Server
bash
Copy
Edit
python3 server.py
HTTP runs on port 8089 and redirects to HTTPS.

HTTPS serves images on port 8087.

🔧 Configuration

Setting	Default Value
HTTP Port	8089
HTTPS Port	8087
Image Directory	/home/ftpserveradmin/upload/
SSL Cert Path	From environment: $SSL_CERT_FILE
SSL Key Path	From environment: $SSL_KEY_FILE
🛡️ Security Tips
Keep your .pem and .key files safe — never commit them to GitHub.

Always use HTTPS in production.

Use a reverse proxy (like Nginx) for more flexibility and caching.

📸 Example
bash
Copy
Edit
https://yourdomain.com:8087/sample.jpg
📂 FTP + API Setup
You can configure your FTP server to store uploaded images in the upload/ directory. This script will automatically serve whatever is stored there.

🔗 Author & Repo
Made with ❤️ by Vishal Tinani