Here's a `README.md` file for running the backend server and setting up the MongoDB environment variables.

---

# Healthcare Revenue Cycle Management (HRCM) Backend

This is the backend server for the Healthcare Revenue Cycle Management (HRCM) application. It is built using **FastAPI** and uses **MongoDB** for data storage.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.9 or later
- MongoDB
- pip (Python package manager)

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd hrcm_backend
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to manage dependencies:

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. MongoDB Setup

Make sure MongoDB is running locally or on a remote server. If it is not installed, you can download and install it from [MongoDB Official Website](https://www.mongodb.com/try/download/community).

### 5. Configure Environment Variables

Create a `.env` file in the project root directory and add the following content:

```env
MONGO_URI=YOUR_MONGO_URL
MONGO_DB=hrcm
```

- **`MONGO_URI`**: The connection URI for MongoDB. Update this to your MongoDB instance URL if running on a remote server.
- **`MONGO_DB`**: The name of the database to use (default: `hrcm`).

### 6. Run the Server

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.
