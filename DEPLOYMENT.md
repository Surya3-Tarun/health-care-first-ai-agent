# HEALTHFIRST AI - Platform-Specific Deployment

## 🌐 Deployment Platforms Overview

| Platform | Difficulty | Cost | Best For | Setup Time |
|----------|-----------|------|---------|-----------|
| Streamlit Cloud | ⭐ Easy | Free | Quick deployment | 5 min |
| Heroku | ⭐⭐ Medium | Free/Paid | Learning & testing | 10 min |
| Docker + AWS | ⭐⭐⭐ Hard | Paid | Production | 30 min |
| PythonAnywhere | ⭐⭐ Medium | Free/Paid | Simple hosting | 15 min |
| Google Cloud | ⭐⭐⭐ Hard | Paid | Enterprise | 30 min |
| DigitalOcean | ⭐⭐ Medium | Paid | Reliable hosting | 20 min |

---

## 1️⃣ Streamlit Cloud (RECOMMENDED - Most Simple)

### ✅ Advantages
- Completely free
- 1-click deployment from GitHub
- Auto-updates on git push
- Built-in SSL/HTTPS
- 24/7 uptime
- Generous quotas

### 📋 Prerequisites
- GitHub account
- GitHub repository with code
- Groq API key

### 🚀 Deployment Steps

#### Step 1: Prepare GitHub Repository
```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Create main branch
git branch -M main

# Add remote (replace with your URL)
git remote add origin https://github.com/your-username/healthfirst-ai.git

# Push to GitHub
git push -u origin main
```

#### Step 2: Push Code to GitHub
```bash
# Make sure you're in the correct directory
cd Health_Care_First_AI

# Push all code
git push origin main
```

#### Step 3: Deploy on Streamlit Cloud
```
1. Visit: https://streamlit.io/cloud
2. Click "New app"
3. Select "GitHub"
4. Select repository: healthfirst-ai
5. Select branch: main
6. Select main file: app.py
7. Click "Deploy"
```

#### Step 4: Configure Secrets
```
1. Once deployed, click on hamburger menu (top right)
2. Click "Settings"
3. Click "Secrets"
4. Add your secret:

   GROQ_API_KEY = "gsk_xxxxxxxxxxxxx"

5. Save
6. App will auto-restart with the secret
```

#### Step 5: Share Your App
```
Your app is live at:
https://your-username-healthfirst-ai.streamlit.app

Share this URL with others!
```

### 📊 Monitoring
- View logs in "Logs" tab
- Check app health status
- Monitor app usage metrics

---

## 2️⃣ Heroku Deployment

### ✅ Advantages
- Easy deployment
- Custom domain support
- Good for portfolio projects
- Free tier available

### 📋 Prerequisites
- Heroku account (free at heroku.com)
- Heroku CLI installed
- Git installed

### 🚀 Installation

**Windows:**
```bash
# Download and run installer from:
https://devcenter.heroku.com/articles/heroku-cli

# Or use Chocolatey:
choco install heroku-cli
```

**macOS:**
```bash
# Using Homebrew
brew tap heroku/brew && brew install heroku

# Or using installer
# Download from Heroku website
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### 🚀 Deployment Steps

#### Step 1: Create Configuration Files

**Procfile:**
```
web: streamlit run app.py --logger.level=error --server.port=$PORT --server.enableCORS=false
```

**.slugignore:**
```
*.pyc
__pycache__/
.git
.gitignore
venv/
.env
.DS_Store
```

**runtime.txt:**
```
python-3.9.13
```

#### Step 2: Prepare Git Repository
```bash
# Initialize git if not done
git init

# Add files
git add .

# Commit
git commit -m "Prepare for Heroku deployment"

# Verify you're on main branch
git branch -M main
```

#### Step 3: Deploy to Heroku
```bash
# Login to Heroku
heroku login

# Create app (replace with your app name)
heroku create healthfirst-ai-yourname

# Set environment variable
heroku config:set GROQ_API_KEY=your_key_here

# Deploy
git push heroku main

