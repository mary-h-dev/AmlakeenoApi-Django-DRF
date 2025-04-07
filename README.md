# 🧠 Amlak API – Backend for Tehran Property Finder

This is the **backend API** for the Amlak platform, built with Django and Django REST Framework. It provides secure and scalable endpoints to manage listings, users, locations, and more — designed for real estate listings and property search in Tehran.

---

## 🚀 Features

- 🏡 Manage rental and sale property listings
- 🔐 JWT authentication and social login support (via Djoser & AllAuth)
- 🌍 Location-based search with GIS and GDAL
- 🗓️ Persian date support using `django-jalali-date` and `jdatetime`
- 💬 Email templating with `django-templated-mail`
- 🧠 AI-powered endpoints with `LangChain` and `OpenAI API`
- 🧾 Excel export support via `openpyxl`
- ⚡ Redis support for async tasks and caching
- 📊 Admin interface and debug toolbar for development

---

## 🛠️ Stack

| Layer           | Tools |
|-----------------|-------|
| **Framework**   | Django 4, Django REST Framework |
| **Auth**        | JWT (`simplejwt`), Djoser, AllAuth |
| **Database**    | PostgreSQL / MySQL |
| **Geo & Map**   | GDAL, `djangorestframework-gis` |
| **Async / Cache** | Redis, Celery-ready |
| **Other Tools** | Python-dotenv, Pandas, Templated Mail, Jalali Support |

---
## 🔗 Related Projects

- 🖥️ **Frontend Repository:** [amlak-front (React + Leaflet + MUI)](h[ttps://github.com/mary-h-dev/amlak-front](https://github.com/mary-h-dev/amlakeeno-client-react-leafLet))
- 🔙 **Backend Repository:** [amlak-api (Django + DRF + GEODjango)](https://github.com/mary-h-dev/mary-h-dev/amlakeeno-api-django-drf)

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mary-h-dev/mary-h-dev/amlakeeno-api-django-drf.git
cd mary-h-dev/amlakeeno-api-django-drf





