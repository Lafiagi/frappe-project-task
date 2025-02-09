# Project Management System - Frappe Framework

## Prerequisites
- Python 3.10+
- Node.js 14+
- MariaDB
- Redis

## Installation Steps

1. Install bench:
```bash
pip install frappe-bench
```

2. Initialize bench directory:
```bash
bench init frappe-bench
cd frappe-bench
```

3. Create new app:
```bash
bench new-app project_management
```

4. Create new site:
```bash
bench new-site eglobal.local
```

5. Install app on site:
```bash
bench --site eglobal.local install-app project_management
```

6. Start development server:
```bash
bench start
```




# Debugging Guide for Project Management System

## Common Issues and Solutions

### 1. Slow API Performance
**Problem**: API endpoints taking too long to respond
**Solution**:
- Implement proper indexing on frequently queried fields
- Use batch fetching for related records
- Implement caching for frequently accessed data
- Use pagination for large datasets

### 2. Memory Leaks
**Problem**: System memory usage increasing over time
**Solution**:
- Clear cache periodically using scheduled jobs
- Implement proper garbage collection
- Monitor memory usage using Frappe's built-in monitoring tools

### 3. Database Connection Issues
**Problem**: Intermittent database connection errors
**Solution**:
- Check connection pool settings
- Implement connection retry logic
- Monitor and log connection states

## Debugging Process

1. Enable Verbose Logging:
```python
bench --site eglobal.local set-log-level debug
```

2. Check Error Logs:
```bash
bench --site eglobal.local show-logs
```

3. Profile Code Performance:
```python
import cProfile
import frappe

def profile_function():
    cProfile.runctx('frappe.get_all("Task")', globals(), locals(), 'profile.stats')
```

## Performance Monitoring

1. Setup Monitoring:
```bash
bench setup monitoring
```

2. Monitor System Health:
```bash
bench doctor
```

3. Check Slow Queries:
```sql
SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE TIME > 5;
```
# frappe-project-task