# View logs
heroku logs --tail

# Open app
heroku open
```

#### Step 4: Monitor & Update
```bash
# View logs
heroku logs --tail

# View app status
heroku status

# Scale app (paid feature)
heroku ps:scale web=1

# Update app
git push heroku main
```

### 🔧 Troubleshooting
```bash
# Check app status
heroku ps

# Restart app
heroku restart

# View all config variables
heroku config

# Check app activity
heroku activity

# Get app URL
heroku open --show-url
```

---

## 3️⃣ Docker + AWS EC2

### ✅ Advantages
- Full control
- Scalable
- Professional setup
- Multi-region support

### 📋 Prerequisites
- AWS account (free tier available)
- Docker installed
- AWS CLI configured

### 🚀 Deployment Steps

#### Step 1: Create Docker Image
```bash
# In project directory
cd Health_Care_First_AI

# Build Docker image
docker build -t healthfirst-ai:latest .

# Test locally
docker run -e GROQ_API_KEY=your_key -p 8501:8501 healthfirst-ai:latest
```

#### Step 2: Push to AWS ECR
```bash
# Create ECR repository
aws ecr create-repository --repository-name healthfirst-ai

# Get login token
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_AWS_ID.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag healthfirst-ai:latest YOUR_AWS_ID.dkr.ecr.us-east-1.amazonaws.com/healthfirst-ai:latest

# Push to ECR
docker push YOUR_AWS_ID.dkr.ecr.us-east-1.amazonaws.com/healthfirst-ai:latest
```

#### Step 3: Launch EC2 Instance
```bash
# Create security group
aws ec2 create-security-group \
  --group-name healthfirst-sg \
  --description "Security group for HEALTHFIRST AI"

# Allow port 8501
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp \
  --port 8501 \
  --cidr 0.0.0.0/0

# Launch t2.micro instance (free tier)
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --security-group-ids sg-xxxxx
```

#### Step 4: Connect & Deploy
```bash
# SSH into instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Install Docker
sudo yum update -y
sudo yum install -y docker

# Start Docker
sudo systemctl start docker

# Pull image
docker pull YOUR_AWS_ID.dkr.ecr.us-east-1.amazonaws.com/healthfirst-ai:latest

# Run container
docker run -e GROQ_API_KEY=your_key -p 8501:8501 -d YOUR_AWS_ID.dkr.ecr.us-east-1.amazonaws.com/healthfirst-ai:latest

# Access app
# Visit: http://your-instance-ip:8501
```

---

## 4️⃣ Google Cloud Run (Easiest Cloud Option)

### ✅ Advantages
- Serverless (no servers to manage)
- Auto-scaling
- Pay only for usage
- Simple deployment

### 🚀 Deployment Steps

#### Step 1: Install Google Cloud CLI
```bash
# Visit: https://cloud.google.com/sdk/docs/install
# Follow installation instructions for your OS
```

#### Step 2: Initialize Project
```bash
# Set project ID
gcloud config set project YOUR_PROJECT_ID

# Configure Docker
gcloud auth configure-docker
```

#### Step 3: Build & Push Image
```bash
# Build image
docker build -t gcr.io/YOUR_PROJECT_ID/healthfirst-ai .

# Push to Google Container Registry
docker push gcr.io/YOUR_PROJECT_ID/healthfirst-ai
```

#### Step 4: Deploy
```bash
# Deploy to Cloud Run
gcloud run deploy healthfirst-ai \
  --image gcr.io/YOUR_PROJECT_ID/healthfirst-ai \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GROQ_API_KEY=your_key \
  --memory 512Mi \
  --timeout 3600
