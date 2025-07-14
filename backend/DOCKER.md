# Docker Setup for Django Backend

This document explains how to use Docker with the Django backend.

## Quick Start

### Development Environment
```bash
# Start development environment with PostgreSQL
./docker-run.sh dev

# Or manually
docker-compose up --build
```

### Production Environment
```bash
# Start production environment
./docker-run.sh prod

# Or manually
docker-compose -f docker-compose.prod.yml up --build -d
```

## Available Commands

Use the convenience script `./docker-run.sh` for common operations:

```bash
./docker-run.sh dev              # Start development environment
./docker-run.sh prod             # Start production environment
./docker-run.sh build            # Build development Docker image
./docker-run.sh build-prod       # Build production Docker image
./docker-run.sh stop             # Stop development containers
./docker-run.sh stop-prod        # Stop production containers
./docker-run.sh logs             # Show development logs
./docker-run.sh logs-prod        # Show production logs
./docker-run.sh shell            # Open shell in backend container
./docker-run.sh migrate          # Run database migrations
./docker-run.sh makemigrations   # Create new migrations
./docker-run.sh createsuperuser  # Create Django superuser
./docker-run.sh test             # Run Django tests
```

## Docker Files

- `Dockerfile` - Development Docker image
- `Dockerfile.prod` - Production Docker image with Gunicorn
- `docker-compose.yml` - Development environment with PostgreSQL
- `docker-compose.prod.yml` - Production environment
- `.dockerignore` - Files to exclude from Docker build

## Environment Variables

### Development
Environment variables are set in `docker-compose.yml`:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to True for development
- `DB_HOST` - Set to `db` (Docker service name)
- `DB_NAME`, `DB_USER`, `DB_PASSWORD` - Database credentials

### Production
Use environment variables or `.env` file:
```bash
export SECRET_KEY=your-secret-key
export DB_PASSWORD=your-db-password
# ... other variables
```

## Services

### Development
- **Backend**: Django development server on port 8000
- **Database**: PostgreSQL 15 on port 5432

### Production
- **Backend**: Gunicorn with 3 workers on port 8000
- **Database**: PostgreSQL 15 (internal)

## Health Checks

Both development and production setups include health checks:
- Database: `pg_isready` command
- Backend: HTTP request to `/api/hello/` endpoint

## Security Features

- Non-root user (`django`) in containers
- Multi-stage build for production
- Environment variable configuration
- Health checks for monitoring

## Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Check what's using port 8000
   lsof -i :8000
   # Stop the service or change port in docker-compose.yml
   ```

2. **Database connection issues**:
   ```bash
   # Check if database is running
   docker-compose ps
   # Check database logs
   docker-compose logs db
   ```

3. **Permission issues**:
   ```bash
   # Make scripts executable
   chmod +x docker-run.sh run.sh
   ```

### Useful Commands

```bash
# View running containers
docker ps

# View logs
docker-compose logs -f backend

# Execute commands in container
docker-compose exec backend python manage.py shell

# Clean up
docker-compose down -v  # Remove volumes too
docker system prune     # Remove unused images/containers
```

## Production Deployment

For production deployment:

1. Set proper environment variables
2. Use `Dockerfile.prod` and `docker-compose.prod.yml`
3. Configure reverse proxy (nginx) if needed
4. Set up SSL certificates
5. Configure proper logging
6. Set up monitoring and backups

Example production deployment:
```bash
# Build and start production
./docker-run.sh build-prod
./docker-run.sh prod

# Check status
docker-compose -f docker-compose.prod.yml ps
``` 