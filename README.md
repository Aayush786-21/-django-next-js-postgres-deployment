# Django + Next.js Hello World Project

This project is a full-stack web application using Django (with Django REST Framework) for the backend and Next.js (React) for the frontend, with Docker containerization and Docker Hub deployment.

---

## Project Structure

```
django-helloworld/
├── 📁 backend/                 # Django backend
│   ├── 📁 hello/              # Django app
│   ├── 📁 helloworld/         # Django project settings
│   ├── 📁 migrations/         # Database migrations
│   ├── manage.py              # Django management script
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment variables
│   ├── Dockerfile             # Backend Docker image
│   ├── .dockerignore          # Docker ignore patterns
│   └── run.sh                 # Convenience script
├── 📁 frontend/               # Next.js frontend
│   ├── 📁 app/                # Next.js app directory
│   ├── 📁 lib/                # Utility libraries
│   ├── package.json           # Node.js dependencies
│   ├── Dockerfile             # Frontend Docker image
│   └── .dockerignore          # Docker ignore patterns
├── docker-compose.yml         # Full stack orchestration
├── .env                       # Environment variables
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore patterns
```

---

## Quick Start with Docker Hub

### Prerequisites
- Docker and Docker Compose installed
- Docker Hub account

### 1. Configure Environment
```bash
# Copy and edit the environment file
cp .env.example .env
# Update DOCKERHUB_USERNAME and other variables
```

### 2. Build and Push Images (Manual)
```bash
# Build and push backend image
cd backend
docker build -t yourusername/django-helloworld-backend:latest .
docker push yourusername/django-helloworld-backend:latest

# Build and push frontend image
cd ../frontend
docker build -t yourusername/django-helloworld-frontend:latest .
docker push yourusername/django-helloworld-frontend:latest
```

### 3. Deploy Full Stack
```bash
# Deploy the complete application
docker-compose up -d
```

### 4. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Database**: localhost:5432

---

## Docker Hub Images

The application uses pre-built Docker images from Docker Hub:

- **Backend**: `yourusername/django-helloworld-backend:latest`
- **Frontend**: `yourusername/django-helloworld-frontend:latest`

### Building and Pushing Images

```bash
# Build and push backend image
cd backend
docker build -t yourusername/django-helloworld-backend:latest .
docker push yourusername/django-helloworld-backend:latest

# Build and push frontend image
cd ../frontend
docker build -t yourusername/django-helloworld-frontend:latest .
docker push yourusername/django-helloworld-frontend:latest
```

---

## Local Development

### Backend (Django)

#### Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables (see `.env` for required variables).
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser (optional, for admin):
   ```bash
   python manage.py createsuperuser
   ```
7. Start the server:
   ```bash
   python manage.py runserver
   ```

#### API Endpoints
- `/api/hello/` — Simple hello world API
- `/api/greetings/` — List and create greetings
- `/api/greetings/<id>/` — Retrieve, update, or delete a greeting

### Frontend (Next.js)

#### Setup
1. Go to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. The app will be available at [http://localhost:3000](http://localhost:3000)

---

## Environment Variables

### Root Level (.env)
```bash
# Docker Hub Configuration
DOCKERHUB_USERNAME=yourusername

# Database Configuration
DB_NAME=helloworld_db
DB_USER=postgres
DB_PASSWORD=your-secure-password

# Django Configuration
SECRET_KEY=your-django-secret-key-change-this-in-production
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
LANGUAGE_CODE=en-us
TIME_ZONE=UTC

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Docker Commands

### Development
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Management
```bash
# Check status
docker-compose ps

# Restart services
docker-compose restart

# View logs for specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

---

## Services

### Development Stack
- **Frontend**: Next.js on port 3000
- **Backend**: Django API on port 8000
- **Database**: PostgreSQL on port 5432

---

## Running Tests
To run backend tests:
```bash
cd backend
python manage.py test
```

---

## Notes
- The backend uses PostgreSQL by default. You can change DB settings in `.env`.
- CORS is enabled for local frontend development.
- The Django admin is available at `/admin/`.
- All services are containerized and can be deployed from Docker Hub images.
- The application includes health checks for all services.
