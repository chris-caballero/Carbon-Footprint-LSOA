FROM python:3.8.3

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Copy the rest of the code
COPY . /app

EXPOSE 8888

# Set environment variables
ENV JUPYTER_ENABLE_LAB=yes
ENV JUPYTER_TOKEN=docker

# Specify the command to run when the container starts
CMD ["jupyter-lab", "--ip=0.0.0.0", "--allow-root", "carbon_emission_analysis.ipynb"]

