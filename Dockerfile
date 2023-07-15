# Use a base image with the desired Python version
FROM python:3.8.3

# Set the working directory inside the container
WORKDIR /

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Specify the command to run when the container starts
CMD ["jupyter-lab", "carbon_emission_analysis.ipynb"]

