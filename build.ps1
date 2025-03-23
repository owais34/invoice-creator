# Define paths
$clientFolder = "C:\Users\owais\OneDrive\Desktop\invoice-creator\invoice-creator-client"
$serverFolder = "C:\Users\owais\OneDrive\Desktop\invoice-creator\invoice-creator-server"
$buildFolder = "build"
$virtualEnvPath = "$serverFolder\.venv\Scripts\Activate.ps1"

# Step 1: Run 'npm run build' in the client folder (React app build)
Write-Host "Running 'npm run build' in the client folder..."
Set-Location -Path $clientFolder
npm install
npm run build
Write-Host "'npm run build' completed successfully."

# Step 2: Copy the build folder to the server folder as 'client'
Write-Host "Copying build folder to the server folder as 'client'..."
Copy-Item -Path "$clientFolder\$buildFolder" -Destination "$serverFolder\client" -Recurse -Force
Write-Host "Build folder copied successfully."

