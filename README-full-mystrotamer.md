
# 🛡️ Complete Setup for User mystrotamer with Flask, SSH, and GitHub

---

## 🧱 1. Create a New User on the Server

```bash
sudo adduser mystrotamer
sudo usermod -aG sudo mystrotamer
sudo mkdir -p /home/mystrotamer/.ssh
sudo chown mystrotamer:mystrotamer /home/mystrotamer/.ssh
sudo chmod 700 /home/mystrotamer/.ssh
```

---

## 🔐 2. Generate SSH Key from Windows to Server

```powershell
ssh-keygen -t ed25519 -C "mystrotamer-key-local to server" -f ${env:USERPROFILE}\.ssh\id_mystrotamer
Get-Content ${env:USERPROFILE}\.ssh\id_mystrotamer.pub | Set-Clipboard
```

### 📥 Paste the Key into the Server:

```bash
sudo nano /home/mystrotamer/.ssh/authorized_keys
sudo chmod 600 /home/mystrotamer/.ssh/authorized_keys
sudo chown mystrotamer:mystrotamer /home/mystrotamer/.ssh/authorized_keys
```

### ✅ Test the Connection:

```powershell
ssh -i ${env:USERPROFILE}\.ssh\id_mystrotamer -p 13976 mystrotamer@78.47.205.8
```

---

## 🔗 3. Generate GitHub Key from Server

```bash
ssh-keygen -t ed25519 -C "mystrotamer-key-local to server" -f ~/.ssh/id_github_mystrotamer
cat ~/.ssh/id_github_mystrotamer.pub
```

📌 Add the key to GitHub → Settings → SSH Keys.

```bash
ssh -T git@github.com
```

---

## 📦 4. Clone the Project from GitHub

```bash
cd ~
git clone git@github.com:TamerOnLine/mystrotamer.git
cd mystrotamer
```

---

## 🐍 5. Setup Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 💻 6. Run Flask Locally

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=7777
```

---

## 🌀 7. Setup Gunicorn and Nginx

```bash
gunicorn --bind 127.0.0.1:8888 myapp:app
```

Configure Nginx File:

```nginx
server {
    listen 80;
    server_name mystrotamer.com;

    location / {
        proxy_pass http://127.0.0.1:8888;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/mystrotamer /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## 🔒 8. Enable HTTPS

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d mystrotamer.com --http-01-port 80
```

---

## 🛡️ 9. Enable UFW Firewall

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80,443,7777/tcp
sudo ufw enable
```

---

## ✅ Setup Completed Successfully 🎉
