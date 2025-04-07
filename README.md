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

- 🖥️ **Frontend Repository:** [amlak-front (React + MUI)](https://github.com/mary-h-dev/amlak-front)
- 🔙 **Backend Repository:** [amlak-api (Django + DRF + Langchain)](https://github.com/mary-h-dev/AmlakeenoApi-Django-DRF)

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mary-h-dev/AmlakeenoApi-Django-DRF.git
cd AmlakeenoApi-Django-DRF





