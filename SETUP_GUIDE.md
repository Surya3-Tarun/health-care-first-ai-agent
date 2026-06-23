# HEALTHFIRST AI - Complete Setup & Deployment Guide

## 🎯 Quick Start (5 minutes)

### Step 1: Extract Files
Extract the project files to your preferred directory.

### Step 2: Install Python
Ensure Python 3.8+ is installed:
```bash
python --version
```

### Step 3: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Get Groq API Key
1. Visit: https://console.groq.com
2. Create free account
3. Generate API key
4. Copy API key

### Step 6: Configure .env
```bash
# Edit .env file
GROQ_API_KEY=your_api_key_here
```

### Step 7: Run Application
```bash
streamlit run app.py
```

Application opens at: http://localhost:8501

---

## 📦 Complete Installation Steps

### Windows Installation

```batch
REM 1. Navigate to project directory
cd "C:\Path\To\Health_Care_First_AI"

REM 2. Create virtual environment
python -m venv venv

REM 3. Activate virtual environment
venv\Scripts\activate

REM 4. Upgrade pip
python -m pip install --upgrade pip

REM 5. Install dependencies
pip install -r requirements.txt

REM 6. Configure environment
REM Edit .env file and add your Groq API key

REM 7. Run application
streamlit run app.py
```

### macOS Installation

```bash
# 1. Navigate to project directory
cd ~/Health_Care_First_AI

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt

# 6. Configure environment
# Edit .env file and add your Groq API key

# 7. Run application
streamlit run app.py
```

### Linux Installation (Ubuntu/Debian)

```bash
# 1. Install Python dependencies
sudo apt-get install python3 python3-pip python3-venv

# 2. Navigate to project directory
cd ~/Health_Care_First_AI

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate virtual environment
source venv/bin/activate

# 5. Upgrade pip
python -m pip install --upgrade pip

# 6. Install dependencies
pip install -r requirements.txt

# 7. Configure environment
# Edit .env file and add your Groq API key

# 8. Run application
streamlit run app.py
```

---

## 🔑 Getting Groq API Key

### Free Tier (No Credit Card Required)

1. **Visit Groq Console**
   - URL: https://console.groq.com

2. **Sign Up**
   - Create account with email
   - Verify email

3. **Generate API Key**
   - Go to API Keys section
   - Click "Create New API Key"
   - Copy the key

4. **Add to .env**
   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
   ```

### Quota & Limits
- **Free Tier**: ~30 requests per minute
- **Rate Limit**: Generous for testing
- **No Expiration**: Key valid indefinitely
- **Upgrade Available**: For higher volumes

---

## ✅ Verification

### Test Installation
```bash
# Activate virtual environment first
# Then run:
python -c "import streamlit; import groq; import pandas; print('✓ All dependencies OK')"
```

### Test Groq Connection
```bash
# Make sure .env has your API key
python -c "from groq import Groq; print('✓ Groq connection OK')"
```

### Test Application Start
```bash
streamlit run app.py --logger.level=error
```

---

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free)

**Pros:**
- ✅ Free hosting
- ✅ Auto deployment from GitHub
- ✅ SSL included
- ✅ Custom domain support
- ✅ Zero configuration

**Steps:**

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/username/repo.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Click "New app"
   - Select GitHub repo
   - Select branch: `main`
   - Select file: `app.py`
   - Click "Deploy"

3. **Configure Secrets**
   - In app settings, go to "Secrets"
   - Add:
     ```
     GROQ_API_KEY = "your_key_here"
     ```
   - Save

4. **Access App**
   - Your app is now live!
   - Share the public URL

---

### Option 2: Heroku (Free with Limitations)

**Pros:**
- ✅ Simple deployment
- ✅ Good for learning
- ✅ Custom domain support

**Steps:**

1. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Create Procfile**
   ```bash
   # Create file named "Procfile" (no extension)
   # Content:
   web: streamlit run app.py --logger.level=error --server.port=$PORT
   ```

3. **Create .slugignore**
   ```bash
   # File: .slugignore
   # Content:
   *.pyc
   __pycache__/
   .git
   .gitignore
   ```

4. **Deploy**
   ```bash
   # Login to Heroku
   heroku login

   # Create app
   heroku create your-app-name

   # Set environment variables
   heroku config:set GROQ_API_KEY=your_key

   # Push code
   git push heroku main

   # View logs
   heroku logs --tail

   # Open app
   heroku open
   ```

---

### Option 3: Docker Deployment

**Prerequisites:**
- Docker installed: https://www.docker.com/products/docker-desktop

**Steps:**

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   RUN apt-get update && apt-get install -y \
       build-essential \
       curl \
       software-properties-common \
       git \
       && rm -rf /var/lib/apt/lists/*
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create .dockerignore**
   ```
   .git
   .gitignore
   __pycache__
   *.pyc
   .venv
   venv
   .env
   .DS_Store
   ```

3. **Build Image**
   ```bash
   docker build -t healthfirst-ai .
   ```

4. **Run Locally**
   ```bash
   docker run -e GROQ_API_KEY=your_key -p 8501:8501 healthfirst-ai
   ```

5. **Deploy to Cloud**

   **AWS ECS:**
   ```bash
   # Push to ECR
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
   docker tag healthfirst-ai 123456789.dkr.ecr.us-east-1.amazonaws.com/healthfirst-ai
   docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/healthfirst-ai
   ```

   **Google Cloud Run:**
   ```bash
   # Configure authentication
   gcloud auth configure-docker

   # Build and push
   docker build -t gcr.io/PROJECT_ID/healthfirst-ai .
   docker push gcr.io/PROJECT_ID/healthfirst-ai

   # Deploy
   gcloud run deploy healthfirst-ai \
     --image gcr.io/PROJECT_ID/healthfirst-ai \
     --platform managed \
     --region us-central1 \
     --set-env-vars GROQ_API_KEY=your_key
   ```

---

### Option 4: PythonAnywhere (Simple Python Hosting)

1. **Visit**: https://www.pythonanywhere.com
2. **Sign up** for free account
3. **Upload files** via Web interface
4. **Configure WSGI** file for Streamlit
5. **Set environment variables** in settings
6. **Access your app**

---

### Option 5: AWS EC2

**Steps:**

1. **Launch EC2 Instance**
   - OS: Ubuntu 20.04 LTS
   - Instance: t2.micro (free tier)

2. **Connect and Install**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv
   
   git clone your-repo
   cd repo
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   
   # Set environment variable
   export GROQ_API_KEY=your_key
   
   # Run with screen or tmux
   streamlit run app.py
   ```

