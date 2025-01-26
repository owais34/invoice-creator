
# Define the virtual environment name and the Python script to run
$envName = ".venv"
$pythonScript = "app.py"

# Step 1: Create the virtual environment
python -m venv $envName

# Step 2: Activate the virtual environment
$activateScript = ".\$envName\Scripts\Activate.ps1"
& $activateScript

# Step 3: Install any required dependencies (Optional step, modify as needed)
# Uncomment the following line if you have a requirements.txt file
pip install -r requirements.txt

# Step 4: Run the Python script
flask db upgrade

python $pythonScript