```

#### Step 5: Access Application
```
Service URL: https://healthfirst-ai-xxxxx.run.app
```

---

## 5️⃣ PythonAnywhere (Simplest Paid Option)

### ✅ Advantages
- No Docker needed
- Web-based file editor
- Simple setup
- Good documentation

### 🚀 Deployment Steps

1. **Create Account**: https://www.pythonanywhere.com
2. **Upload Files**:
   - Use "Files" section
   - Upload project files
3. **Create Web App**:
   - Create new web app
   - Choose Python 3.9
   - Select Streamlit as framework
4. **Configure**:
   - Set working directory
   - Add environment variables
5. **Run**:
   - Click "Reload"
   - Access your app URL

---

## 6️⃣ DigitalOcean App Platform

### 🚀 Deployment Steps

1. **Create DigitalOcean Account**: https://www.digitalocean.com

2. **Create App Platform**:
   - Click "Create" → "Apps"
   - Connect GitHub repository
   - Select branch: main
   - Select file: app.py

3. **Configure**:
   - Set environment variables
   - Configure domain
   - Set resources

4. **Deploy**:
   - Click "Deploy"
   - Wait for build to complete

5. **Access**:
   - Get app URL from dashboard

---

## 🔄 CI/CD Pipeline Setup

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Streamlit Cloud
        run: |
          pip install streamlit
          streamlit run app.py
        env:
          GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
```

---

## 🔒 Environment Variables Setup

### Streamlit Cloud
1. Dashboard → App settings → Secrets
2. Add: `GROQ_API_KEY = "your_key"`

### Heroku
```bash
heroku config:set GROQ_API_KEY=your_key
```

### Docker/Cloud Run
```bash
docker run -e GROQ_API_KEY=your_key -p 8501:8501 image-name
```

### Environment File
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_key"
```

---

## 📊 Performance Comparison

| Platform | Startup | Response | Cost | Scaling |
|----------|---------|----------|------|---------|
| Streamlit Cloud | Fast | <1s | Free | Auto |
| Heroku | Medium | ~1s | Free/Paid | Manual |
| Docker | Fast | <1s | Paid | Manual |
| Cloud Run | Very Fast | <500ms | Pay-per-use | Auto |
| PythonAnywhere | Medium | ~1s | Paid | Manual |

---

## 🚨 Troubleshooting by Platform

### Streamlit Cloud
```
- Clear browser cache
- Check Secrets configuration
- View logs in dashboard
- Restart app
```

### Heroku
```
heroku logs --tail
heroku restart
heroku config
heroku status
```

### Docker
```
docker ps
docker logs container_id
docker exec container_id bash
docker restart container_id
```

---

## 📈 Scaling Strategies

### Low Traffic (< 100 users/day)
- Streamlit Cloud (free)
- Small Heroku dyno
- Small Cloud Run instance

### Medium Traffic (100-1000 users/day)
- Heroku with 2+ dynos
- Cloud Run with scaling
- Docker on t2.small EC2

### High Traffic (1000+ users/day)
- Docker on larger EC2 instances
- Kubernetes cluster
- Load balancer + auto-scaling
- Database + caching layer

---

## 🎯 Recommended Path

### For Beginners
1. Start with **Streamlit Cloud** (easiest)
2. Progress to **Heroku** if needed
3. Learn **Docker** for professional setup

### For Production
1. Deploy on **Google Cloud Run** (serverless)
2. Or **AWS EC2** + **Docker** (more control)
3. Use **Load Balancer** for scaling

### For Portfolio
1. Use **Streamlit Cloud** (free & impressive)
2. Custom domain with **Vercel** or **Cloudflare**
3. Link in resume & GitHub

---

## ✅ Deployment Verification Checklist

After deployment, verify:
- [ ] App loads without errors
- [ ] All pages are accessible
- [ ] AI responses work correctly
- [ ] API key is properly configured
- [ ] No sensitive data in logs
- [ ] HTTPS is enabled
- [ ] Performance is acceptable
- [ ] Mobile view works
- [ ] Emergency alerts show properly
- [ ] First aid guides display correctly

---

## 🎉 You're Deployed!

Your HEALTHFIRST AI is now live and accessible to the world!

**Next Steps:**
1. Share your app URL
2. Monitor usage & performance
3. Gather user feedback
4. Make improvements
5. Scale if needed

**Questions?** Refer to specific platform documentation.
