# 1. Use a base Python image
FROM python:3.11-slim

# 2. Install system-level dependencies for WhiteboxTools (like libgomp, wget, and unzip)
RUN apt-get update && apt-get install -y \
    libgomp1 \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory
WORKDIR /app

# 4. Copy requirements first and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Automatically download WhiteboxTools for Linux inside the container
# This removes the need to have a local 'WBT_Linux' folder.
# We move it to /app/WBT to match the project structure.
RUN python -c "import whitebox; whitebox.download_wbt()" && \
    mv $(python -c "import whitebox, os; print(os.path.dirname(whitebox.__file__))")/WBT /app/WBT

# 6. Copy the rest of the app code (respects .dockerignore)
COPY . .

# 7. Set environment variables
ENV WBT_PATH="/app/WBT"

# 8. Launch Streamlit
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]