3. **Configure Security**
   - Open port 8501 in security group
   - Use Elastic IP for stability

4. **Access Application**
   - Visit: `http://your-instance-ip:8501`

---

## 📊 Performance Optimization

### For Production

1. **Enable Caching**
   ```python
   import streamlit as st
   
   @st.cache_resource
   def load_model():
       return initialize_groq_client()
   ```

2. **Optimize Images**
   - Compress all images < 100KB
   - Use WebP format when possible

3. **Database Caching**
   - Cache API responses
   - Implement request batching

4. **Monitor Performance**
   ```bash
   streamlit run app.py --logger.level=error --client.showErrorDetails=false
   ```

---

## 🔒 Security Checklist

- [ ] .env file in .gitignore
- [ ] API keys never in code
- [ ] HTTPS enabled (all cloud platforms)
- [ ] Input validation implemented
- [ ] Output sanitization done
- [ ] Rate limiting configured
- [ ] CORS properly configured
- [ ] Secrets managed in CI/CD

---

## 🐛 Troubleshooting

### Port 8501 Already in Use
```bash
streamlit run app.py --server.port 8502
```

### Module Import Errors
```bash
pip install --upgrade -r requirements.txt
pip cache purge
```

### Groq API Errors
```bash
# Test connection
python -c "from groq import Groq; c = Groq(); print('OK')"

# Check quota
# Visit: https://console.groq.com/usage
```

### Memory Issues
```bash
# Run with increased memory
streamlit run app.py --client.maxMessageSize=1024
```

### Slow Performance
- Check internet connection
- Verify Groq API availability
- Monitor system resources
- Check for memory leaks

---

## 📞 Support Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Groq Docs**: https://console.groq.com/docs
- **GitHub Issues**: Create issue in repository
- **Community**: Streamlit Community Discord

---

## ✨ Post-Deployment

### Monitor Application
```bash
# Use these tools:
- Streamlit metrics dashboard
- Groq API usage console
- Application error logs
- User feedback surveys
```

### Maintenance
- Regular dependency updates
- Monitor API quota usage
- Update medical information regularly
- Regular security audits

### Scaling
- Increase Groq quota if needed
- Deploy multiple instances
- Use load balancer
- Implement caching layer

---

## 📝 Deployment Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Groq API key obtained
- [ ] .env file configured
- [ ] Application tested locally
- [ ] GitHub repository created
- [ ] Deployment platform selected
- [ ] Environment variables set
- [ ] SSL/HTTPS enabled
- [ ] Domain configured
- [ ] Monitoring set up
- [ ] Backup strategy in place

---

## 🎉 You're Ready!

Your HEALTHFIRST AI platform is now ready for deployment.

**Next Steps:**
1. Test locally one more time
2. Choose deployment platform
3. Deploy to production
4. Share with users
5. Gather feedback
6. Iterate and improve

---

**Questions?** Refer to README.md for more details.

**Version**: 1.0.0
**Status**: Production Ready
