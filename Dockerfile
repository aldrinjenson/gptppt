# Use a Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir streamlit

# Install Marp CLI
RUN apt-get update && apt-get install -y wget && \
    wget -qO- https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @marp-team/marp-cli

# Expose the port streamlit runs on
EXPOSE 8501

# Command to run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
